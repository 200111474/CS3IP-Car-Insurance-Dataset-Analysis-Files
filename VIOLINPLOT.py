import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Car Insurance dataset
data = pd.read_csv('Car_Insurance_Data.csv')

# Plot violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, palette='husl')
plt.title('Distribution of Variables')
plt.show()

# Car Models dataset
data = pd.read_csv('mergedcarfiles.csv')

plt.figure(figsize=(10, 6))
sns.violinplot(data=data, palette='husl')
plt.title('Distribution of Variables')
plt.show()
