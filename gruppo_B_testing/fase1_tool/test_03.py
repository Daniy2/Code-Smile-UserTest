import pandas as pd

def update_column():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    for index, row in df.iterrows():
        df.loc[index, "a"] = row["b"] + 1
    return df
