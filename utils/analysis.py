import pandas as pd
from pathlib import Path

def load_data():
    file_path = Path(__file__).parent.parent / "data" / "korban_kekerasan_bogor_2017-2021.xlsx"
    
    df = pd.read_excel(file_path)
    
    return df

df = load_data()

def preprocess_data(df):
    df.drop(columns=["NO", "Nama Inisial", "Keterangan"], inplace = True)
    df.dropna(inplace=True)
        
    return df

df_clean = preprocess_data(df)

def get_total_kasus(df):
    return len(df)

def get_kasus_per_tahun(df):
    return df.groupby("Tahun").size()
    
total_kasus_pertahun = get_kasus_per_tahun(df)

def get_kasus_per_kecamatan(df):
    return df.groupby("Kecamatan").size()

get_kasus_per_kecamatan(df)

def get_kasus_per_jenis(df):
    return df.groupby("Jenis Kekerasan").size()

get_kasus_per_jenis(df)

def get_kasus_per_status(df):
    return df.groupby("Status").size()

print(get_kasus_per_status(df))
