import pandas as pd

# Load the Titanic dataset
titanic_file_path = './Assignment14/titanic.csv'
titanic_data = pd.read_csv(titanic_file_path)

# Filter the data to include only survivors
survivors_data = titanic_data[titanic_data['Survived'] == 1]

# Path for the new CSV file
survived_file_path = './Assignment14/survived.csv'

# Write the survivors data to the new CSV file
survivors_data.to_csv(survived_file_path, index=False)
