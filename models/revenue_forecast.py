import pandas as pd

def revenue_forecast():

    df = pd.read_csv("dataset/customers.csv")

    current_revenue = df["Total_Spending"].sum()

    forecast = current_revenue * 1.15

    return {
        "current": current_revenue,
        "forecast": round(forecast, 2)
    }