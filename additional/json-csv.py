import pandas as pd

# Read the JSON file
df = pd.read_json('dataset.json')

# Write the DataFrame to a CSV file
df.to_csv('dataset.csv', sep=';', index=False)
