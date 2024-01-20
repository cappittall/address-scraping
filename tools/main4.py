
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as O
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


from tools.tls._dosya_olusturma import *
from tools.tls._sira_ekleme import *
from tools.tls._alan_secim import *
from tools.tls._kayit_et import * 



def process_il(driver,secilen_il,secilen_il_adi):
    while True:
        try:
            # Eğer kullanıcının girdiği il adına uygun bir seçenek bulunduysa, il adını web sayfasında seç
            if not secilen_il.empty:
                # Web sayfasında il adını ara ve tıkla
                acilan_iller = driver.find_elements(By.XPATH, "//ul[contains(@class, 'select2-results__options')]//li")
                for il in acilan_iller:
                    if secilen_il_adi.lower() in il.text.lower():
                        il.click()
                        print(f"{secilen_il_adi.upper()} seçildi.")

                        # Excel dosyasını oku
                        dosya_adi = 'SIRA.xlsx'
                        df = pd.read_excel(dosya_adi)
                        if df.empty or df['IL SIRA'].isna().all():
                            # Eğer DataFrame boşsa veya 'IL SIRA' sütunu tamamen NaN ise
                            df.loc[0, 'IL SIRA'] = secilen_il_adi
                        else:
                            # Eğer DataFrame boş değilse, ilk boş hücreye veriyi ekle
                            ilk_bos_index = df['IL SIRA'].isna().idxmax()
                            df.at[ilk_bos_index, 'IL SIRA'] = secilen_il_adi

                        # Değişiklikleri aynı dosyaya kaydet
                        df.to_excel(dosya_adi, index=False)
                        break
        except Exception as e:
            print(f"İl Seçiminde bir sorun çıktı: {e}. Yeniden deniyorum.")
            continue
        break
def process_ilce(driver, secilen_ilce,secilen_ilce_adi ):
    while True:
        try:
            # Eğer kullanıcının girdiği ilce adına uygun bir seçenek bulunduysa, ilce adını web sayfasında seç
            if not secilen_ilce.empty:
                # Web sayfasında ilce adını ara ve tıkla
                acilan_ilceler = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']//li")
                for ilce in acilan_ilceler:
                    if secilen_ilce_adi.lower() in ilce.text.lower():
                        ilce.click()
                        print(f"{secilen_ilce_adi.upper()} seçildi.")

                        # Excel dosyasını oku
                        dosya_adi = 'SIRA.xlsx'
                        df = pd.read_excel(dosya_adi)
                        if df.empty or df['ILCE SIRA'].isna().all():
                            # Eğer DataFrame boşsa veya 'IL SIRA' sütunu tamamen NaN ise
                            df.loc[0, 'ILCE SIRA'] = secilen_ilce_adi
                        else:
                            # Eğer DataFrame boş değilse, ilk boş hücreye veriyi ekle
                            ilk_bos_index = df['ILCE SIRA'].isna().idxmax()
                            df.at[ilk_bos_index, 'ILCE SIRA'] = secilen_ilce_adi

                        # Değişiklikleri aynı dosyaya kaydet
                        df.to_excel(dosya_adi, index=False)
                        break
        except Exception as e:
            print(f"İlçe Seçiminde bir sorun çıktı: {e}. Yeniden deniyorum.")
            continue
        break
def process_mahalle(driver, secilen_mahalle, secilen_mahalle_adi):
    while True:
        try:
            # Eğer kullanıcının girdiği Mahalle adına uygun bir seçenek bulunduysa, Mahalle adını web sayfasında seç
            if not secilen_mahalle.empty:
                # Web sayfasında Mahalle adını ara ve tıkla
                acilan_mahalleler = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']//li")
                for mahalle in acilan_mahalleler:
                    if secilen_mahalle_adi.lower() in mahalle.text.lower():
                        mahalle.click()
                        print(f"{secilen_mahalle_adi.upper()} seçildi.")

                        # Excel dosyasını oku
                        dosya_adi = 'SIRA.xlsx'
                        df = pd.read_excel(dosya_adi)
                        if df.empty or df['MAHALLE SIRA'].isna().all():
                            # Eğer DataFrame boşsa veya 'IL SIRA' sütunu tamamen NaN ise
                            df.loc[0, 'MAHALLE SIRA'] = secilen_mahalle_adi
                        else:
                            # Eğer DataFrame boş değilse, ilk boş hücreye veriyi ekle
                            ilk_bos_index = df['MAHALLE SIRA'].isna().idxmax()
                            df.at[ilk_bos_index, 'MAHALLE SIRA'] = secilen_mahalle_adi

                        # Değişiklikleri aynı dosyaya kaydet
                        df.to_excel(dosya_adi, index=False)
                        break
        except Exception as e:
            print(f"Mahalle Seçiminde bir sorun çıktı: {e}. Yeniden deniyorum.")
            continue
        break
