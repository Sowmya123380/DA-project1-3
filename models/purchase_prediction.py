import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def purchase_prediction():

    df = pd.read_csv("dataset/customers.csv")

    df["Future_Purchase"] = (
        df["Purchase_Frequency"] > 5
    ).astype(int)

    X = df[[
        "Annual_Income",
        "Purchase_Frequency",
        "Total_Spending"
    ]]

    y = df["Future_Purchase"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier()

    model.fit(X_train, y_train)

    df["Purchase_Prediction"] = model.predict(X)

    return df