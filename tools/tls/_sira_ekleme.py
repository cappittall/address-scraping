
import pandas as pd

from _dosya_olusturma import create_casted_df 

def il_sira_ekle():
    sira_dosyasi = 'SIRA.xlsx'
    il_dosyasi = 'IL.xlsx'

    try:
        df_sira = pd.read_excel(sira_dosyasi)
    except FileNotFoundError:

        # Create a DataFrame with specified data types
        df_sira = create_casted_df(['IL SIRA', 'ILCE SIRA', 'MAHALLE SIRA', 'CSBM SIRA', 'BINA NO SIRA'])
        
    # Eğer 'IL SIRA' sütunu boşsa veya tamamen NaN ise, IL.xlsx'den ilk il adını al
    if df_sira.empty or df_sira['IL SIRA'].isna().all():
        try:
            df_il = pd.read_excel(il_dosyasi)
            ilk_il_adi = df_il['IL'].iloc[0]
            df_sira.loc[0, 'IL SIRA'] = ilk_il_adi
            # Değişiklikleri aynı dosyaya kaydet
            df_sira.to_excel(sira_dosyasi, index=False)
            print(f"'{ilk_il_adi}' SIRA.xlsx dosyasına eklendi.")
        except FileNotFoundError:
            print(f"'{il_dosyasi}' dosyası bulunamadı.")
        except IndexError:
            print(f"'{il_dosyasi}' dosyasında il bilgisi bulunamadı.")
    else:
        pass
    
def ilce_sira_ekle():
    sira_dosyasi = 'SIRA.xlsx'
    ilce_dosyasi = 'IL_ILCE.xlsx'

    try:
        df_sira = pd.read_excel(sira_dosyasi)
    except FileNotFoundError:

        # Create a DataFrame with specified data types
        df_sira = create_casted_df(['IL SIRA', 'ILCE SIRA', 'MAHALLE SIRA', 'CSBM SIRA', 'BINA NO SIRA'])
        
    # Eğer 'ILCE SIRA' sütunu boşsa veya tamamen NaN ise,
    if df_sira.empty or df_sira['ILCE SIRA'].isna().all():
        try:
            df_ilce = pd.read_excel(ilce_dosyasi)
            ilk_ilce_adi = df_ilce['ILCE'].iloc[0]
            df_sira.loc[0, 'ILCE SIRA'] = ilk_ilce_adi
            # Değişiklikleri aynı dosyaya kaydet
            df_sira.to_excel(sira_dosyasi, index=False)
            print(f"'{ilk_ilce_adi}' SIRA.xlsx dosyasına eklendi.")
        except FileNotFoundError:
            print(f"'{ilce_dosyasi}' dosyası bulunamadı.")
        except IndexError:
            print(f"'{ilce_dosyasi}' dosyasında ilçe bilgisi bulunamadı.")
    else:
        pass
def mahalle_sira_ekle():
    sira_dosyasi = 'SIRA.xlsx'
    mahalle_dosyasi = 'IL_ILCE_MAHALLE.xlsx'

    try:
        df_sira = pd.read_excel(sira_dosyasi)
    except FileNotFoundError:
        # Explicitly set data types for each column
        dtypes = {'IL SIRA', 'ILCE SIRA', 'MAHALLE SIRA', 'CSBM SIRA', 'BINA NO SIRA'}
        # Create a DataFrame with specified data types
        df_sira = pd.DataFrame(columns=dtypes.keys()).astype(dtypes)
    # Eğer 'MAHALLE SIRA' sütunu boşsa veya tamamen NaN ise,
    if df_sira.empty or df_sira['MAHALLE SIRA'].isna().all():
        try:
            df_mahalle = pd.read_excel(mahalle_dosyasi)
            ilk_mahalle_adi = df_mahalle['MAHALLE'].iloc[0]
            df_sira.loc[0, 'MAHALLE SIRA'] = ilk_mahalle_adi
            # Değişiklikleri aynı dosyaya kaydet
            df_sira.to_excel(sira_dosyasi, index=False)
            print(f"'{ilk_mahalle_adi}' SIRA.xlsx dosyasına eklendi.")
        except FileNotFoundError:
            print(f"'{mahalle_dosyasi}' dosyası bulunamadı.")
        except IndexError:
            print(f"'{mahalle_dosyasi}' dosyasında Mahalle bilgisi bulunamadı.")
    else:
        pass
def csbm_sira_ekle():
    sira_dosyasi = 'SIRA.xlsx'
    csbm_dosyasi = 'IL_ILCE_MAHALLE_CSBM.xlsx'

    try:
        df_sira = pd.read_excel(sira_dosyasi)
    except FileNotFoundError:

        # Explicitly set data types for each column
        dtypes = {'IL SIRA', 'ILCE SIRA', 'MAHALLE SIRA', 'CSBM SIRA', 'BINA NO SIRA'}
        # Create a DataFrame with specified data types
        df_sira = pd.DataFrame(columns=dtypes.keys()).astype(dtypes)
    # Eğer 'CSBM SIRA' sütunu boşsa veya tamamen NaN ise,
    if df_sira.empty or df_sira['CSBM SIRA'].isna().all():
        try:
            df_csbm = pd.read_excel(csbm_dosyasi)
            ilk_csbm_adi = df_csbm['CSBM'].iloc[0]
            df_sira.loc[0, 'CSBM SIRA'] = ilk_csbm_adi
            # Değişiklikleri aynı dosyaya kaydet
            df_sira.to_excel(sira_dosyasi, index=False)
            print(f"'{ilk_csbm_adi}' SIRA.xlsx dosyasına eklendi.")
        except FileNotFoundError:
            print(f"'{csbm_dosyasi}' dosyası bulunamadı.")
        except IndexError:
            print(f"'{csbm_dosyasi}' dosyasında CSBM bilgisi bulunamadı.")
    else:
        pass

def bina_sira_ekle():
    sira_dosyasi = 'SIRA.xlsx'
    bina_dosyasi = 'IL_ILCE_MAHALLE_CSBM_BINA_NO.xlsx'

    try:
        df_sira = pd.read_excel(sira_dosyasi)
    except FileNotFoundError:
        # Explicitly set data types for each column
        dtypes = {'IL SIRA', 'ILCE SIRA', 'MAHALLE SIRA', 'CSBM SIRA', 'BINA NO SIRA'}
        # Create a DataFrame with specified data types
        df_sira = pd.DataFrame(columns=dtypes.keys()).astype(dtypes)
        
    # Eğer 'BINA NO SIRA' sütunu boşsa veya tamamen NaN ise,
    if df_sira.empty or df_sira['BINA NO SIRA'].isna().all():
        try:
            df_bina = pd.read_excel(bina_dosyasi)
            ilk_bina_adi = df_bina['BINA NO'].iloc[0]
            df_sira.loc[0, 'BINA NO SIRA'] = ilk_bina_adi
            # Değişiklikleri aynı dosyaya kaydet
            df_sira.to_excel(sira_dosyasi, index=False)
            print(f"'{ilk_bina_adi}' SIRA.xlsx dosyasına eklendi.")
        except FileNotFoundError:
            print(f"'{bina_dosyasi}' dosyası bulunamadı.")
        except IndexError:
            print(f"'{bina_dosyasi}' dosyasında BINA NO bilgisi bulunamadı.")
    else:
        pass