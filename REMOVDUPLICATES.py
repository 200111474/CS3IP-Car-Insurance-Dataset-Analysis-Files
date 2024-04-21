import pandas as pd

# Car Insurance dataset
data = pd.read_csv('Car_Insurance_Data.csv')

# Display information about duplicate records before removal
print("Car Insurance Duplicate Records Before Removal:")
print(data.duplicated().sum())

# Remove duplicate records
data_cleaned = data.drop_duplicates()

# Display information after removal
print("\nDuplicate Records After Removal:")
print(data_cleaned.duplicated().sum())

# Crash Data dataset
data = pd.read_csv('Crash_Data.csv')

print("Crash Duplicate Records Before Removal:")
print(data.duplicated().sum())

data_cleaned = data.drop_duplicates()

print("\nDuplicate Records After Removal:")
print(data_cleaned.duplicated().sum())

# Car Models dataset
data = pd.read_csv('mergedcarfiles.csv')

# Display information about duplicate records before removal
print("Car Models Duplicate Records Before Removal:")
print(data.duplicated().sum())

# Remove duplicate records
data_cleaned = data.drop_duplicates()

# Display information after removal
print("\nDuplicate Records After Removal:")
print(data_cleaned.duplicated().sum())


