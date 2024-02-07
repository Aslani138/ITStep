import pandas as pd

# Load the organizations-100.csv file
org_file_path = './Assignment14/organizations-100.csv'
org_data = pd.read_csv(org_file_path)

# Filter the data to include only companies with SSL protected websites (HTTPS)
ssl_companies_data = org_data[org_data['Website'].str.startswith('https://')]

# Select only the required columns
ssl_companies_data = ssl_companies_data[['Organization Id', 'Name', 'Website', 'Industry', 'Number of employees']]

# Path for the new CSV file
ssl_companies_file_path = './Assignment14/ssl_companies.csv'

# Write the filtered data to the new CSV file
ssl_companies_data.to_csv(ssl_companies_file_path, index=False)