def process_sokak(driver, secilen_csbm, secilen_csbm_adi):
    while True:
        try:
            # Eğer kullanıcının girdiği CBSM adına uygun bir seçenek bulunduysa, CBSM adını web sayfasında seç
            if not secilen_csbm.empty:
                # Web sayfasında CBSM adını ara ve tıkla
                acilan_csbm = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']//li")
                for cbsm in acilan_csbm:
                    if secilen_csbm_adi.lower() in cbsm.text.lower():
                        cbsm.click()
                        print(f"{secilen_csbm_adi.upper()} seçildi.")

                        # Excel dosyasını oku
                        dosya_adi = 'SIRA.xlsx'
                        df = pd.read_excel(dosya_adi)
                        if df.empty or df['CSBM SIRA'].isna().all():
                            # Eğer DataFrame boşsa veya 'IL SIRA' sütunu tamamen NaN ise
                            df.loc[0, 'CSBM SIRA'] = secilen_csbm_adi
                        else:
                            # Eğer DataFrame boş değilse, ilk boş hücreye veriyi ekle
                            ilk_bos_index = df['CSBM SIRA'].isna().idxmax()
                            df.at[ilk_bos_index, 'CSBM SIRA'] = secilen_csbm_adi

                        # Değişiklikleri aynı dosyaya kaydet
                        df.to_excel(dosya_adi, index=False)
                        break
        except Exception as e:
            print(f"CBSM Seçiminde bir sorun çıktı: {e}. Yeniden deniyorum.")
            continue
        break
def process_bina(driver, secilen_bina, secilen_bina_adi):
    while True:
        try:
            # Eğer kullanıcının girdiği BINA adına uygun bir seçenek bulunduysa, BINA adını web sayfasında seç
            if not secilen_bina.empty:
                # Web sayfasında CBSM adını ara ve tıkla
                acilan_bina = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']//li")
                for bina in acilan_bina:
                    if secilen_bina_adi.lower() in bina.text.lower():
                        bina.click()
                        print(f"{secilen_bina_adi.upper()} seçildi.")

                        # Excel dosyasını oku
                        dosya_adi = 'SIRA.xlsx'
                        df = pd.read_excel(dosya_adi)
                        if df.empty or df['BINA NO SIRA'].isna().all():
                            # Eğer DataFrame boşsa veya 'IL SIRA' sütunu tamamen NaN ise
                            df.loc[0, 'BINA NO SIRA'] = secilen_bina_adi
                        else:
                            # Eğer DataFrame boş değilse, ilk boş hücreye veriyi ekle
                            ilk_bos_index = df['BINA NO SIRA'].isna().idxmax()
                            df.at[ilk_bos_index, 'BINA NO SIRA'] = secilen_bina_adi

                        # Değişiklikleri aynı dosyaya kaydet
                        df.to_excel(dosya_adi, index=False)
                        break

        except Exception as e:
            print(f"BINA Seçiminde bir sorun çıktı: {e}. Yeniden deniyorum.")
            continue
        break
    
def process_homepass(driver, secilen_il_adi, secilen_ilce_adi, secilen_mahalle_adi, secilen_csbm_adi,dis_kapi_listesi,secilen_bina_adi):
    while True:
        try:
            time.sleep(3)
            print("1")
            # Elementi bul
            element = driver.find_element(By.NAME, "bagimsizBolumKayitNo")
            # JavaScript ile zorla tıklama
            driver.execute_script("arguments[0].click();", element)

            print("2")
            try:
                ic_kapi_listesi = []
                # Açılan iç kapıları alın
                # Açılan iç kapı seçeneklerinin yüklenmesini bekleyin
                wait = WebDriverWait(driver, 5)
                wait.until(EC.presence_of_element_located((By.XPATH,
                                                           "//ul[@id='select2-bagimsizBolumListesi-results']//li")))
                print("3")
                # Açılan iç kapıları alın
                acilan_ic_kapilar = driver.find_elements(By.XPATH,
                                                         "//ul[@id='select2-bagimsizBolumListesi-results']//li")
                print("4")
                # Açılan iç kapıları listeleyin ve sayısını hesaplayın
                for ic_kapi in acilan_ic_kapilar:
                    ic_kapi_metni = ic_kapi.text
                    ic_kapi_listesi.append(ic_kapi_metni)
                    print(ic_kapi_listesi)
                ic_kapi_sayisi = len(ic_kapi_listesi)

                # İç kapıları ve diğer bilgileri bir Excel dosyasına kaydedin
                # Fonksiyon çağrısı
                dis_kapi_ve_ic_kapi_save_to_excel(
                    file_name='IL_ILCE_MAHALLE_CSBM_BINA_NO_HOMEPASS.xlsx',
                    il_adi=secilen_il_adi.upper(),
                    ilce_adi=secilen_ilce_adi.upper(),
                    mahalle_adi=secilen_mahalle_adi.upper(),
                    csbm_adi=secilen_csbm_adi.upper(),
                    dis_kapi_listesi=dis_kapi_listesi,
                    secilen_dis_kapi_numarasi=secilen_bina_adi,
                    ic_kapi_sayisi=ic_kapi_sayisi)
                print(f"Toplam {ic_kapi_sayisi} adet (Homepass) bulundu.")
                break

                # İç kapıların sayısını yazdırın
            except:
                ic_kapi_sayisi = 1
                # İç kapıları ve diğer bilgileri bir Excel dosyasına kaydedin
                # Fonksiyon çağrısı
                dis_kapi_ve_ic_kapi_save_to_excel(
                    file_name='IL_ILCE_MAHALLE_CSBM_BINA_NO_HOMEPASS.xlsx',
                    il_adi=secilen_il_adi.upper(),
                    ilce_adi=secilen_ilce_adi.upper(),
                    mahalle_adi=secilen_mahalle_adi.upper(),
                    csbm_adi=secilen_csbm_adi.upper(),
                    dis_kapi_listesi=dis_kapi_listesi,
                    secilen_dis_kapi_numarasi=secilen_bina_adi,
                    ic_kapi_sayisi=ic_kapi_sayisi)
                print(f"Toplam {ic_kapi_sayisi} adet (Homepass) bulundu.")
                break

        except Exception as e:
            print(
                f"HOMEPASS Seçiminde bir sorun çıktı: {e}. Yeniden deniyorum.")
            continue




