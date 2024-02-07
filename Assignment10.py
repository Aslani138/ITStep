#დავალება 1

import random

# Function to generate a list of 100 random numbers
def generate_random_numbers(n=100):
    return [random.randint(1, 1000) for _ in range(n)]

# Linear Search Function
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # Return the index of the found element
    return -1  # Return -1 if the element is not found

# Bubble Sort Function
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# Binary Search Function
def binary_search(sorted_lst, target):
    left, right = 0, len(sorted_lst) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sorted_lst[mid] == target:
            return mid
        elif sorted_lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
random_numbers = generate_random_numbers()
print("Random Numbers:", random_numbers)

# Linear Search
search_target = 500  # Example target number for search
linear_result = linear_search(random_numbers, search_target)
print(f"Linear Search: Element {search_target} found at index {linear_result}")

# Sorting and Binary Search
sorted_numbers = bubble_sort(random_numbers)
print("Sorted Numbers:", sorted_numbers)
binary_result = binary_search(sorted_numbers, search_target)
print(f"Binary Search: Element {search_target} found at index {binary_result}")


#დავალება 2

# Lambda function to check if a number is a multiple of three
is_multiple_of_three = lambda x: x % 3 == 0

def find_indices(lst, condition):
    indices = []
    for i, value in enumerate(lst):
        if condition(value):
            indices.append(i)
    return indices

# Example usage
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find indices of multiples of three in the example list
indices_of_multiples = find_indices(example_list, is_multiple_of_three)

print("Indices of multiples of three:", indices_of_multiples)
