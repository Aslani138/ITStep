#დავალება 1

# Creating a variable squared_numbers that contains squared numbers from 1 to 10
squared_numbers = [i**2 for i in range(1, 11)]
print(squared_numbers)


#დავალება 2

def combine_tuples(tuple1, tuple2):
    # Combine tuples and remove duplicates
    combined_tuple = tuple(set(tuple1) | set(tuple2))

    # Find duplicated values
    duplicated_values = [value for value in tuple1 if value in tuple2]
    # Remove duplicates from duplicated_values
    duplicated_values = list(set(duplicated_values))

    return combined_tuple, duplicated_values

# Example usage
tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)

combined_tuple, duplicated_values = combine_tuples(tuple1, tuple2)
print(f"combined_tuple: {combined_tuple}")
print(f"duplicated_values: {duplicated_values}")
