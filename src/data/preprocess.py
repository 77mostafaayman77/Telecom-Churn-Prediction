import pandas as pd

def preprocess_data(df: pd.DataFrame, target_col: str = 'Churn') -> pd.DataFrame:
    """
    Basic cleaning for Telco churn.
    - trim column names
    - drop obvious ID cols
    - fix TotalCharges to numeric
    - map target Churn to 0/1 if needed
    - simple NA handling
    """
    # columns names
    df.columns = df.columns.str.strip()
    
    # drop ids if present
    for col in ['customerID','CustomerID','customer_id']:
        if col in df.columns:
            df = df.drop(col,axis=1)

    # target to 0/1 if it's Yes/No
    if target_col in df.columns and df[target_col].dtype == 'object':
        df[target_col] = df[target_col].str.strip().map({'No': 0 ,'Yes': 1})
    
    # convert TotalCharges to numeric
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # SeniorCitizen should be 0/1 ints if present
    if 'SeniorCitizen' in df.columns:
        mode_value = df['SeniorCitizen'].mode()[0]
        df['SeniorCitizen'] = df['SeniorCitizen'].fillna(mode_value).astype(int)
    
    # simple NA strategy:
    # - numeric: fill with 0
    # - others: leave for encoders to handle (get_dummies ignores NaN safely)
    num_cols = df.select_dtypes(include=['number']).columns
    df[num_cols] = df[num_cols].fillna(0)

    return df