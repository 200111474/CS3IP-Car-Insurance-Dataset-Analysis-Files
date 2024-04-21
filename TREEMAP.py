import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Merged Car Makes/Models file
data = pd.read_csv('mergedcarfiles.csv')

# Model and Year of dataset
model_count = data['model'].value_counts().reset_index()
model_count.columns = ['model', 'year']

# TreeMap Construction
plt.figure(figsize=(10, 8))
squarify.plot(sizes=model_count['year'], label=model_count['model'], alpha=0.8)

# Title
plt.title("Popularity of Car Models")
plt.axis('off')

# Show the plot
plt.show()