def bina_islemi_tamamlandi_mi(bina_df, sira_dosyasi):
    # SIRA.xlsx dosyasından son BINA NO SIRA değerini al
    son_bina_no_sira = pd.read_excel(sira_dosyasi)['BINA NO SIRA'].iloc[-1].lower()

    # IL_ILCE_MAHALLE_CSBM_BINA_NO.xlsx dosyasından son BINA NO değerini al
    son_bina_no = bina_df['BINA NO'].iloc[-1].lower()

    # İki değeri karşılaştır ve sonuç döndür
    return son_bina_no_sira == son_bina_no

def sokak_islemi_tamamlandi_mi(csbm_df, sira_dosyasi):
    # SIRA.xlsx dosyasından son CBSM SIRA değerini al
    son_csbm_sira = pd.read_excel(sira_dosyasi)['CSBM SIRA'].iloc[-1].lower()

    # IL_ILCE_MAHALLE_CSBM.xlsx dosyasından son CBSM değerini al
    son_csbm = csbm_df['CSBM'].iloc[-1].lower()

    # İki değeri karşılaştır ve sonuç döndür
    return son_csbm_sira == son_csbm

def mahalle_islemi_tamamlandi_mi(mahalle_df, sira_dosyasi):
    # SIRA.xlsx dosyasından son MAHALLE SIRA değerini al
    son_mahalle_sira = pd.read_excel(sira_dosyasi)['MAHALLE SIRA'].iloc[-1].lower()

    # IL_ILCE_MAHALLE_CSBM.xlsx dosyasından son MAHALLE değerini al
    son_mahalle = mahalle_df['MAHALLE'].iloc[-1].lower()

    # İki değeri karşılaştır ve sonuç döndür
    return son_mahalle_sira == son_mahalle

def ilce_islemi_tamamlandi_mi(ilce_df, sira_dosyasi):
    # SIRA.xlsx dosyasından son ILCE SIRA değerini al
    son_ilce_sira = pd.read_excel(sira_dosyasi)['ILCE SIRA'].iloc[-1].lower()

    # IL_ILCE_MAHALLE_CSBM.xlsx dosyasından son MAHALLE değerini al
    son_ilce = ilce_df['ILCE'].iloc[-1].lower()

    # İki değeri karşılaştır ve sonuç döndür
    return son_ilce_sira == son_ilce

def il_islemi_tamamlandi_mi(il_df, sira_dosyasi):
    # SIRA.xlsx dosyasından son IL SIRA değerini al
    son_il_sira = pd.read_excel(sira_dosyasi)['IL SIRA'].iloc[-1].lower()

    # IL_ILCE_MAHALLE_CSBM.xlsx dosyasından son MAHALLE değerini al
    son_il = il_df['IL'].iloc[-1].lower()

    # İki değeri karşılaştır ve sonuç döndür
    return son_il_sira == son_il

