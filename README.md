# insurance-etl-project

This project implements a complete **Extract, Transform, Load (ETL)** working flow using Python and Pandas to convert raw insurance demographic and charge data into clean and feature-riched datasets that are optimized for predictive modeling.

## 🛠️Key Technologies
- **Python 3.13**
- **pandas** : For efficient data manipulation and loading.
- **scikit-learn** : For model training, standard scaling and train-test-split.
- **SQLAlchemy** : For creating a robust connection to the PostgreSQL database.
- **POstgreSQL** : The destionation database for the final, processed data.

## ⚙️Pipeline Architecture
> **run_pipeline.py** [Orchestrator] Main entry point that executes the ETL steps sequentially
> **scripts/extract.py** [Extract] Reads raw **insurance.csv** data into a DataFrame
> **scripts/clean.py** [Transform] Remove duplicates and missing values. Implement IQR-based outlier removal on the charges column
> **scripts/feature_engineering.py** [Transform] Converts categorical data using **One-Hot Encoding**. Creates **interaction features** (e.g., bmi_smoker). **Standard Scales** all numerical features.
> **scripts/load.py** [Load] Connects to PostgreSQL and loads the final DataFrame into the **insurance_features_scaled** table.



