import os
import pandas as pd

def load_data(file_name: str) -> pd.DataFrame:
    '''
    Loads CSV data into a pandas Dataframe.

    Args:
        file_name (str): Path to the CSV file.
    
    Returns:
        pd.Dataframe: Loaded dataset.
    '''
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File not found: {file_name}")
    
    return pd.read_csv(file_name)