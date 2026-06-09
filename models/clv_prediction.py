import pandas as pd

def calculate_clv():

    df = pd.read_csv("dataset/customers.csv")

    df["CLV"] = (
        df["Purchase_Frequency"]
        * df["Total_Spending"]
    )

    return df