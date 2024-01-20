
import os
import pandas as pd 

def create_casted_df(keys):
    dtypes = {k:str for k in keys }
    df = pd.DataFrame(columns=dtypes.keys()).astype(dtypes)
    return df
    
def sira_dosyasi_olusturma():
    file_path = 'SIRA.xlsx'
    if not os.path.exists(file_path):

        # Create a DataFrame with specified data types
        df = create_casted_df(['IL SIRA', 'ILCE SIRA', 'MAHALLE SIRA', 'CSBM SIRA', 'BINA NO SIRA'])
        
        try:
            # Save the DataFrame to an Excel file
            df.to_excel(file_path, index=False)
            print(f"{file_path} created successfully.")
        except Exception as e:
            print(f"Error creating {file_path}: {e}")
    else:
        print(f"{file_path} already exists.")
        
def il_dosyası_olusturma():
    # File path for the Excel file
    file_path = 'IL.xlsx'
    if not os.path.exists(file_path):
        # Create a DataFrame with specified data types
        df = create_casted_df(['IL'])

        # Saving this DataFrame to an Excel file
        df.to_excel(file_path, index=False)
def ilce_dosyası_olusturma():
    # File path for the Excel file
    file_path = 'IL_ILCE.xlsx'
    if not os.path.exists(file_path):        
        # Create a DataFrame with specified data types
        df = create_casted_df(['IL', 'ILCE'])
        
        # Saving this DataFrame to an Excel file named
        df.to_excel(file_path, index=False)

def mahalle_dosyası_olusturma():
    # File path for the Excel file
    file_path = 'IL_ILCE_MAHALLE.xlsx'
    if not os.path.exists(file_path):
        
        # Create a DataFrame with specified data types
        df = create_casted_df(['IL', 'ILCE', 'MAHALLE'])
        # Saving this DataFrame to an Excel file named
        df.to_excel(file_path, index=False)

def sokak_dosyası_olusturma():
    # File path for the Excel file
    file_path = 'IL_ILCE_MAHALLE_CSBM.xlsx'
    if not os.path.exists(file_path):
        
        # Create a DataFrame with specified data types
        df = create_casted_df(['IL', 'ILCE', 'MAHALLE', 'CSBM'])
        # Saving this DataFrame to an Excel file named
        df.to_excel(file_path, index=False)

def bina_dosyası_olusturma():
    # File path for the Excel file
    file_path = 'IL_ILCE_MAHALLE_CSBM_BINA_NO.xlsx'
    if not os.path.exists(file_path):

        # Create a DataFrame with specified data types
        df = create_casted_df(['IL', 'ILCE', 'MAHALLE', 'CSBM', 'BINA NO'])
        # Saving this DataFrame to an Excel file named
        df.to_excel(file_path, index=False)

def homepass_dosyası_olusturma():
    # Excel dosyasının yolu
    file_path = 'IL_ILCE_MAHALLE_CSBM_BINA_NO_HOMEPASS.xlsx'

    if not os.path.exists(file_path):
        # Create a DataFrame with specified data types
        df = create_casted_df(['IL', 'ILCE', 'MAHALLE', 'CSBM', 'BINA NO', 'HOMEPASS'])
        # Bu DataFrame'i bir Excel dosyasına kaydet
        df.to_excel(file_path, index=False)
