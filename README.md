# insurance-etl-project

This project implements a complete **Extract, Transform, Load (ETL)** working flow using Python and Pandas to convert raw insurance demographic and charge data into clean and feature-riched datasets that are optimized for predictive modeling.

## 🛠️Key Technologies
- **Python 3.13**
- **pandas** : For efficient data manipulation and loading.
- **scikit-learn** : For model training, standard scaling and train-test-split.
- **SQLAlchemy** : For creating a robust connection to the PostgreSQL database.
- **POstgreSQL** : The destionation database for the final, processed data.

The pipe line is architected into five modular scripits

- Extraction: Reads the intial data from CSV source.

- Cleaning: Employs **IQR-based outlier detection** on the **charges** columns and handles duplicates/missing values.

- Feature Engineering: Creates model-ready features. Using **one-hot encoding** for categorical variables and generating critical interaction terms (the product of age and BMI).

- Scaling
- Loading

