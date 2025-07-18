import pandas as pd

# Load the dataset
df = pd.read_csv('dataset/500_Person_Gender_Height_Weight_Index.csv')

# Display first few rows
print(df.head())

# Display column data types and null values
print(df.info())

# Display summary statistics
print(df.describe())