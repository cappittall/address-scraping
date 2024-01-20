from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd 
from pathlib import Path


def il_save_to_excel(file_name, il):
    df = pd.DataFrame(il, columns=['IL'])
    df.to_excel(file_name, index=False)
    
def ilceler_save_to_excel(file_name, il_adi, ilce):
    df = pd.DataFrame(ilce, columns=['ILCE'])
    df.insert(0, 'IL', il_adi)
    df.to_excel(file_name, index=False)
    
def mahalleler_save_to_excel(file_name, il_adi, ilce, mahalle):
    df = pd.DataFrame(mahalle, columns=['MAHALLE'])
    df.insert(0, 'ILCE', ilce)
    df.insert(0, 'IL', il_adi)
    df.to_excel(file_name, index=False)
    
def csbm_save_to_excel(file_name, il_adi, ilce_adi, mahalle_adi, csbm_listesi):
    df = pd.DataFrame(csbm_listesi, columns=['CSBM'])
    df.insert(0, 'MAHALLE', mahalle_adi)
    df.insert(0, 'ILCE', ilce_adi)
    df.insert(0, 'IL', il_adi)
    df.to_excel(file_name, index=False)
    
def dis_kapi_save_to_excel(file_name, il_adi, ilce_adi, mahalle_adi, csbm_adi, dis_kapi_listesi):
    # DataFrame oluştur
    df = pd.DataFrame(dis_kapi_listesi, columns=['BINA NO'])
    # Diğer bilgileri DataFrame'e ekle
    df.insert(0, 'CSBM', csbm_adi)
    df.insert(0, 'MAHALLE', mahalle_adi)
    df.insert(0, 'ILCE', ilce_adi)
    df.insert(0, 'IL', il_adi)
    # DataFrame'i Excel dosyasına kaydet
    df.to_excel(file_name, index=False)
    
def dis_kapi_ve_ic_kapi_save_to_excel(file_name, il_adi, ilce_adi, mahalle_adi, csbm_adi, dis_kapi_listesi, secilen_dis_kapi_numarasi, ic_kapi_sayisi):
    # Dosya yolu kontrolü
    file_path = Path(file_name)
    if file_path.is_file():
        # Dosya varsa, verileri oku
        existing_df = pd.read_excel(file_name)
    else:
        # Dosya yoksa, gerekli sütunlarla boş bir DataFrame oluştur
        existing_df = pd.DataFrame(columns=['IL', 'ILCE', 'MAHALLE', 'CSBM', 'BINA NO', 'HOMEPASS'])

    # Yeni veri eklemek için boş bir liste oluştur
    new_data = []
    for bina_no in dis_kapi_listesi:
        # Mevcut DataFrame içinde bina_no yoksa veya varsa ve HOMEPASS değeri boşsa, yeni veriyi ekle
        if not (existing_df[(existing_df['IL'] == il_adi) &
                            (existing_df['ILCE'] == ilce_adi) &
                            (existing_df['MAHALLE'] == mahalle_adi) &
                            (existing_df['CSBM'] == csbm_adi) &
                            (existing_df['BINA NO'] == bina_no)].any(axis=None)):
            homepass_value = ic_kapi_sayisi  # HOMEPASS sayısal değeri her zaman kullanılıyor
            new_data.append({
                'IL': il_adi,
                'ILCE': ilce_adi,
                'MAHALLE': mahalle_adi,
                'CSBM': csbm_adi,
                'BINA NO': bina_no,
                'HOMEPASS': homepass_value
            })

    # Yeni veri varsa, DataFrame oluştur ve kaydet
    if new_data:
        new_df = pd.DataFrame(new_data)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df.drop_duplicates(subset=['IL', 'ILCE', 'MAHALLE', 'CSBM', 'BINA NO'], keep='last', inplace=True)
        # Birleştirilmiş DataFrame'i Excel dosyasına kaydet
        combined_df.to_excel(file_name, index=False)
    else:
        pass
    
