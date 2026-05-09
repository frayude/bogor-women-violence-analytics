import pandas as pd
from pathlib import Path

def load_data():
    file_path = Path(__file__).parent.parent / "data" / "korban_kekerasan_bogor_2017-2021.xlsx"
    
    df = pd.read_excel(file_path)
    
    return df

# df = load_data()

def preprocess_data(df):
    df.drop(columns=["NO", "Nama Inisial", "Keterangan"], inplace = True)
    df.dropna()
    return df

# df_clean = preprocess_data(df)