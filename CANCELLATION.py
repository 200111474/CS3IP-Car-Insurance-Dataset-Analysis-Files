import pandas as pd
import matplotlib.pyplot as plt

# Car Insurance data
data = pd.read_csv('Car_Insurance_Data.csv')

# Creating a bar chart
plt.figure(figsize=(10, 6))
plt.bar(data['OFFENSES'], data['SPEEDING_VIOLATIONS'], color='blue')
plt.xlabel('Reasons for Cancellation')
plt.ylabel('Number of Cancellations')
plt.title('Car Insurance Policy Cancellations by Reason')
plt.xticks(rotation=45)
plt.tight_layout()

# Show
plt.show()