def bir_sonraki_tum_bul():
    # SIRA.xlsx dosyasını yükle
    sira_df = pd.read_excel('SIRA.xlsx')

    # SIRA.xlsx dosyasının son satırından mevcut ILCE'yi al
    if not sira_df.empty:
        mevcut_il = sira_df.iloc[-1]['IL SIRA']
    else:
        return "SIRA.xlsx dosyası boş."

    # IL_ILCE_MAHALLE.xlsx dosyasını yükle
    il_df = pd.read_excel('IL.xlsx')

    # Mevcut CSBM'nin indeksini bul
    try:
        mevcut_index = il_df[il_df['ILCE'] == mevcut_il].index[0]
    except IndexError:
        # Mevcut CSBM bulunamazsa, hata mesajı döndür
        return "Mevcut ILCE, IL.xlsx dosyasında bulunamadı."

    # Bir sonraki ILCE'nin indeksini kontrol et
    if mevcut_index + 1 < len(il_df):
        # Bir sonraki ıl'yi döndür
        return il_df.loc[mevcut_index + 1, 'IL']
    else:
        # Eğer bir sonraki IL yoksa, None döndür
        return None
def bir_sonraki_tum_guncelle():
    # Bir sonraki IL'yi bul
    bir_sonraki_il = bir_sonraki_il_bul()

    if bir_sonraki_il is None:
        print("Bir sonraki İl bulunamadı veya SIRA.xlsx dosyası boş.")
        return
    elif isinstance(bir_sonraki_il, str) and bir_sonraki_il.startswith("Bir sonraki İl bulunamadı."):
        print(bir_sonraki_il)  # Hata mesajını yazdır
        return

    # SIRA.xlsx dosyasını oku
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        if not sira_df.empty:

            # 'IL' sütunundaki tüm değerleri sil
            sira_df['IL SIRA'] = pd.NA
            # 'ILCE' sütunundaki tüm değerleri sil
            sira_df['ILCE SIRA'] = pd.NA
            # 'MAHALLE' sütunundaki tüm değerleri sil
            sira_df['MAHALLE SIRA'] = pd.NA
            # 'CSBM' sütunundaki tüm değerleri sil
            sira_df['CSBM SIRA'] = pd.NA
            # 'BINA NO SIRA' sütunundaki tüm değerleri sil
            sira_df['BINA NO SIRA'] = pd.NA
            # Değişiklikleri kaydet
            sira_df.to_excel('SIRA.xlsx', index=False)
            print(f"'IL SIRA' sütunu '{bir_sonraki_il}' ile güncellendi.")
        else:
            print("SIRA.xlsx dosyası boş.")
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")

def bir_sonraki_il_bul():
    # SIRA.xlsx dosyasını yükle
    sira_df = pd.read_excel('SIRA.xlsx')

    # SIRA.xlsx dosyasının son satırından mevcut ILCE'yi al
    if not sira_df.empty:
        mevcut_il = sira_df.iloc[-1]['IL SIRA']
    else:
        return "SIRA.xlsx dosyası boş."

    # IL_ILCE_MAHALLE.xlsx dosyasını yükle
    il_df = pd.read_excel('IL.xlsx')

    # Mevcut CSBM'nin indeksini bul
    try:
        mevcut_index = il_df[il_df['IL'] == mevcut_il].index[0]
    except IndexError:
        # Mevcut CSBM bulunamazsa, hata mesajı döndür
        return "Mevcut IL, IL.xlsx dosyasında bulunamadı."

    # Bir sonraki ILCE'nin indeksini kontrol et
    if mevcut_index + 1 < len(il_df):
        # Bir sonraki ıl'yi döndür
        return il_df.loc[mevcut_index + 1, 'IL']
    else:
        # Eğer bir sonraki IL yoksa, None döndür
        return None
def bir_sonraki_il_guncelle():
    # Bir sonraki IL'yi bul
    bir_sonraki_il = bir_sonraki_il_bul()

    if bir_sonraki_il is None:
        print("Bir sonraki İl bulunamadı veya SIRA.xlsx dosyası boş.")
        return
    elif isinstance(bir_sonraki_il, str) and bir_sonraki_il.startswith("Bir sonraki İl bulunamadı"):
        print(bir_sonraki_il)  # Hata mesajını yazdır
        return

    # SIRA.xlsx dosyasını oku
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        if not sira_df.empty:
            # 'IL SIRA' sütununun son değerini güncelle
            sira_df['IL SIRA'].iloc[-1] = bir_sonraki_il
            # 'ILCE' sütunundaki tüm değerleri sil
            sira_df['ILCE SIRA'] = pd.NA
            # 'MAHALLE' sütunundaki tüm değerleri sil
            sira_df['MAHALLE SIRA'] = pd.NA
            # 'CSBM' sütunundaki tüm değerleri sil
            sira_df['CSBM SIRA'] = pd.NA
            # 'BINA NO SIRA' sütunundaki tüm değerleri sil
            sira_df['BINA NO SIRA'] = pd.NA
            # Değişiklikleri kaydet
            sira_df.to_excel('SIRA.xlsx', index=False)
            print(f"'IL SIRA' sütunu '{bir_sonraki_il}' ile güncellendi.")
        else:
            print("SIRA.xlsx dosyası boş.")
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")

