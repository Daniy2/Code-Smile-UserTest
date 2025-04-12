import pandas as pd

def get_first_value():
    df = pd.DataFrame({
        "a": [10, 20, 30],
        "b": [40, 50, 60]
    })
    return df["a"][0]
