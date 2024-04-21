import pandas as pd
import matplotlib.pyplot as plt

# Crash dataset
crash_data = pd.read_csv('Crash_Data.csv')

# Filter out only the categorical variables
categorical_columns = crash_data.select_dtypes(include=['object']).columns

# Plot bar charts for each categorical variable
for col in categorical_columns:
# Get value counts
    value_counts = crash_data[col].value_counts()
    
# Plotting
    plt.figure(figsize=(8, 6))
    value_counts.plot(kind='bar', color='skyblue')
    plt.title(f'Frequency Distribution of {col}')
    plt.xlabel('Categories')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.tight_layout()
    plt.show()

# Crash dataset
crash_data = pd.read_csv('Crash_Data.csv')

# Filter
categorical_columns = crash_data.select_dtypes(include=['object']).columns

# Plot pie charts 
for col in categorical_columns:

    value_counts = crash_data[col].value_counts()
    
    # Plotting
    plt.figure(figsize=(8, 6))
    plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Percentage Distribution of {col}')
    plt.axis('equal')  
    plt.tight_layout()
    plt.show()

