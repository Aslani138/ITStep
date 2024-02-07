#დავალება 1

# Create a text file and write 1000 lines to it
file_name = "sample_text_file.txt"

# Writing 1000 lines to the file
with open(file_name, "w") as file:
    for i in range(1, 1001):
        file.write(f"{i}\n")

# Now, read the file and count the number of lines
line_count = 0
with open(file_name, "r") as file:
    for line in file:
        line_count += 1

print("Number of lines in the file:", line_count)


#დავალება 2

# Define the file name
file_name = "custom_lines_text_file.txt"

# Numbers and their text names to be written on specific lines
lines_to_write = {
    2: "Two",
    8: "Eight",
    10: "Ten",
    13: "Thirteen",
    17: "Seventeen"
}

# Writing to the file
with open(file_name, "w") as file:
    for i in range(1, 18):
        if i in lines_to_write:
            file.write(f"{lines_to_write[i]}\n")
        else:
            file.write("\n")  # Write an empty line for other numbers


#დავალება 3
            
def merge_files(file1, file2, merged_file):
    # Open the first file and read its contents
    with open(file1, 'r') as f1:
        content1 = f1.read()

    # Open the second file and read its contents
    with open(file2, 'r') as f2:
        content2 = f2.read()

    # Merge the contents and write to the new file
    with open(merged_file, 'w') as mf:
        mf.write(content1 + "\n" + content2)

def read_and_print(file):
    # Read and print the contents of the file
    with open(file, 'r') as f:
        print(f.read())

file1 = 'path_to_first_file.txt'   # Replace with the actual file path
file2 = 'path_to_second_file.txt'  # Replace with the actual file path
merged_file = 'path_to_merged_file.txt'  # Replace with the desired path for the merged file

merge_files(file1, file2, merged_file)
read_and_print(merged_file)

