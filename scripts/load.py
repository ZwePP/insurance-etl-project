# Load the DF postgres
import pandas as pd
from sqlalchemy import create_engine

def load_to_postgres(df, table_name):
    print('Loading to Postgres....')
    engine = create_engine("postgresql://postgres:8102002@localhost:5432/postgres")
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ Loaded {len(df)} rows to table: {table_name}")
