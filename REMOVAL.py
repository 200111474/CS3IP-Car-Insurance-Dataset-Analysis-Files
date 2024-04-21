import pandas as pd

# Audi dataset
data = pd.read_csv('Audi.csv')

# Display information about missing values before removal
print("Missing Values Before Removal:")
print(data.isnull().sum())

# Remove rows with missing values
data_cleaned = data.dropna()

# Display information after removal
print("\nMissing Values After Removal:")
print(data_cleaned.isnull().sum())

# BMW dataset
data = pd.read_csv('BMW.csv')

print("Missing Values Before Removal:")
print(data.isnull().sum())

data_cleaned = data.dropna()

print("\nMissing Values After Removal:")
print(data_cleaned.isnull().sum())

# Ford dataset
data = pd.read_csv('Ford.csv')

print("Missing Values Before Removal:")
print(data.isnull().sum())

data_cleaned = data.dropna()

print("\nMissing Values After Removal:")
print(data_cleaned.isnull().sum())

# Mercedes-Benz dataset
data = pd.read_csv('Merc.csv')

print("Missing Values Before Removal:")
print(data.isnull().sum())

data_cleaned = data.dropna()

print("\nMissing Values After Removal:")
print(data_cleaned.isnull().sum())

# Toyota dataset
data = pd.read_csv('toyota.csv')

print("Missing Values Before Removal:")
print(data.isnull().sum())

data_cleaned = data.dropna()

print("\nMissing Values After Removal:")
print(data_cleaned.isnull().sum())

# Vauxhall dataset
data = pd.read_csv('vauxhall.csv')

print("Missing Values Before Removal:")
print(data.isnull().sum())

data_cleaned = data.dropna()

print("\nMissing Values After Removal:")
print(data_cleaned.isnull().sum())

# Volkswagen dataset
data = pd.read_csv('vw.csv')

print("Missing Values Before Removal:")
print(data.isnull().sum())

data_cleaned = data.dropna()

print("\nMissing Values After Removal:")
print(data_cleaned.isnull().sum())

# Crash dataset
data = pd.read_csv('Crash_Data.csv')

print("Missing Values Before Removal:")
print(data.isnull().sum())

data_cleaned = data.dropna()

print("\nMissing Values After Removal:")
print(data_cleaned.isnull().sum())

# Car Insurance dataset
data = pd.read_csv('Car_Insurance_Data.csv')

print("Missing Values Before Removal:")
print(data.isnull().sum())

data_cleaned = data.dropna()

print("\nMissing Values After Removal:")
print(data_cleaned.isnull().sum())



