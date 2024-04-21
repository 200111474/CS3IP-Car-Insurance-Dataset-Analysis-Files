import pandas as pd

# Crash dataset
data = pd.read_csv('Crash_Data.csv')

# Compute summary statistics
summary_stats = data.describe()

# Display the summary statistics
print("Crash Data Summary Statistics:")
print(summary_stats)

# Car Insurance dataset
data = pd.read_csv('Car_Insurance_Data.csv')

# Compute summary statistics
summary_stats = data.describe()

# Display the summary statistics
print("Insurance Data Summary Statistics:")
print(summary_stats)

# Car Model dataset
data = pd.read_csv('mergedcarfiles.csv')

# Compute summary statistics
summary_stats = data.describe()

# Display the summary statistics
print("Car Models Summary Statistics:")
print(summary_stats)



