import pandas as pd
import matplotlib.pyplot as plt

# Load Cleaned Dataset
data = pd.read_csv("upi_cleaned_1000.csv")

print("Total Cleaned Records:", len(data))

# 1️⃣ Total Transaction Amount
if 'amount (inr)' in data.columns:
    total_amount = data['amount (inr)'].sum()
    print("Total Transaction Amount:", total_amount)

# 2️⃣ Transaction Type Distribution (Pie Chart)
if 'transaction type' in data.columns:
    type_counts = data['transaction type'].value_counts()

    plt.figure()
    plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')
    plt.title("Transaction Type Distribution")
    plt.show()

# 3️⃣ Monthly Transaction Trend (Bar Graph)
if 'timestamp' in data.columns:
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data['month'] = data['timestamp'].dt.month

    monthly_amount = data.groupby('month')['amount (inr)'].sum()

    plt.figure()
    monthly_amount.plot(kind='bar')
    plt.title("Monthly Transaction Amount")
    plt.xlabel("Month")
    plt.ylabel("Total Amount (INR)")

    plt.show()