def bir_sonraki_ilce_bul():
    # SIRA.xlsx dosyasını yükle
    sira_df = pd.read_excel('SIRA.xlsx')

    # SIRA.xlsx dosyasının son satırından mevcut ILCE'yi al
    if not sira_df.empty:
        mevcut_ilce = sira_df.iloc[-1]['ILCE SIRA']
    else:
        return "SIRA.xlsx dosyası boş."

    # IL_ILCE_MAHALLE.xlsx dosyasını yükle
    ilce_df = pd.read_excel('IL_ILCE.xlsx')

    # Mevcut CSBM'nin indeksini bul
    try:
        mevcut_index = ilce_df[ilce_df['ILCE'] == mevcut_ilce].index[0]
    except IndexError:
        # Mevcut CSBM bulunamazsa, hata mesajı döndür
        return "Mevcut ILCE, IL_ILCE.xlsx dosyasında bulunamadı."

    # Bir sonraki ILCE'nin indeksini kontrol et
    if mevcut_index + 1 < len(ilce_df):
        # Bir sonraki CSBM'yi döndür
        return ilce_df.loc[mevcut_index + 1, 'ILCE']
    else:
        # Eğer bir sonraki ILCE yoksa, None döndür
        return None

def bir_sonraki_ilce_guncelle():
    # Bir sonraki CSBM'yi bul
    bir_sonraki_ilce = bir_sonraki_ilce_bul()

    if bir_sonraki_ilce is None:
        print("Bir sonraki İlçe bulunamadı veya SIRA.xlsx dosyası boş.")
        return
    elif isinstance(bir_sonraki_ilce, str) and bir_sonraki_ilce.startswith("Bir sonraki İlçe bulunamadı"):
        print(bir_sonraki_ilce)  # Hata mesajını yazdır
        return

    # SIRA.xlsx dosyasını oku
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        if not sira_df.empty:
            # 'ILCE SIRA' sütununun son değerini güncelle
            sira_df['ILCE SIRA'].iloc[-1] = bir_sonraki_ilce
            # 'MAHALLE' sütunundaki tüm değerleri sil
            sira_df['MAHALLE SIRA'] = pd.NA
            # 'CSBM' sütunundaki tüm değerleri sil
            sira_df['CSBM SIRA'] = pd.NA
            # 'BINA NO SIRA' sütunundaki tüm değerleri sil
            sira_df['BINA NO SIRA'] = pd.NA
            # Değişiklikleri kaydet
            sira_df.to_excel('SIRA.xlsx', index=False)
            print(f"'ILCE SIRA' sütunu '{bir_sonraki_ilce}' ile güncellendi.")
        else:
            print("SIRA.xlsx dosyası boş.")
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")

def bir_sonraki_mahalle_bul():
    # SIRA.xlsx dosyasını yükle
    sira_df = pd.read_excel('SIRA.xlsx')

    # SIRA.xlsx dosyasının son satırından mevcut CSBM'yi al
    if not sira_df.empty:
        mevcut_mahalle = sira_df.iloc[-1]['MAHALLE SIRA']
    else:
        return "SIRA.xlsx dosyası boş."

    # IL_ILCE_MAHALLE.xlsx dosyasını yükle
    mahalle_df = pd.read_excel('IL_ILCE_MAHALLE.xlsx')

    # Mevcut CSBM'nin indeksini bul
    try:
        mevcut_index = mahalle_df[mahalle_df['MAHALLE'] == mevcut_mahalle].index[0]
    except IndexError:
        # Mevcut CSBM bulunamazsa, hata mesajı döndür
        return "Mevcut MAHALLE, IL_ILCE_MAHALLE.xlsx dosyasında bulunamadı."

    # Bir sonraki MAHALLE'nin indeksini kontrol et
    if mevcut_index + 1 < len(mahalle_df):
        # Bir sonraki CSBM'yi döndür
        return mahalle_df.loc[mevcut_index + 1, 'MAHALLE']
    else:
        # Eğer bir sonraki MAHALLE yoksa, None döndür
        return None

