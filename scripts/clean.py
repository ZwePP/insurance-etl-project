
def clean_data(df): #df : Dataframe
    print('🧹Cleaning Data.....')
    
    #Remove Duplicates [x]
    df = df.drop_duplicates()

    #Remove NA Values [x]
    df = df.dropna() 

    #Removing Outliers For Charges [x]
    lower_range, upper_range = calculate_iqr(df['charges'])

    df = df[(df['charges'] <= upper_range) & (df['charges'] >= lower_range)]
    return df



#IQR function
def calculate_iqr(df_column):
    q1 = df_column.quantile(0.25)
    q3 = df_column.quantile(0.75)
    IQR = q3 - q1
    bmi_lower = q1 - 1.5 * IQR
    bmi_upper = q3 + 1.5 * IQR
    return bmi_lower, bmi_upper




