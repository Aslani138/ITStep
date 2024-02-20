class PositiveCheck:
    def __init__(self, func):
        self.func = func

    def __call__(self, n):
        if n < 0:
            raise ValueError("Number must be positive")
        result = self.func(n)
        print(result)
        return result

def return_number(n):
    return n

# Applying the functor
positive_return_number = PositiveCheck(return_number)

# Example usage
try:
    positive_return_number(10)  # This should print 10
    positive_return_number(-5)  # This should raise ValueError
except ValueError as e:
    print(e)
