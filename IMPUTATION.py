import pandas as pd

# Crash dataset
data = pd.read_csv('Crash_Data.csv')

# Display information about missing values
print("Missing Values Before Imputation:")
print(data.isnull().sum())

# Impute missing values with the mean
data_imputed = data.fillna(data.mean())

# Display information after Imputation
print("\nMissing Values After Imputation:")
print(data_imputed.isnull().sum())

# Insurance dataset
data = pd.read_csv('Car_Insurance_Data.csv')

print("Missing Values Before Imputation:")
print(data.isnull().sum())

data_imputed = data.fillna(data.mean())

print("\nMissing Values After Imputation:")
print(data_imputed.isnull().sum())


# Audi dataset
data = pd.read_csv('Audi.csv')

print("Missing Values Before Imputation:")
print(data.isnull().sum())

data_imputed = data.fillna(data.mean())

print("\nMissing Values After Imputation:")
print(data_imputed.isnull().sum())

# Loading BMW dataset
data = pd.read_csv('BMW.csv')

print("Missing Values Before Imputation:")
print(data.isnull().sum())

data_imputed = data.fillna(data.mean())

print("\nMissing Values After Imputation:")
print(data_imputed.isnull().sum())

# Loading Mercedes-Benz dataset
data = pd.read_csv('Merc.csv')

print("Missing Values Before Imputation:")
print(data.isnull().sum())

data_imputed = data.fillna(data.mean())

print("\nMissing Values After Imputation:")
print(data_imputed.isnull().sum())

# Loading Volkswagen dataset
data = pd.read_csv('vw.csv')

print("Missing Values Before Imputation:")
print(data.isnull().sum())

data_imputed = data.fillna(data.mean())

print("\nMissing Values After Imputation:")
print(data_imputed.isnull().sum())

# Loading Vauxhall dataset
data = pd.read_csv('Vauxhall.csv')

print("Missing Values Before Imputation:")
print(data.isnull().sum())

data_imputed = data.fillna(data.mean())

print("\nMissing Values After Imputation:")
print(data_imputed.isnull().sum())

# Loading Ford dataset
data = pd.read_csv('Ford.csv')

print("Missing Values Before Imputation:")
print(data.isnull().sum())

data_imputed = data.fillna(data.mean())

print("\nMissing Values After Imputation:")
print(data_imputed.isnull().sum())
