import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def predict_churn():

    df = pd.read_csv("dataset/customers.csv")

    X = df[[
        "Annual_Income",
        "Purchase_Frequency",
        "Total_Spending",
        "Last_Purchase_Days"
    ]]

    y = df["Churn_Status"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)

    df["Churn_Prediction"] = model.predict(X)

    return df