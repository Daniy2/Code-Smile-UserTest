import pandas as pd

def load_data():
    df = pd.read_csv("data.csv")
    return df

def create_dataframe():
    df2 = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    return df2
