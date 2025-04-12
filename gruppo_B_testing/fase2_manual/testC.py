import pandas as pd

def join_dataframes():
    df1 = pd.DataFrame({"id": [1, 2], "value": ["a", "b"]})
    df2 = pd.DataFrame({"id": [1, 2], "other": ["x", "y"]})
    merged = df1.merge(df2)
    return merged
