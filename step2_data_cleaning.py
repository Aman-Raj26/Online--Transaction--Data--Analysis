import pandas as pd

# Load Random 3000 Dataset
data = pd.read_csv("upi_random_3000.csv")

print("Initial Rows:", len(data))

# 1️⃣ Remove Duplicates
data = data.drop_duplicates()
print("After Removing Duplicates:", len(data))

# 2️⃣ Remove Missing Values
data = data.dropna()
print("After Removing Missing Values:", len(data))

# 3️⃣ Standardize Column Names
data.columns = data.columns.str.strip().str.lower()

# 4️⃣ Convert Timestamp to Datetime (if column exists)
if 'timestamp' in data.columns:
    data['timestamp'] = pd.to_datetime(data['timestamp'])

# 5️⃣ Remove Negative or Zero Amount
if 'amount (inr)' in data.columns:
    data = data[data['amount (inr)'] > 0]

print("After Removing Invalid Amounts:", len(data))

# 6️⃣ Select Final 1000 Cleaned Records
final_1000 = data.sample(n=1000, random_state=42)

print("Final Cleaned Dataset Rows:", len(final_1000))

# Save Final Cleaned Dataset
final_1000.to_csv("upi_cleaned_1000.csv", index=False)

print("Cleaned 1000 dataset saved successfully.")