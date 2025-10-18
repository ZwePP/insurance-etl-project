import pandas as pd

def extract_data(path):
    print("📥 Extracting data...")
    df = pd.read_csv(path)
    print(f'Loaded {len(df)} rows.')
    return df