def bir_sonraki_mahalle_guncelle():
    # Bir sonraki CSBM'yi bul
    bir_sonraki_mahalle = bir_sonraki_mahalle_bul()

    if bir_sonraki_mahalle is None:
        print("Bir sonraki Mahalle bulunamadı veya SIRA.xlsx dosyası boş.")
        return
    elif isinstance(bir_sonraki_mahalle, str) and bir_sonraki_mahalle.startswith("Bir sonraki Mahalle bulunamadı"):
        print(bir_sonraki_mahalle)  # Hata mesajını yazdır
        return

    # SIRA.xlsx dosyasını oku
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        if not sira_df.empty:
            # 'MAHALLE SIRA' sütununun son değerini güncelle
            sira_df['MAHALLE SIRA'].iloc[-1] = bir_sonraki_mahalle
            # 'CSBM' sütunundaki tüm değerleri sil
            sira_df['CSBM SIRA'] = pd.NA
            # 'BINA NO SIRA' sütunundaki tüm değerleri sil
            sira_df['BINA NO SIRA'] = pd.NA
            # Değişiklikleri kaydet
            sira_df.to_excel('SIRA.xlsx', index=False)
            print(f"'MAHALLE SIRA' sütunu '{bir_sonraki_mahalle}' ile güncellendi.")
        else:
            print("SIRA.xlsx dosyası boş.")
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")

def bir_sonraki_csbm_bul():
    # SIRA.xlsx dosyasını yükle
    sira_df = pd.read_excel('SIRA.xlsx')

    # SIRA.xlsx dosyasının son satırından mevcut CSBM'yi al
    if not sira_df.empty:
        mevcut_csbm = sira_df.iloc[-1]['CSBM SIRA']
    else:
        return "SIRA.xlsx dosyası boş."

    # IL_ILCE_MAHALLE_CSBM_BINA_NO.xlsx dosyasını yükle
    csbm_df = pd.read_excel('IL_ILCE_MAHALLE_CSBM.xlsx')

    # Mevcut CSBM'nin indeksini bul
    try:
        mevcut_index = csbm_df[csbm_df['CSBM'] == mevcut_csbm].index[0]
    except IndexError:
        # Mevcut CSBM bulunamazsa, hata mesajı döndür
        return "Mevcut CSBM, IL_ILCE_MAHALLE_CSBM.xlsx dosyasında bulunamadı."

    # Bir sonraki CSBM'nin indeksini kontrol et
    if mevcut_index + 1 < len(csbm_df):
        # Bir sonraki CSBM'yi döndür
        return csbm_df.loc[mevcut_index + 1, 'CSBM']
    else:
        # Eğer bir sonraki CSBM yoksa, None döndür
        return None

def bir_sonraki_csbm_guncelle():
    # Bir sonraki CSBM'yi bul
    bir_sonraki_csbm = bir_sonraki_csbm_bul()

    if bir_sonraki_csbm is None:
        print("Bir sonraki CSBM bulunamadı veya SIRA.xlsx dosyası boş.")
        return
    elif isinstance(bir_sonraki_csbm, str) and bir_sonraki_csbm.startswith("Bir sonraki CSBM bulunamadı"):
        print(bir_sonraki_csbm)  # Hata mesajını yazdır
        return

    # SIRA.xlsx dosyasını oku
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        if not sira_df.empty:
            # 'CSBM SIRA' sütununun son değerini güncelle
            sira_df['CSBM SIRA'].iloc[-1] = bir_sonraki_csbm
            # 'BINA NO SIRA' sütunundaki tüm değerleri sil
            sira_df['BINA NO SIRA'] = pd.NA
            # Değişiklikleri kaydet
            sira_df.to_excel('SIRA.xlsx', index=False)
            print(f"SIRA {bir_sonraki_csbm}' ile güncellendi.")
        else:
            print("SIRA.xlsx dosyası boş.")
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")

def bir_sonraki_bina_bul():
    # SIRA.xlsx dosyasını yükle
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        # SIRA.xlsx dosyasının son satırından mevcut Bina No'yu al
        if not sira_df.empty:
            mevcut_bina_no = sira_df.iloc[-1]['BINA NO SIRA']
        else:
            return "SIRA.xlsx dosyası boş."
    except FileNotFoundError:
        return "SIRA.xlsx dosyası bulunamadı."

    # IL_ILCE_MAHALLE_CSBM_BINA_NO.xlsx dosyasını yükle
    try:
        bina_df = pd.read_excel('IL_ILCE_MAHALLE_CSBM_BINA_NO.xlsx')
    except FileNotFoundError:
        return "IL_ILCE_MAHALLE_CSBM_BINA_NO.xlsx dosyası bulunamadı."

    # Mevcut Bina No'nun indeksini bul
    try:
        mevcut_index = bina_df[bina_df['BINA NO'] == mevcut_bina_no].index[0]
    except IndexError:
        return "Mevcut Bina No, IL_ILCE_MAHALLE_CSBM_BINA_NO.xlsx dosyasında bulunamadı."

    # Bir sonraki Bina No'nun indeksini kontrol et
    if mevcut_index + 1 < len(bina_df):
        # Bir sonraki Bina No'yu döndür
        return bina_df.loc[mevcut_index + 1, 'BINA NO']
    else:
        # Eğer bir sonraki Bina No yoksa, None döndür
        return None

