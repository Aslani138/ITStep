#დავალება 1

import random

def generate_and_sort():
    # Generate a list of 100 randomly generated elements
    random_list = [random.randint(1, 1000) for _ in range(100)]

    # Sort the list in ascending order using the sort() method
    random_list.sort()

    # Copy and sort the original list in descending order using the sorted() function
    sorted_descending = sorted(random_list, reverse=True)

    return random_list, sorted_descending

# Generate and sort the list
ascending_order, descending_order = generate_and_sort()

# Display the results
print(ascending_order[:10], descending_order[:10])


#დავალება 2

import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr, descending=False):
    n = len(arr)
    for i in range(n):
        index = i
        for j in range(i+1, n):
            if descending:
                if arr[j] > arr[index]:
                    index = j
            else:
                if arr[j] < arr[index]:
                    index = j
        arr[i], arr[index] = arr[index], arr[i]

    return arr

def generate_and_sort():
    # Generate a list of 100 randomly generated elements
    random_list = [random.randint(1, 1000) for _ in range(100)]

    # Copy the list for different sorting
    list_for_bubble_sort = random_list.copy()
    list_for_selection_sort = random_list.copy()

    # Sort the list in ascending order using bubble sort
    sorted_ascending = bubble_sort(list_for_bubble_sort)

    # Sort the list in descending order using selection sort
    sorted_descending = selection_sort(list_for_selection_sort, descending=True)

    return sorted_ascending, sorted_descending

# Generate and sort the list
ascending_order, descending_order = generate_and_sort()

# Display the results
print(ascending_order[:10], descending_order[:10])


