##########
## Autohor @cappittall at all platforms 
## netcat16@gmail.com 
##########
import sys
import os

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from tools.recaptcha import handle_recaptcha

# Init driver globally
driver = None
# COLUMNS = ['IL', 'ILCE', 'MAHALLE', 'CSBM', 'BINA NO', 'BAGIMSIZ BOLUM']
COLUMNS = ['IL#', 'IL', 'ILCE#', 'ILCE', 'MAHALLE#', 'MAHALLE', 'CSBM#', 'CSBM', 'BINA#', 'BINA NO', 'BB#', 'BAGIMSIZ BOLUM', 'LNG', 'LAT']

def read_last_row_from_csv(file_path = "data/scraped_data.csv"):
    # Reads the last row from the CSV file and returns it as a dictionary.    """
     # Ensure the directory for the file path exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            if not df.empty:
                return df.iloc[-1].to_dict()
            else:
                return None
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return None
    else:
        return None
    
def get_current_map_center():
    # This script gets the current center of the map view
    current_center_script = """
        var map = window.harita.map;
        if (map && map instanceof ol.Map) {
            var view = map.getView();
            var center = view.getCenter();
            // Transform the center coordinates to longitude/latitude
            center = ol.proj.transform(center, view.getProjection(), 'EPSG:4326');
            return center;
        } else {
            return null; // The map object is not found or not initialized yet
        }
    """
    current_center = driver.execute_script(current_center_script)
    
    if current_center:
        print(f"Current Map Center Coordinates: {current_center}")
        return current_center
    else:
        print("Unable to retrieve current map center.")
        return (None, None)

def append_to_csv(data, file_path = 'data/scraped_data.csv' ):
    # A function to append the scraped data into a CSV file.
    
    df = pd.DataFrame(data, columns=COLUMNS )
    
    header = not os.path.isfile(file_path)
    df.to_csv(file_path, mode='a', index=False, header=header)

def init_driver():
    global driver 
    # Setup code for webdriver...
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print('Error initializing WebDriver: ', e)
        sys.exit()

def has_options(driver, select_id):
    try:
        select_element = WebDriverWait(driver, 10).until(
            # EC.presence_of_element_located((By.ID, select_id))
            EC.element_to_be_clickable((By.ID, select_id))
        )
        select_object = Select(select_element)
        options = [option.get_attribute('value') for option in select_object.options if option.get_attribute('value') != '']
        return len(options) > 0
    except TimeoutException:
        return False

    
