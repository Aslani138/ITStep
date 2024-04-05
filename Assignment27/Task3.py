import asyncio

async def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

async def square_if_even(number):
    """Return the square of the number if it is even, otherwise None."""
    if await is_even(number):
        return number * number
    return None

async def main():
    # Create a list of numbers to test
    numbers = [1, 2, 3, 4, 5, 6]

    # Using asyncio.gather to run square_if_even for all numbers concurrently
    results = await asyncio.gather(*(square_if_even(number) for number in numbers))

    print(results)

# Run the main function
asyncio.run(main())
