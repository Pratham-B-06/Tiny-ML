import pandas as pd

# Load dataset
df = pd.read_csv("C:\Workshop\TinyML-Workshop\Data_Logger\dataset.csv")

# Count duplicate rows
duplicate_count = df.duplicated().sum()
print("Duplicate Rows:", duplicate_count)

# Remove duplicates
df = df.drop_duplicates()

# Verify dataset
print("New Shape:", df.shape)