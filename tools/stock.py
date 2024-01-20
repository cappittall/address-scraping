
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
read_last_row_from_csv = None

# Init driver globally
driver = None


def save_to_excel(data):
    """
    A function to save the scraped data into an Excel file.
    """
    df = pd.DataFrame(data, columns=['IL SIRA', 'ILCE SIRA', 'MAHALLE SIRA', 'CSBM SIRA', 'BINA NO SIRA'])
    df.to_excel('data/scraped_data.xlsx', index=False)
    
def main():
    global driver
       
    # Setup code for webdriver...
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print('Error initializing WebDriver: ', e)
        sys.exit()
    driver.get("https://adres.nvi.gov.tr/Home")
    
    while True:
        driver.get("https://adres.nvi.gov.tr/VatandasIslemleri/AdresSorgu")
        # Handle reCAPTCHA if needed
        handle_recaptcha(driver)
    
        # Read the last scraped data to determine where to resume
        last_scraped_data = read_last_row_from_csv('data/scraped_data.csv')
        start_il = last_scraped_data['IL SIRA'] if last_scraped_data else None
        start_ilce = last_scraped_data['ILCE SIRA'] if last_scraped_data else None
        start_mahelle = last_scraped_data['MAHALLE SIRA'] if last_scraped_data else None
        start_csbm = last_scraped_data['CSBM SIRA'] if last_scraped_data else None
        start_diskapi = last_scraped_data['BINA NO SIRA'] if last_scraped_data else None
        start_ickapi = last_scraped_data['ICKAPI'] if last_scraped_data else None  # Assuming 'ICKAPI' is the column name for iç kapı

        il_container_xpath = "//span[@id='select2-ilListesi-container']"
        available_ils = select_dropdown_option_select2("ilListesi", il_container_xpath, start_il)
        scraped_data = []

        for il in available_ils:
            if start_il and il != start_il:
                continue
            start_il = None # 
            
            ilce_container_xpath = "//span[@id='select2-ilceListesi-container']"
            selected_ilce = select_dropdown_option_select2("ilceListesi", ilce_container_xpath, start_ilce)
            
            for ilce in selected_ilce:  # Iterate over the selected ilces
                if start_ilce and start_ilce != ilce:
                    continue
                start_ilce = None  # Reset start_ilce after using it
                
                mahalle_container_xpath = "//span[@id='select2-mahalleKoyBaglisiListesi-container']"
                selected_mahalle = select_dropdown_option_select2("mahalleKoyBaglisiListesi", mahalle_container_xpath, start_mahelle)

                for mahalle in selected_mahalle:
                    if start_mahalle and start_mahalle != mahalle:
                        continue
                    start_mahalle = None  # Reset start_mahalle after using it
                    
                    csbm_container_xpath = "//span[@id='select2-yolListesi-container']"
                    selected_csbm = select_dropdown_option_select2("yolListesi", csbm_container_xpath, start_csbm)
                    for csbm in selected_csbm:
                        if start_csbm and start_csbm != csbm:
                            continue
                        start_csbm = None  # Reset start_csbm after using it
                        
                        diskapi_container_xpath = "//span[@id='select2-binaListesi-container']"
                        selected_diskapi = select_dropdown_option_select2("binaListesi", diskapi_container_xpath, start_diskapi)

                        for diskapi in selected_diskapi:
                            if start_diskapi and start_diskapi != diskapi:
                                continue
                            start_diskapi = None  # Reset start_diskapi after using it
                        
                            ickapi_container_xpath = "//span[@id='select2-bagimsizBolumListesi-container']"
                            #previous apps           "//ul[@id='select2-bagimsizBolumListesi-results']//li"
                            selected_ickapi = select_dropdown_option_select2("bagimsizBolumListesi", ickapi_container_xpath, start_ickapi)

                            for ickapi in selected_ickapi:
                                if start_ickapi and start_ickapi != ickapi:
                                    continue
                                start_ickapi = None  # Reset start_ickapi after using it

                                # Final data collection
                                data = {
                                    "il": il,
                                    "ilce": ilce,
                                    "mahalle": mahalle,
                                    "csbm": csbm,
                                    "diskapi": diskapi,
                                    "ickapi": ickapi,
                                    # ... [Other fields if any]
                                }
                                scraped_data.append(data)
                                    
                        # Append the collected data to the CSV file
                        # append_to_csv([data], 'data/scraped_data.csv')
        inp = input('Çıkmak için q tuşuna.Tekrar denemek için ENTER tuşuna basınız')
        if inp == 'q': break
        else:
            continue
    
    # Clean up
    driver.quit()

if __name__ == '__main__':
    main()
    
    
    



