import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Crash Data dataset
data = pd.read_csv('Crash_Data.csv')

# Select only numeric columns
numeric_data = data.select_dtypes(include=['number'])

# Correlation matrix
correlation_matrix = numeric_data.corr()

# Making a Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Car Insurance dataset
data = pd.read_csv('Car_Insurance_Data.csv')

# Select only numeric columns
numeric_data = data.select_dtypes(include=['number'])

# Correlation matrix
correlation_matrix = numeric_data.corr()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()


# Car Makes/Models Merged dataset
data = pd.read_csv('mergedcarfiles.csv')

# Select only numeric columns
numeric_data = data.select_dtypes(include=['number'])

# Correlation matrix
correlation_matrix = numeric_data.corr()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

