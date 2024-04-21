import pandas as pd

# Loading Our Various CSV files
csv1 = pd.read_csv('merc.csv')
csv2 = pd.read_csv('bmw.csv')
csv3 = pd.read_csv('toyota.csv')
csv4 = pd.read_csv('vauxhall.csv')
csv5 = pd.read_csv('vw.csv')
csv6 = pd.read_csv('ford.csv')
csv7 = pd.read_csv('audi.csv')

# Here we are using the process Concatenate
concatenated_data = pd.concat([csv1, csv2, csv3, csv4, csv5, csv6, csv7], ignore_index=True)

# Save the concatenated data to a new CSV file
concatenated_data.to_csv('mergedcarfiles.csv', index=False)
