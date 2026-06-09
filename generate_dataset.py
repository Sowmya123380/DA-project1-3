import pandas as pd
import random

data = []

locations = ["Hyderabad", "Bangalore", "Chennai", "Mumbai", "Delhi"]
categories = ["Electronics", "Fashion", "Books", "Home", "Sports"]
membership = ["Gold", "Silver", "Platinum"]

for i in range(1, 101):
    age = random.randint(18, 65)
    income = random.randint(20000, 150000)
    frequency = random.randint(1, 20)
    spending = random.randint(1000, 100000)
    last_days = random.randint(1, 180)

    churn = 1 if last_days > 90 else 0

    data.append([
        f"CUST{i:03}",
        age,
        random.choice(["Male", "Female"]),
        random.choice(locations),
        income,
        frequency,
        spending,
        last_days,
        random.choice(membership),
        churn,
        random.choice(categories)
    ])

df = pd.DataFrame(data, columns=[
    "Customer_ID",
    "Age",
    "Gender",
    "Location",
    "Annual_Income",
    "Purchase_Frequency",
    "Total_Spending",
    "Last_Purchase_Days",
    "Membership_Status",
    "Churn_Status",
    "Preferred_Product_Category"
])

df.to_csv("dataset/customers.csv", index=False)

print("Dataset Created Successfully")