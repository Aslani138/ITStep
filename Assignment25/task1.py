import json
import threading
import os

# Function to create a JSON file with sample data
def create_json_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)

# Function to parse a JSON file and print its contents
def parse_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print(f"File: {file_name}\nData: {data}\n")

# Create a few sample JSON files
sample_data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
for i in range(3):
    create_json_file(f'sample_{i}.json', sample_data[i])

# Parse each file in a separate thread
threads = []
for i in range(3):
    file_name = f'sample_{i}.json'
    thread = threading.Thread(target=parse_json_file, args=(file_name,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Clean up: Remove the created files (optional)
for i in range(3):
    os.remove(f'sample_{i}.json')
