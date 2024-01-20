
import pandas as pd 

def secilen_il_def():
    # SIRA.xlsx dosyasını yükle
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        # İlk il adını döndür
        if not sira_df.empty and not sira_df['IL SIRA'].isna().all():
            return sira_df['IL SIRA'].dropna().iloc[0]
        else:
            return None
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")
        return None
    
def secilen_ilce_def():
    # SIRA.xlsx dosyasını yükle
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        # İlk ilce adını döndür
        if not sira_df.empty and not sira_df['ILCE SIRA'].isna().all():
            return sira_df['ILCE SIRA'].dropna().iloc[0]
        else:
            return None
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")
        return None
    
def secilen_mahalle_def():
    # SIRA.xlsx dosyasını yükle
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        # İlk mahalle adını döndür
        if not sira_df.empty and not sira_df['MAHALLE SIRA'].isna().all():
            return sira_df['MAHALLE SIRA'].dropna().iloc[0]
        else:
            return None
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")
        return None
def secilen_csbm_def():
    # SIRA.xlsx dosyasını yükle
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        # İlk CSBM adını döndür
        if not sira_df.empty and not sira_df['CSBM SIRA'].isna().all():
            return sira_df['CSBM SIRA'].dropna().iloc[0]
        else:
            return None
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")
        return None

def secilen_bina_def():
    # SIRA.xlsx dosyasını yükle
    try:
        sira_df = pd.read_excel('SIRA.xlsx')
        # İlk BINA NO adını döndür
        if not sira_df.empty and not sira_df['BINA NO SIRA'].isna().all():
            return sira_df['BINA NO SIRA'].dropna().iloc[0]
        else:
            return None
    except FileNotFoundError:
        print("SIRA.xlsx dosyası bulunamadı.")
        return None