def bir_sonraki_bina_guncelle():
    # Bir sonraki Bina No'yu bul
    bir_sonraki_bina_no = bir_sonraki_bina_bul()

    if bir_sonraki_bina_no is None:
        return
    elif isinstance(bir_sonraki_bina_no, str) and bir_sonraki_bina_no.startswith("Bir sonraki Bina No bulunamadı"):
        print(bir_sonraki_bina_no)  # Hata mesajını yazdır
        return

    # SIRA.xlsx dosyasını oku
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        if not sira_df.empty:
            # 'BINA NO SIRA' sütununun son değerini güncelle
            sira_df['BINA NO SIRA'].iloc[-1] = bir_sonraki_bina_no
            # Değişiklikleri kaydet
            sira_df.to_excel('SIRA.xlsx', index=False)
        else:
            print("SIRA.xlsx dosyası boş.")
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")

def main():
    try:
        options = Options()
        
        options.headless = True  # Arka plan çalıştırma için True, görsel için False
        
        # driver = webdriver.Firefox(options=options, service=service)
        driver = webdriver.Chrome(options=options)

        driver.get("https://adres.nvi.gov.tr/Home")
    except Exception as e:
        print('Hata ', e )
        sys.exit()

    while True:
        driver.get("https://adres.nvi.gov.tr/VatandasIslemleri/AdresSorgu")

        try:
            # Sayfa yüklendikten sonra Recaptcha'nın yüklenip yüklenmediğini kontrol etmek için bekleyin
            try:
                # Recaptcha çerçevesinin varlığını kontrol etmek için bir bekleme yapın
                recaptcha_frame = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']"))
                )
                print("reCAPTCHA bulundu.")

                # Kullanıcıya doğrulama yapması için bir mesaj gösterin
                print("Lütfen reCAPTCHA'yı çözün ve ENTER tuşuna basın...")

                # Kullanıcı ENTER tuşuna basana kadar bekleyin
                while True:
                    user_input = input()  # Kullanıcının girdisini alın
                    if user_input == "":
                        break  # Kullanıcı ENTER tuşuna bastığında döngüyü sonlandırın

                # Kullanıcı ENTER tuşuna bastıktan sonra işleme devam edebilirsiniz

            except:
                print("reCAPTCHA bulunamadı veya gerekmeyebilir.")

            sira_dosyasi_olusturma()
            il_dosyası_olusturma()
                    
            il_kaydet(driver)
            il_sira_ekle()
            iller_df = pd.read_excel('IL.xlsx')

            secilen_il_adi = secilen_il_def()
            secilen_ilce_adi = secilen_ilce_def()
            secilen_mahalle_adi = secilen_mahalle_def()
            secilen_csbm_adi = secilen_csbm_def()
            secilen_bina_adi = secilen_bina_def()

            # İl adını Excel dosyasından ara
            secilen_il = iller_df[iller_df['IL'].str.lower() == secilen_il_adi.lower()]
            process_il(driver,secilen_il, secilen_il_adi)

            ilce_dosyası_olusturma()
            ilce_kaydet(driver, secilen_il_adi)
            ilce_sira_ekle()
            ilceler_df = pd.read_excel('IL_ILCE.xlsx')
            secilen_il_adi = secilen_il_def()
            secilen_ilce_adi = secilen_ilce_def()
            secilen_mahalle_adi = secilen_mahalle_def()
            secilen_csbm_adi = secilen_csbm_def()
            secilen_bina_adi = secilen_bina_def()

            # İlçe adını Excel dosyasından ara
            secilen_ilce = ilceler_df[ilceler_df['ILCE'].str.lower() == secilen_ilce_adi.lower()]
            process_ilce(driver, secilen_ilce, secilen_ilce_adi)

            mahalle_dosyası_olusturma()

            # İlgili ilçe için mahalleleri işle
            mahalle_kaydet(driver, secilen_il_adi, secilen_ilce_adi)
            mahalle_sira_ekle()
            mahalleler_df = pd.read_excel('IL_ILCE_MAHALLE.xlsx')
            secilen_il_adi = secilen_il_def()
            secilen_ilce_adi = secilen_ilce_def()
            secilen_mahalle_adi = secilen_mahalle_def()
            secilen_csbm_adi = secilen_csbm_def()
            secilen_bina_adi = secilen_bina_def()

            # Mahalle adını Excel dosyasından ara
            secilen_mahalle = mahalleler_df[mahalleler_df['MAHALLE'].str.lower() == secilen_mahalle_adi.lower()]

            process_mahalle(driver, secilen_mahalle, secilen_mahalle_adi)


            sokak_dosyası_olusturma()
            sokak_kaydet(driver, secilen_il_adi, secilen_ilce_adi, secilen_mahalle_adi)
            csbm_sira_ekle()
            csbm_df = pd.read_excel('IL_ILCE_MAHALLE_CSBM.xlsx')
            secilen_il_adi = secilen_il_def()
            secilen_ilce_adi = secilen_ilce_def()
            secilen_mahalle_adi = secilen_mahalle_def()
            secilen_csbm_adi = secilen_csbm_def()
            secilen_bina_adi = secilen_bina_def()

            # CSBM adını Excel dosyasından ara
            secilen_csbm = csbm_df[csbm_df['CSBM'].str.lower() == secilen_csbm_adi.lower()]
            process_sokak(driver, secilen_csbm, secilen_csbm_adi)

            bina_sira_ekle()
            bina_df = pd.read_excel('IL_ILCE_MAHALLE_CSBM_BINA_NO.xlsx')
            print(bina_df)
            secilen_il_adi = secilen_il_def()
            secilen_ilce_adi = secilen_ilce_def()
            secilen_mahalle_adi = secilen_mahalle_def()
            secilen_csbm_adi = secilen_csbm_def()
            secilen_bina_adi = secilen_bina_def()
            print(secilen_bina_adi)
            # Bina adını Excel dosyasından ara
            secilen_bina = bina_df[bina_df['BINA NO'].str.lower() == secilen_bina_adi.lower()]
            print(secilen_bina)

            process_bina(driver,secilen_bina, secilen_bina_adi)

            dis_kapi_listesi = bina_kaydet(driver, secilen_il_adi, secilen_ilce_adi, secilen_mahalle_adi, secilen_csbm_adi)
            homepass_dosyası_olusturma()

            # Fonksiyonu çağır
            bir_sonraki_bina = bir_sonraki_bina_bul()
            bir_sonraki_bina_guncelle()

            # Her bina için Homepass bilgilerini işle
            process_homepass(driver, secilen_il_adi, secilen_ilce_adi, secilen_mahalle_adi,
                            secilen_csbm_adi, dis_kapi_listesi, secilen_bina_adi)

            # Eğer son bina işlendi ise, bir sonraki sokağa geç
            if bir_sonraki_bina== None:
                print(
                    f"{secilen_csbm_adi} sokagindaki binaların tamamı kaydedildi, bir sonraki sokağa geçiliyor.")
                # Fonksiyonu çağır
                bir_sonraki_csbm = bir_sonraki_csbm_bul()
                bir_sonraki_csbm_guncelle()
                break  # Bu sokaktaki işlemi bitir ve bir sonraki sokağa geç

            # Eğer son sokak işlendi ise ve sokak işlemi tamamlandıysa, bir sonraki sokağa geç
            if bir_sonraki_csbm == None:
                print(
                    f"{secilen_mahalle_adi}  mahallesinde bulunan binaların tamamı kaydedildi, bir sonraki mahalleye geçiliyor.")
                # Fonksiyonu çağır
                bir_sonraki_mahalle = bir_sonraki_mahalle_bul()
                bir_sonraki_mahalle_guncelle()
                break  # Bu sokaktaki işlemi bitir ve bir sonraki sokağa geç

            # Eğer son sokak işlendi ise ve mahalle işlemi tamamlandıysa, bir sonraki mahalleye geç
            if bir_sonraki_mahalle == None:
                print(
                    f"{secilen_ilce_adi} ilçesinde bulunan binaların tamamı kaydedildi, bir sonraki ilçeye geçiliyor.")
                # Fonksiyonu çağır
                bir_sonraki_ilce = bir_sonraki_ilce_bul()
                bir_sonraki_ilce_guncelle()
                break  # Bu mahalledeki işlemi bitir ve bir sonraki mahalleye geç
            # Eğer son mahalle işlendi ise ve ilçe işlemi tamamlandıysa, bir sonraki ilçeye geç
            if bir_sonraki_ilce==None:
                print(
                    f"{secilen_il_adi} ilinde bulunan binaların tamamı kaydedildi, bir sonraki ile geçiliyor.")
                # Fonksiyonu çağır
                bir_sonraki_il = bir_sonraki_il_bul()
                bir_sonraki_il_guncelle()
                break  # Bu ilçedeki işlemi bitir ve bir sonraki ilçeye geç
            # Eğer son mahalle işlendi ise ve ilçe işlemi tamamlandıysa, bir sonraki ilçeye geç
            if bir_sonraki_il==None:
                print("Türkiye'de bulunan binaların tamamı kaydedildi.")
                # Fonksiyonu çağır
                bir_sonraki_tum = bir_sonraki_tum_bul()
                bir_sonraki_tum_guncelle()
                break  # Bu ilindeki işlemi bitir ve bir sonraki ile geç

            print("Tüm işlemler tamamlandı.")
            break
        except Exception as e:
            print(f"Hata: Görmezden gelerek devam edelim.{e}")
            continue

if __name__== '__main__':
    main()
    