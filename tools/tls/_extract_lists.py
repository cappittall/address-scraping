import sys
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as O
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = None

def extract_il_list():

    iller_listesi = []
    il_secme_elementi = driver.find_element(By.XPATH, "//span[@id='select2-ilListesi-container']")
    il_secme_elementi.click()
    wait = WebDriverWait(driver, 4)
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")))
   
    acilan_iller = driver.find_elements(By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")

    # Açılan illeri listeleyin
    for il in acilan_iller:
        il_metni = il.text
        iller_listesi.append([il_metni])
    return iller_listesi

def extract_ilce_list():
    # Extracting ilce lists 
    ilceler_listesi = []
    ilce_secme_elementi = driver.find_element(By.XPATH, "//span[@id='select2-ilceListesi-container']")
    ilce_secme_elementi.click()

    wait = WebDriverWait(driver, 4)
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")))

    # Açılan ilçeleri alın
    acilan_ilceler = driver.find_elements(By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")

    # Açılan ilçeleri listeleyin
    for ilce in acilan_ilceler:
        ilce_metni = ilce.text
        ilceler_listesi.append(ilce_metni)
    return ilceler_listesi

def extract_mahalle_list():
    
    # Mahalleler saklamak için bir liste oluşturun
    mahalleler_listesi = []
    mahalle_secme_elementi = driver.find_element(By.XPATH,
                             "//span[@id='select2-mahalleKoyBaglisiListesi-container']")
    mahalle_secme_elementi.click()
    wait = WebDriverWait(driver, 4)  # Dinamik içerik için daha uzun bir süre belirledim.
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='select2-results__options']//li")))

    # Açılan mahalleleri alın
    acilan_mahalleler = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']//li")

    # Açılan mahalleleri listeleyin
    for mahalle in acilan_mahalleler:
        mahalle_metni = mahalle.text
        mahalleler_listesi.append([mahalle_metni])

    # Açılan mahalleleri düz bir liste olarak oluşturun
    mahalleler_listesi = [mahalle.text for mahalle in acilan_mahalleler]
    
    return mahalleler_listesi

def extract_csbm_list():
    
    csbm_listesi = []

    # CSBM listesi 
    csbm_secme_elementi = driver.find_element(By.XPATH, "//span[@id='select2-yolListesi-container']")
    csbm_secme_elementi.click()
    wait = WebDriverWait(driver, 4)
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='select2-results__options']//li")))

    # Açılan CSBM'leri alın
    acilan_csbm = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']//li")

    # Açılan CSBM'leri listeleyin
    for csbm in acilan_csbm:
        csbm_metni = csbm.text
        csbm_listesi.append(csbm_metni)
    return csbm_listesi

def extract_diskapi_lists():
    # Dış kapılar (binalar) saklamak için bir liste oluşturun
    dis_kapi_listesi = []

    # Dış kapı seçme elementini bulun
    dis_kapi_secme_elementi = driver.find_element(
        By.XPATH, "//span[@id='select2-binaListesi-container']")

    dis_kapi_secme_elementi.click()

    # Açılan dış kapı seçeneklerinin yüklenmesini bekleyin
    wait = WebDriverWait(driver, 4)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//ul[@class='select2-results__options']//li")))

    # Açılan dış kapıları alın
    acilan_dis_kapilar = driver.find_elements(
        By.XPATH, "//ul[@class='select2-results__options']//li")

    # Açılan dış kapıları listeleyin
    for dis_kapi in acilan_dis_kapilar:
        dis_kapi_metni = dis_kapi.text
        dis_kapi_listesi.append(dis_kapi_metni)
    return dis_kapi_listesi

def extract_ickapi_lists():
    ic_kapi_listesi = []
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((
        By.XPATH, "//ul[@id='select2-bagimsizBolumListesi-results']//li")))
    acilan_ic_kapilar = driver.find_elements(
        By.XPATH, "//ul[@id='select2-bagimsizBolumListesi-results']//li")
    
    # Açılan iç kapıları listeleyin ve sayısını hesaplayın
    for ic_kapi in acilan_ic_kapilar:
        ic_kapi_metni = ic_kapi.text
        ic_kapi_listesi.append(ic_kapi_metni)
    return ic_kapi_listesi
 


       
def select_dropdown_option(dropdown_id):
    """
    A function to select an option from a dropdown and return all available options.
    """
    try:
        dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, dropdown_id)))
        dropdown.click() # Click the dropdown
        # Wait for the dropdown options to be visible
        options_list = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, f"//ul[@aria-labelledby='{dropdown_id}']//li")))
        
        # Extract the text for each option
        options_text = [option.text for option in options_list]

        # Clicking an option would be something like:
        # options_list[0].click() # to click the first option

        return options_text
    except NoSuchElementException:
        print(f"Dropdown with id {dropdown_id} not found.")
        return []