from flask import Flask, render_template
import pandas as pd

from models.segmentation import customer_segmentation
from models.churn_prediction import predict_churn
from models.purchase_prediction import purchase_prediction
from models.revenue_forecast import revenue_forecast
from models.clv_prediction import calculate_clv

app = Flask(__name__)

@app.route("/")
def dashboard():

    df = pd.read_csv("dataset/customers.csv")

    total_customers = len(df)

    total_revenue = df["Total_Spending"].sum()

    active_customers = len(
        df[df["Churn_Status"] == 0]
    )

    return render_template(
        "dashboard.html",
        total_customers=total_customers,
        total_revenue=total_revenue,
        active_customers=active_customers
    )

@app.route("/customers")
def customers():

    df = pd.read_csv("dataset/customers.csv")

    customers = df.to_dict(orient="records")

    return render_template(
        "customers.html",
        customers=customers
    )

@app.route("/segmentation")
def segmentation():

    df = customer_segmentation()

    data = df.to_dict(orient="records")

    return render_template(
        "segmentation.html",
        data=data
    )

@app.route("/churn")
def churn():

    df = predict_churn()

    data = df.to_dict(orient="records")

    return render_template(
        "churn.html",
        data=data
    )

@app.route("/purchase")
def purchase():

    df = purchase_prediction()

    data = df.to_dict(orient="records")

    return render_template(
        "purchase.html",
        data=data
    )

@app.route("/analytics")
def analytics():

    revenue = revenue_forecast()

    return render_template(
        "analytics.html",
        revenue=revenue
    )

@app.route("/reports")
def reports():

    clv = calculate_clv()

    data = clv.to_dict(orient="records")

    return render_template(
        "reports.html",
        data=data
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)