#დავალება 1
def group_elements(list1, list2):
    return list(zip(list1, list2))

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
grouped_elements = group_elements(list1, list2)
print(grouped_elements)


#დავალება 2

# Lambda function to filter odd elements from a list
filter_odd = lambda lst: [x for x in lst if x % 2 != 0]

example_list = [1, 2, 3, 4, 5, 6, 7]
odd_elements = filter_odd(example_list)
print(odd_elements)


#დავალება 3

# Lambda function to check if a number is positive
is_positive = lambda x: x > 0

numbers = [-10, -5, 0, 3, 9, -2, 7]

# Using filter to apply the lambda function
positive_numbers = list(filter(is_positive, numbers))
print(positive_numbers)

#დავალება 4

# Lambda function to check if a string is a palindrome
is_palindrome = lambda s: s == s[::-1]

strings = ["radar", "hello", "level", "world", "racecar"]

# Using filter to apply the lambda function
palindromes = list(filter(is_palindrome, strings))
print(palindromes)

#დავალება 5

from functools import reduce

def product_of_list(lst):
    return reduce(lambda x, y: x * y, lst)

example_list = [1, 2, 3, 4, 5]
product_result = product_of_list(example_list)
print(product_result)

#დავალება 6

def filter_strings_by_ending(strings, ending):
    try:
        return list(filter(lambda s: s.endswith(ending), strings))
    except TypeError as e:
        # Handling the case where inputs are not of correct type
        return f"TypeError: {e}"

example_strings = ['hello', 'world', 'coding', 'nod']
example_ending = 'ing'
filtered_strings = filter_strings_by_ending(example_strings, example_ending)
print(filtered_strings)