def select_dropdown_option_select2(dropdown_id, dropdown_container_xpath, option_text=None, max_trials=5):
    print("Option text: ", option_text)
    trial = 0  # Initialize trial counter

    while trial < max_trials:
        try:
            container_element = driver.find_element(By.XPATH, dropdown_container_xpath)
            container_element.click()
            wait = WebDriverWait(driver, 4)
            # Wait until the element is clickable
            wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")))
            
            # If option_text is provided, select the matching option
            if option_text:
                options_list = driver.find_elements(By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")
                for option in options_list:
                    if option.text == option_text:
                        try:
                            option.click()
                            print(f"Option '{option_text}' selected.")
                            return True  # Successfully selected the option
                        except:
                            # If click fails, use JavaScript to set the value
                            value_to_select = option.get_attribute("id")
                            driver.execute_script(f"$('#{dropdown_id}').val('{value_to_select}').trigger('change');")
                            print(f"Option '{option_text}' selected via JS.")
                            return True  # Successfully selected the option via JS
            else:
                # If no specific option is provided, click the first available option
                first_option = driver.find_element(By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")
                first_option.click()
                print("First option selected.")
                return True  # Successfully selected the first option

        except NoSuchElementException:
            print(f"Dropdown with id {dropdown_id} not found.")
        except TimeoutException:
            print(f"Timeout waiting for options to be clickable in dropdown with id {dropdown_id}.")
        except Exception as e:
            print(f"Error selecting option from dropdown: {e}")
        
        trial += 1  # Increment the trial counter
        print(f"Retrying... Attempt {trial}/{max_trials}")

    # If the code reaches this point, it means the selection wasn't successful after the max trials
    print(f"Failed to select an option after {max_trials} attempts.")
    return False

     
def extract_list_by_xpath_(xpath):
    # Generic function to extract lists from dropdowns using XPaths.
    try:
        element = driver.find_element(By.XPATH, xpath)
        element.click()
        wait = WebDriverWait(driver, 20)  # Increased wait time
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")))
        items = driver.find_elements(By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")
        return [item.text for item in items]
    except TimeoutException:
        print(f"HATA: Timeout :{xpath}.")
        return []
    except NoSuchElementException:
        print(f"HATA: Element with XPath {xpath} not found.")
        return []
    except Exception as e:
        print(f"Unexpected error when extracting list by XPath {xpath}: {e}")
        return []

def extract_list_by_xpath(dropdown_id):
    try:
        # Wait up to 20 seconds for the dropdown to be present
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, dropdown_id)))
        
        # Find the dropdown element by its ID
        dropdown = driver.find_element(By.ID, dropdown_id)
        
        # Wait up to 20 seconds for the options of the dropdown to be loaded
        WebDriverWait(driver, 20).until(lambda driver: len(Select(dropdown).options) > 1)
        
        # Create a Select object based on the found dropdown for easier interaction
        select = Select(dropdown)
        
        # Extract the options from the dropdown
        options = select.options
        
        # Extract the text for each option and return it as a list
        options_list = [option.text for option in options if option.text.strip() != ""]
        return options_list
    
    except NoSuchElementException:
        print(f"Dropdown with id {dropdown_id} not found.")
        return []
    except TimeoutException:
        print(f"Timeout waiting for dropdown with id {dropdown_id} or its options to load.")
        return []
    except Exception as e:
        print(f"Unexpected error when extracting list by dropdown id {dropdown_id}: {e}")
        return []

"//span[@id='select2-ilListesi-container']"
"//span[@id='select2-ilceListesi-container']"
"//span[@id='select2-mahalleKoyBaglisiListesi-container']"
"//span[@id='select2-yolListesi-container']"
"//span[@id='select2-binaListesi-container']"
"//span[@id='select2-bagimsizBolumListesi-container']"
 
 
 
"""
 
                                print(f"Processing diskapi: {diskapi} in csbm: {csbm}")
                                if start_diskapi and diskapi != start_diskapi:
                                    continue  # Skip to the next outer door number if this is not the one to start with
                                start_diskapi = None  # Reset start_diskapi after using it
                                diskapi_select.select_by_value(diskapi)
                                
                                try:
                                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='bagimsizBolumListesi']/option[@value!='']")))
                                except TimeoutException:
                                    print(f"No 'ickapi' options available for diskapi {diskapi}. Moving to the next 'diskapi'.")
                                    continue
                                
                                if not has_options(driver, 'bagimsizBolumListesi'):
                                    print(f"No 'ickapi' options available for diskapi {diskapi}. Moving to the next 'diskapi'.")
                                    continue
                                
                                ickapi_select = Select(driver.find_element(By.ID,'bagimsizBolumListesi'))
                                ickapis = [option.get_attribute('value') for option in ickapi_select.options if option.get_attribute('value') != '']
                               
                                scraped_data = []
                                # Extract the visible text for each selected option
                                selected_il_text = il_select.first_selected_option.text.strip()
                                selected_ilce_text = ilce_select.first_selected_option.text.strip()
                                selected_mahalle_text = mahalle_select.first_selected_option.text.strip()
                                selected_csbm_text = csbm_select.first_selected_option.text.strip()
                                selected_diskapi_text = diskapi_select.first_selected_option.text.strip()
                                data = {
                                        'IL': selected_il_text,
                                        'ILCE': selected_ilce_text,
                                        'MAHALLE': selected_mahalle_text,
                                        'CSBM': selected_csbm_text,
                                        'BINA NO': selected_diskapi_text,
                                        'BAGIMSIZ BOLUM': ""
                                    }
                                scraped_data.append(data)
                                for ickapi in ickapis:
                                    # Select each ickapi before reading its text
                                    ickapi_select.select_by_value(ickapi)
                                    selected_ickapi_text = ickapi_select.first_selected_option.text.strip()
                                    
                                    # Final data collection for this combination of selections
                                    data = {
                                        'IL': selected_il_text,
                                        'ILCE': selected_ilce_text,
                                        'MAHALLE': selected_mahalle_text,
                                        'CSBM': selected_csbm_text,
                                        'BINA NO': selected_diskapi_text,
                                        'BAGIMSIZ BOLUM': selected_ickapi_text
                                    }
                                    scraped_data.append(data)
                                append_to_csv(scraped_data, 'data/scraped_data.csv')  # Append the collected data to the CSV file
                                """