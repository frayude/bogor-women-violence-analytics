import pandas as pd
import numpy as np
from pathlib import Path

def load_data():
    file_path = Path(__file__).parent.parent / "data" / "korban_kekerasan_bogor_2017-2021.xlsx"
    
    df = pd.read_excel(file_path)
    
    return df

df = load_data()

def preprocess_status(df):
    # Cleaning column status data is dirty
    df["Status"] = (
        df["Status"]
        .str.replace('●', '', regex=False)
        .str.replace('\uf0b7', '', regex=False)
        .str.replace('\n', ' ', regex=False)
        .str.replace(r'\.+', "", regex=True)
        .str.strip()
        .replace("", np.nan)
        .str.title()
        )

    conditions = [
    df["Status"].str.contains("Proses|Sidang", na=False),
    df["Status"].str.contains("Selesai|Cerai", na=False),
    df["Status"].str.contains("Dirujuk", na=False),
    df["Status"].str.contains("Terhenti", na=False),
    ]
    
    choices = ["Dalam Proses", "Selesai", "Dirujuk" , "Terhenti"]

    df["Status"] = np.select(conditions, choices, default="Masih Berjalan")
    
    # delete null cell
    df.dropna(subset=["Status"], inplace=True)
    
    return df

def preprocess_penanganan(df):
    df["Penanganan"] = (
        df["Penanganan"]
        .str.title()
        .str.replace('\uf0b7', '', regex=False)
        .str.replace('●', '', regex=False)
        .str.replace('•', '', regex=False)
        .str.replace(r'\s+', " ", regex=True)
        .str.strip()
        .replace("", np.nan)
    )

    conditions = [
    df["Penanganan"].str.contains("Konseling Hukum", na=False),
    df["Penanganan"].str.contains("Telp|Telepon|Via Wa|Hotline", na=False),
    df["Penanganan"].str.contains("Visit", na=False),
    df["Penanganan"].str.contains("Psikolog|Psikologi|Psikologis|Mediasi|Relaksasi", na=False),
    ]
    
    choices = ["Konseling Hukum", "Konseling Via Telepon", "Home Visit", "Konseling Psikologis"]

    df["Penanganan"] = np.select(conditions, choices, default="Konseling Penguatan")
    
    df.dropna(subset=["Penanganan"], inplace=True)
    
    return df

def preprocess_data(df):
    df.drop(columns=["NO", "Nama Inisial", "Keterangan"], inplace = True)
    df.dropna(inplace=True)
    
    df = preprocess_status(df)
    df = preprocess_penanganan(df)

    return df
    
preprocess_data(df)

def get_total_kasus(df):
    return len(df)

# get_total_kasus(df)

def get_kasus_per_tahun(df):
    return df.groupby("Tahun").size()
    
# get_kasus_per_tahun(df)

def get_kasus_per_kecamatan(df):
    return df.groupby("Kecamatan").size()

# get_kasus_per_kecamatan(df)

def get_kasus_per_jenis(df):
    return df.groupby("Jenis Kekerasan").size()

# get_kasus_per_jenis(df)

def get_kasus_per_status(df):
    return df.groupby("Status").size()

# get_kasus_per_status(df)

def get_kasus_penanganan(df):
    return df.groupby("Penanganan").size()

get_kasus_penanganan(df)