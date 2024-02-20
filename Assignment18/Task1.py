def positive_check(func):
    def wrapper(n):
        if n < 0:
            raise ValueError("Number must be positive")
        result = func(n)
        print(result)
        return result
    return wrapper

@positive_check
def return_number(n):
    return n

# Example usage
try:
    return_number(10)  # This should print 10
    return_number(-5)  # This should raise ValueError
except ValueError as e:
    print(e)
