import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Crash dataset
data = pd.read_csv('Crash_Data.csv')

# Select only numeric columns
numeric_data = data.select_dtypes(include=['number'])

# Set up matplotlib 
fig, axes = plt.subplots(nrows=len(numeric_data.columns), ncols=2, figsize=(12, 6 * len(numeric_data.columns)))
plt.subplots_adjust(hspace=0.5)

for i, col in enumerate(numeric_data.columns):
    # Histogram
    sns.histplot(data[col], ax=axes[i, 0], kde=True)
    axes[i, 0].set_title(f'Histogram of {col}')
    axes[i, 0].set_xlabel(col)
    axes[i, 0].set_ylabel('Frequency')

    # Box plot
    sns.boxplot(data[col], ax=axes[i, 1])
    axes[i, 1].set_title(f'Box Plot of {col}')
    axes[i, 1].set_xlabel(col)

# Show the plots
plt.tight_layout()
plt.show()

# Insurance dataset
data = pd.read_csv('Car_Insurance_Data.csv')

numeric_data = data.select_dtypes(include=['number'])

fig, axes = plt.subplots(nrows=len(numeric_data.columns), ncols=2, figsize=(12, 6 * len(numeric_data.columns)))
plt.subplots_adjust(hspace=0.5)

for i, col in enumerate(numeric_data.columns):
    # Histogram
    sns.histplot(data[col], ax=axes[i, 0], kde=True)
    axes[i, 0].set_title(f'Histogram of {col}')
    axes[i, 0].set_xlabel(col)
    axes[i, 0].set_ylabel('Frequency')

    # Box plot
    sns.boxplot(data[col], ax=axes[i, 1])
    axes[i, 1].set_title(f'Box Plot of {col}')
    axes[i, 1].set_xlabel(col)

# Show the plots
plt.tight_layout()
plt.show()
