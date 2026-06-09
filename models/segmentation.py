import pandas as pd
from sklearn.cluster import KMeans

def customer_segmentation():

    df = pd.read_csv("dataset/customers.csv")

    X = df[[
        "Annual_Income",
        "Purchase_Frequency",
        "Total_Spending"
    ]]

    model = KMeans(n_clusters=4, random_state=42)

    df["Segment"] = model.fit_predict(X)

    return df