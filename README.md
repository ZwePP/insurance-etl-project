# Insurance Data ETL & ML Pipeline

This project implements a complete **Extract, Transform, Load (ETL)** working flow using Python and Pandas to convert raw insurance demographic and charge data into clean and feature-riched datasets that are optimized for predictive modeling.

## 🛠️Key Technologies
- **Python 3.13**
- **pandas** : Data manipulation and ETL core.
- **scikit-learn** : Feature scaling (StandardScaler) and Machine Learning modeling/evaluation.
- **SQLAlchemy** : Database connection management.
- **POstgreSQL** : Target database for cleaned dataset.
- **Jupyter Notebook** : Enviroment for the final ML modeling and experimentation.

## ⚙️Pipeline Architecture
### ETL Pipeline (Scripts)
- **run_pipeline.py** [Orchestrator] Main entry point that executes the ETL steps sequentially
- **scripts/extract.py** [Extract] Reads raw **insurance.csv** data into a DataFrame
- **scripts/clean.py** [Transform] Remove duplicates and missing values. Implement IQR-based outlier removal on the charges column
- **scripts/feature_engineering.py** [Transform] Converts categorical data using **One-Hot Encoding**. Creates **interaction features** (e.g., bmi_smoker)**Standard Scales** all numerical features.
- **scripts/load.py** [Load] Connects to PostgreSQL and loads the final DataFrame into the **insurance_features_scaled** table.

### Machine Learning (Notebook)
- **ml_layer.ipynb** [Modeling_&_Evaluation]Connects to the PostgreSQL and retrieve the ML-ready data. Split and train into a Linear Regression Model. Evalutes its performance on predicting medical charges.



