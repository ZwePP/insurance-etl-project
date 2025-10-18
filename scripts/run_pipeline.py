from scripts.extract import extract_data
from scripts.clean import clean_data
from scripts.feature_engineering import feature_engineering
from scripts.load import load_to_postgres

def run_pipeline():
    #Step 1: Extract Raw Data
    df_raw = extract_data('data/insurance.csv')

    #Step 2: Clean Data
    df_clean = clean_data(df_raw)

    #Step 3: Feature Engineering
    df_fe = feature_engineering(df_clean)

    #Step 4: Load to Postgres
    df_load = load_to_postgres(df_fe, table_name='insurance_features_scaled')

if __name__ == "__main__":
    run_pipeline()