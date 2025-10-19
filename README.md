# Insurance Data ETL & ML Pipeline

This project implements a complete **Extract, Transform, Load (ETL)** working flow using Python and Pandas to convert raw insurance demographic and charge data into clean and feature-riched datasets that are optimized for predictive modeling.

## 🛠️Key Technologies
- **Python 3.13**
- **pandas** : Data manipulation and core ETL.
- **scikit-learn** : Feature scaling (StandardScaler) and Machine Learning modeling/evaluation.
- **SQLAlchemy** : Database connection management.
- **POstgreSQL** : Target database for cleaned dataset.
- **Jupyter Notebook** : Enviroment for the final ML modeling and experimentation.

## ⚙️Pipeline Architecture
### ETL Pipeline (Scripts)
- **run_pipeline.py** [Orchestrator] Main entry point that executes the ETL steps sequentially.
- **scripts/extract.py** [Extract] Reads raw **insurance.csv** data into a DataFrame.
- **scripts/clean.py** [Transform] Remove duplicates and missing values. Implement IQR-based outlier removal on the charges column.
- **scripts/feature_engineering.py** [Transform] Converts categorical data using **One-Hot Encoding**. Creates **interaction features** (e.g., bmi_smoker)**Standard Scales** all numerical features.
- **scripts/load.py** [Load] Connects to PostgreSQL and loads the final DataFrame into the **insurance_features_scaled** table.

### Machine Learning (Notebook)
- **ml_layer.ipynb** [Modeling & Evaluation] Connects to the PostgreSQL and retrieve the ML-ready data. Split and train into a Linear Regression Model. Evalutes its performance on predicting medical charges.

## 🚀How to Run The Pipeline
### Prerequisites
1. Python 3 installed
2. A running instance of PostgreSQL
3. The input csv file (insurnace.csv) placed in a designed **data/directory**.
 > #Clone the repository 
 > git clone https://github.com/ZwePP/insurance-etl-project.git
 >
 > #Install dependencies
 > pip install pandas scikit-learn sqlalchemy psycopg2-binary jupyer
 >#**Configuration**: Update database credentials in scripts/load.py
 > #engine = create_engine("postgresql://postgres:YOUR_PASSWORD@localhost:5432/postgres")
 >
 >




