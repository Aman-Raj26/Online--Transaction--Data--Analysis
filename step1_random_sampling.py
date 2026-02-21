import pandas as pd

# Load Original Dataset
data = pd.read_csv("upi_transactions_2024.csv")
print("Total Original Rows:", len(data))

# Select Random 3000 Records
random_3000 = data.sample(n=3000, random_state=42)
print("Random 3000 Rows Selected:", len(random_3000))

# Save New CSV
random_3000.to_csv("upi_random_3000.csv", index=False)
print("Random 3000 dataset saved successfully.")