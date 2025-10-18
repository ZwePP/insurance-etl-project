import pandas as pd
from sklearn.preprocessing import StandardScaler

def feature_engineering(df):
    #One Hot Enconding [x]
    encode_cols = ['sex', 'region', 'smoker']
    df = pd.get_dummies(df, columns = encode_cols, drop_first=True)

    #Creating Interactions []
    df['bmi_smoker'] = df['bmi'] * df['smoker_yes']
    df['age_smoker'] = df['age'] * df["smoker_yes"]
    df['age_bmi'] = df['age'] * df['bmi']
    

    #Standard Scaling []
    num_cols = ['age', 'bmi', 'children', 'bmi_smoker', 'age_smoker', 'age_bmi']
    standard_scale = StandardScaler()
    df[num_cols] = standard_scale.fit_transform(df[num_cols])

    print('After Scaling', df.columns.tolist())


    return df
    