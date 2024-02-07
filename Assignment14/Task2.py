import pandas as pd

# Load the organizations-100.csv file
org_file_path = './Assignment14/organizations-100.csv'
org_data = pd.read_csv(org_file_path)

# Sort the data based on 'Number of employees'
sorted_org_data = org_data.sort_values(by='Number of employees')

# Path for the new CSV file
sorted_file_path = './Assignment14/sorted.csv'  # Replace with the desired file path

# Write the sorted data to the new CSV file
sorted_org_data.to_csv(sorted_file_path, index=False)
