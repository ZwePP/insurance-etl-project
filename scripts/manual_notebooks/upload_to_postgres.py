import pandas as pd
from sqlalchemy import create_engine

#Connect to database
engine = create_engine("postgresql://postgres:8102002@localhost:5432/postgres")

#Load CSV
cleaned_df = pd.read_csv('data/clean_insurance.csv')
scaled_df = pd.read_csv('data/insurance_scaled_final.csv')

#Upload CSV
cleaned_df.to_sql("cleaned_data", engine, if_exists='replace', index='False')
print('Clean Data Uploaded') #clean_data

scaled_df.to_sql("scaled_data", engine, if_exists='replace', index='False')
print('Scaled Data uploaded') #scaled_data