def il_kaydet(driver):

    # Açılan iller saklamak için bir liste oluşturun
    iller_listesi = []

    # İl seçme dropdown elementini XPath kullanarak bulun
    il_secme_elementi = driver.find_element(By.XPATH, "//span[@id='select2-ilListesi-container']")


    # İl seçme dropdown'ına tıklayın
    il_secme_elementi.click()


    # Açılan iller listesinin yüklenmesini bekleyin
    # XPath ile açılan listeyi bekleyecek şekilde güncellendi
    wait = WebDriverWait(driver, 4)
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")))

    # Açılan illeri alın
    # XPath kullanarak açılan illeri seçecek şekilde güncellendi
    acilan_iller = driver.find_elements(By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")

    # Açılan illeri listeleyin
    for il in acilan_iller:
        il_metni = il.text
        iller_listesi.append([il_metni])

    # İller listesini CSV dosyasına kaydet
    il_save_to_excel('IL.xlsx', iller_listesi)

def ilce_kaydet(driver, secilen_il_adi):
    # Açılan ilçeler saklamak için bir liste oluşturun

    ilceler_listesi = []

    # İlçe seçme dropdown elementini XPath kullanarak bulun
    ilce_secme_elementi = driver.find_element(By.XPATH, "//span[@id='select2-ilceListesi-container']")


    # İlçe seçme dropdown'ına tıklayın
    ilce_secme_elementi.click()


    # Açılan ilçeler listesinin yüklenmesini bekleyin
    wait = WebDriverWait(driver, 4)
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")))

    # Açılan ilçeleri alın
    acilan_ilceler = driver.find_elements(By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")

    # Açılan ilçeleri listeleyin
    for ilce in acilan_ilceler:
        ilce_metni = ilce.text
        ilceler_listesi.append(ilce_metni)

    # İlçeler listesini Excel dosyasına kaydet
    ilceler_save_to_excel('IL_ILCE.xlsx', secilen_il_adi.upper(), ilceler_listesi)

def mahalle_kaydet(driver, secilen_il_adi, secilen_ilce_adi):

    # Mahalleler saklamak için bir liste oluşturun
    mahalleler_listesi = []

    # Verilen HTML örneğine göre id kullanarak XPath güncellendi
    mahalle_secme_elementi = driver.find_element(By.XPATH,
                                                 "//span[@id='select2-mahalleKoyBaglisiListesi-container']")


    # Mahalle seçme elementine tıklayın
    mahalle_secme_elementi.click()


    # Açılan mahalle seçeneklerinin yüklenmesini bekleyin
    # Bu bekleme süresi, mahallelerin listelenmesi için gerekli olan dinamik yüklenme süresine göre değişiklik gösterebilir.
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

    mahalleler_save_to_excel(file_name='IL_ILCE_MAHALLE.xlsx',il_adi=secilen_il_adi.upper(),ilce=secilen_ilce_adi.upper(),mahalle=mahalleler_listesi)

def sokak_kaydet(driver, secilen_il_adi, secilen_ilce_adi, secilen_mahalle_adi):
    # CSBM'ler (Cadde/Sokak/Bulvar/Meydan) saklamak için bir liste oluşturun
    csbm_listesi = []

    # CSBM seçme elementini bulun
    csbm_secme_elementi = driver.find_element(By.XPATH, "//span[@id='select2-yolListesi-container']")


    # CSBM seçme elementine tıklayın
    csbm_secme_elementi.click()

    # Açılan CSBM seçeneklerinin yüklenmesini bekleyin
    wait = WebDriverWait(driver, 4)
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='select2-results__options']//li")))

    # Açılan CSBM'leri alın
    acilan_csbm = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']//li")

    # Açılan CSBM'leri listeleyin
    for csbm in acilan_csbm:
        csbm_metni = csbm.text
        csbm_listesi.append(csbm_metni)

    # CSBM'leri CSV dosyasına kaydedin
    csbm_save_to_excel(
        file_name='IL_ILCE_MAHALLE_CSBM.xlsx',
        il_adi=secilen_il_adi.upper(),
        ilce_adi=secilen_ilce_adi.upper(),
        mahalle_adi=secilen_mahalle_adi.upper(),
        csbm_listesi=csbm_listesi
    )

def bina_kaydet(driver, secilen_il_adi, secilen_ilce_adi, secilen_mahalle_adi, secilen_csbm_adi ):

    # Dış kapılar (binalar) saklamak için bir liste oluşturun
    dis_kapi_listesi = []

    # Dış kapı seçme elementini bulun
    dis_kapi_secme_elementi = driver.find_element(By.XPATH,
                                                  "//span[@id='select2-binaListesi-container']")


    # Dış kapı seçme elementine tıklayın
    dis_kapi_secme_elementi.click()


    # Açılan dış kapı seçeneklerinin yüklenmesini bekleyin
    wait = WebDriverWait(driver, 4)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//ul[@class='select2-results__options']//li")))

    # Açılan dış kapıları alın
    acilan_dis_kapilar = driver.find_elements(By.XPATH,
                                              "//ul[@class='select2-results__options']//li")

    # Açılan dış kapıları listeleyin
    for dis_kapi in acilan_dis_kapilar:
        dis_kapi_metni = dis_kapi.text
        dis_kapi_listesi.append(dis_kapi_metni)
    print('2-', dis_kapi_listesi)
    # Dış kapıları CSV dosyasına kaydedin
    dis_kapi_save_to_excel(
        file_name='IL_ILCE_MAHALLE_CSBM_BINA_NO.xlsx',
        il_adi=secilen_il_adi.upper(),
        ilce_adi=secilen_ilce_adi.upper(),
        mahalle_adi=secilen_mahalle_adi.upper(),
        csbm_adi=secilen_csbm_adi.upper(),
        dis_kapi_listesi=dis_kapi_listesi
    )
    return dis_kapi_listesi