def main():
    init_driver()
    driver.get("https://adres.nvi.gov.tr/Home")
    
    while True:
        # Read the last scraped data to determine where to resume
        last_scraped_data = read_last_row_from_csv()

        # Variables to keep track of the current scraping position
        start_il = str(int(last_scraped_data[COLUMNS[0]])).strip() if last_scraped_data else None
        start_ilce = str(int(last_scraped_data[COLUMNS[2]])).strip() if last_scraped_data else None
        start_mahalle = str(int(last_scraped_data[COLUMNS[4]])).strip() if last_scraped_data else None
        start_csbm = str(int(last_scraped_data[COLUMNS[6]])).strip() if last_scraped_data else None
        start_diskapi = str(int(last_scraped_data[COLUMNS[8]])).strip() if last_scraped_data else None
        
        print(start_il)
        print(start_ilce)
        print(start_mahalle)
        print(start_csbm)
        print(start_diskapi)
        print('*' * 50 )
    
        try:
            driver.get("https://adres.nvi.gov.tr/VatandasIslemleri/AdresSorgu")
            # Handle reCAPTCHA if needed
            handle_recaptcha(driver)
            
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ilListesi")))
            il_select = Select(driver.find_element(By.ID, 'ilListesi'))
            ils = [(option.get_attribute('value'), option.text.strip()) for option in il_select.options if option.get_attribute('value') != '']

            for il, il_text in ils:
                print(f"1-Processing il: {il}-{il_text}  start_il: {start_il}")
                if start_il and il != start_il:
                    continue  # Skip to the next city if this is not the one to start with
                start_il = None  # Reset start_il after using it
                il_select.select_by_value(il)

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='ilceListesi']/option[@value!='']")))
                ilce_select = Select(driver.find_element(By.ID,'ilceListesi'))
                ilces = [(option.get_attribute('value'), option.text.strip()) for option in ilce_select.options if option.get_attribute('value') != '']
                
                for ilce, ilce_text in ilces:
                    print(f"2-Processing ilce: {ilce}-{ilce_text} in il: {il_text}")
                    if start_ilce and ilce != start_ilce:
                        continue  # Skip to the next district if this is not the one to start with
                    start_ilce = None  # Reset start_ilce after using it
                    ilce_select.select_by_value(ilce)

                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='mahalleKoyBaglisiListesi']/option[@value!='']")))
                    mahalle_select = Select(driver.find_element(By.ID,'mahalleKoyBaglisiListesi'))
                    mahalles = [(option.get_attribute('value'), option.text.strip()) for option in mahalle_select.options if option.get_attribute('value') != '']
                    
                    for mahalle, mahalle_text in mahalles:
                        print(f"3-Processing mahalle:{mahalle}-{mahalle_text} in ilce: {ilce_text}")
                        if start_mahalle and mahalle != start_mahalle:
                            continue  # Skip to the next neighborhood if this is not the one to start with
                        start_mahalle = None  # Reset start_mahalle after using it
                        mahalle_select.select_by_value(mahalle)

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='yolListesi']/option[@value!='']")))
                        csbm_select = Select(driver.find_element(By.ID,'yolListesi'))
                        csbms = [(option.get_attribute('value'), option.text.strip()) for option in csbm_select.options if option.get_attribute('value') != '']
                        
                        for csbm, csbm_text in csbms:
                            print(f"4-Processing csbm: {csbm}-{csbm_text} in mahalle: {mahalle_text}")
                            if start_csbm and csbm != start_csbm:
                                continue  # Skip to the next street if this is not the one to start with
                            start_csbm = None  # Reset start_csbm after using it
                            csbm_select.select_by_value(csbm)
                            
                            scraped_data = []  # Initialize the list to collect data
                                                            
                            if not has_options(driver, 'binaListesi'):
                                print(f"No 'diskapi' options available for csbm {csbm}. Saving data with empty 'BINA NO' and 'BAGIMSIZ BOLUM'.")
                                
                                lng, lat = get_current_map_center()
                                texts = [il, il_text, ilce, ilce_text, mahalle, mahalle_text, csbm, csbm_text, "", "", "", "", lng, lat]
                                data = dict(zip(COLUMNS, texts))
                                scraped_data.append(data)
                            else:
                                diskapi_select = Select(driver.find_element(By.ID, 'binaListesi'))
                                diskapis = [(option.get_attribute('value'), option.text.strip()) for option in diskapi_select.options if option.get_attribute('value') != '']
                                
                                for diskapi, diskapi_text in diskapis:
                                    print(f"5-Processing diskapi: {diskapi}-{diskapi_text} in csbm: {csbm_text}")
                                    if start_diskapi and diskapi != start_diskapi:
                                        continue  # Skip to the next outer door number if this is not the one to start with
                                    start_diskapi = None  # Reset start_diskapi after using it
                                    diskapi_select.select_by_value(diskapi)
                                    
                                    # Extract coordinate 
                                    lng, lat = get_current_map_center()
                                                                                                        
                                    if not has_options(driver, 'bagimsizBolumListesi'):
                                        print(f"No 'ickapi' options available for diskapi {diskapi}. Saving data with empty 'BAGIMSIZ BOLUM'.")
                                        texts = [il, il_text, ilce, ilce_text, mahalle, mahalle_text, csbm, csbm_text, diskapi, diskapi_text, "", "", lng, lat]
                                        data = dict(zip(COLUMNS, texts))
                                        scraped_data.append(data)
                                    else:
                                        ickapi_select = Select(driver.find_element(By.ID,'bagimsizBolumListesi'))
                                        ickapis = [(option.get_attribute('value'), option.text.strip()) for option in ickapi_select.options if option.get_attribute('value') != '']
                                        
                                        for ickapi, ickapi_text in ickapis:
                                            print(f"Processing ickapi: {ickapi}-{ickapi_text} in diskapi: {diskapi_text}")
                                            # Final data collection for this combination of selections
                                            texts = [il, il_text, ilce, ilce_text, mahalle, mahalle_text, csbm, csbm_text, diskapi, diskapi_text, ickapi, ickapi_text, lng, lat]
                                            data = dict(zip(COLUMNS, texts))
                                            scraped_data.append(data)
                                        # Call append_to_csv only if scraped_data is not empty
                                        if scraped_data:
                                            append_to_csv(scraped_data)
                                            scraped_data = []  # Reset scraped_data after appending    
                                # Call append_to_csv only if scraped_data is not empty
                                if scraped_data:
                                    append_to_csv(scraped_data)
                                    scraped_data = []  # Reset scraped_data after appending
                            
        except TimeoutException as e:
            print("Timeout occurred: ", e)
        except NoSuchElementException as e:
            print("Element not found: ", e)
        except Exception as e:
            print("An error occurred: ", e)

        inp = input('Press ENTER to continue or q to exit.')
        if inp.lower() == 'q':
            break

    # Clean up
    driver.quit()

if __name__ == '__main__':
    main()
