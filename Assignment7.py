#დავალება 1

def sum_of_numbers(numbers_list):
    return sum(numbers_list)

numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
print(sum_of_numbers(numbers))

#დავალება 2

def sum_of_digits(number):
    # Base case: if the number is less than 10, return the number itself
    if number < 10:
        return number
    else:
        # Recursive case: add the last digit to the sum of the remaining digits
        return number % 10 + sum_of_digits(number // 10)

test_number = 12345
print(sum_of_digits(test_number))

#დავალება 3

def reverse_string(s):
    # Base case: if the string is empty or has only one character, return the string itself
    if len(s) <= 1:
        return s
    else:
        # Recursive case: return the last character plus the reverse of the rest of the string
        return s[-1] + reverse_string(s[:-1])

# Testing the function with the string "Hello"
test_string = "Hello"
print(reverse_string(test_string))

#დავალება 4

def factorial(n):
    # Base case: if n is 0 or 1, the factorial is 1
    if n in [0, 1]:
        return 1
    else:
        # Recursive case: n factorial is n times (n-1) factorial
        return n * factorial(n - 1)

# Testing the function with a number, for example, 5
test_number = 5
print(factorial(test_number))


