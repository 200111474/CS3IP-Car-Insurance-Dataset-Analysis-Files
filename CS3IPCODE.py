import pandas as pd

# Load Audi dataset
audi_data = pd.read_csv('audi.csv')
print("Audi Car Dataset:")
print(audi_data.head())

# Load BMW dataset
bmw_data = pd.read_csv('bmw.csv')
print("BMW Car Dataset:")
print(bmw_data.head())

# Load Ford dataset
ford_data = pd.read_csv('ford.csv')
print("Ford Car Dataset:")
print(ford_data.head())

# Load Mercedes-Benz dataset
merc_data = pd.read_csv('merc.csv')
print("Mercedes-Benz Car Dataset:")
print(merc_data.head())

# Load Toyota dataset
toyota_data = pd.read_csv('toyota.csv')
print("Toyota Car Dataset:")
print(toyota_data.head())

# Load Vauxhall dataset
vauxhall_data = pd.read_csv('vauxhall.csv')
print("Vauxhall Car Dataset:")
print(vauxhall_data.head())

# Load Volkswagen dataset
vw_data = pd.read_csv('vw.csv')
print("Volkswagen Car Dataset:")
print(vw_data.head())

# Load insurance dataset
insurance_data = pd.read_csv('Car_Insurance_Data.csv')
print("\nInsurance Dataset:")
print(insurance_data.head())

# Load crash dataset
crash_data = pd.read_csv('Crash_Data.csv')
print("\nCrash Dataset:")
print(crash_data.head())

# Category Variables in Audi Car Dataset
print("\nCategory Variables in Audi Car Dataset:")
for column in audi_data.select_dtypes(include='object').columns:
    print(audi_data[column].value_counts())

# Category Variables in BMW Car Dataset
print("\nCategory Variables in BMW Car Dataset:")
for column in bmw_data.select_dtypes(include='object').columns:
    print(bmw_data[column].value_counts())

# Category Variables in Ford Car Dataset
print("\nCategory Variables in Ford Car Dataset:")
for column in ford_data.select_dtypes(include='object').columns:
    print(ford_data[column].value_counts())

# Category Variables in Mercedees-Benz Car Dataset
print("\nCategory Variables in Mercedes-Benz Car Dataset:")
for column in merc_data.select_dtypes(include='object').columns:
    print(merc_data[column].value_counts())

# Category Variables in Toyota Car Dataset
print("\nCategory Variables in Toyota Car Dataset:")
for column in toyota_data.select_dtypes(include='object').columns:
    print(toyota_data[column].value_counts())

# Category Variables in Vauxhall Car Dataset
print("\nCategory Variables in Vauxhall Car Dataset:")
for column in vauxhall_data.select_dtypes(include='object').columns:
    print(vauxhall_data[column].value_counts())

# Category Variables in Volkswagen Car Dataset
print("\nCategory Variables in Volkswagen Car Dataset:")
for column in vw_data.select_dtypes(include='object').columns:
    print(vw_data[column].value_counts())

# Descriptive statistics for Crash Dataset
print("Descriptive Statistics for Crash Dataset:")
print(crash_data.describe())

# Category Variables in Crash Dataset
print("\nCategory Variables in Crash Dataset:")
for column in crash_data.select_dtypes(include='object').columns:
    print(crash_data[column].value_counts())

# Descriptive statistics for Insurance Dataset
print("Descriptive Statistics for Insurance Dataset:")
print(insurance_data.describe())

# Category Variables in Insurance Dataset
print("\nCategory Variables in Insurance Dataset:")
for column in insurance_data.select_dtypes(include='object').columns:
    print(insurance_data[column].value_counts())

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

# Car Make Model data
car_data = pd.read_csv('mergedcarfiles.csv')

# Separate features and target variable
X = car_data.drop('price', axis=1)
y = car_data['price']

# ENCODING
X = pd.get_dummies(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Regressor Model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)



# Feature importances
importances = rf_model.feature_importances_

# Names of the features
feature_names = X.columns

# Sort feature importances
indices = importances.argsort()[::-1]

# Plot feature importances
plt.figure(figsize=(10, 6))
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), feature_names[indices], rotation=90)
plt.tight_layout()
plt.show()

import seaborn as sns
import numpy as np

# Car Insurance Dataset
data = pd.read_csv('Car_Insurance_Data.csv')

# Randomly select two columns for the scatter plot
columns = np.random.choice(data.columns, size=2, replace=False)

# Plot the scatter plot
sns.scatterplot(x=columns[0], y=columns[1], data=data)

