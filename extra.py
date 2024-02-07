#დავალება 1

def largest_divisor(number):
    # Starting from the number - 1 and going downwards
    for i in range(number - 1, 0, -1):
        # If i is a divisor of number
        if number % i == 0:
            return i
    return None

# Taking user input
number = int(input("Enter a number: "))
print("Largest divisor of", number, "is:", largest_divisor(number))

#დავალება 2

def print_operations(max_number):
    # Header for the table
    print(f"{'x':^3} | {'x^2':^5} | {'x^10':^20} | {'x^x':^30}")
    print("-" * 63)
    
    # Iterate through numbers from 1 to max_number
    for x in range(1, max_number + 1):
        x_squared = x ** 2
        x_tenth = x ** 10
        x_to_the_x = x ** x
        print(f"{x:^3} | {x_squared:^5} | {x_tenth:^20} | {x_to_the_x:^30}")

print_operations(15)

#დავალება 3

from datetime import datetime
import time

while True:
    time_now = datetime.now()
    print(f"\rCurrent time: {time_now.strftime('%Y-%m-%d %H:%M:%S')}", end='')
    time.sleep(1)  # Sleep for 1 second before updating the time again

#დავალება 4

def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Find the position in 0-25
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            # Same as above, but with lowercase characters
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's neither, just add the character as it is
        else:
            encrypted_text += char

    return encrypted_text

# Taking user input
text = input("Enter a string to encrypt: ")
shift = int(input("Enter the number of shifts for the cipher: "))

# Encrypting the string using the Caesar cipher
encrypted = caesar_cipher(text, shift)

# Printing the encrypted string
print("Encrypted string:", encrypted)


#დავალება 5

def is_leap_year(year):
    # Check if the year is a multiple of 4 but not a multiple of 100,
    # or if it's a multiple of 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Replace 2024 with the year you want to check
year = 2024

if is_leap_year(year):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")


#დავალება 6

def check_prime_and_print_divisors(number):
    # List to store divisors
    divisors = []

    # Check for divisors of the number
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)

    # If no divisors found, it's a prime number
    if not divisors:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number. Its divisors are: {divisors}")

# Taking user input
num = int(input("Enter a number: "))

# Running the function
check_prime_and_print_divisors(num)

#დავალება 7

def remove_duplicates(lst):
    return list(set(lst))

# Example usage
example_list = [1, 2, 2, 3, 3, 4, 5, 5, 6]
print("Original list:", example_list)
print("List without duplicates:", remove_duplicates(example_list))

#დავალება 8

def is_monotonic(lst):
    if all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)):
        return "List is monotonic. Sorted list (ascending): " + str(sorted(lst))
    elif all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)):
        return "List is monotonic. Sorted list (descending): " + str(sorted(lst, reverse=True))
    else:
        return "List is not monotonic."

# Example usage
example_list = [1, 2, 3, 4, 5]
print(is_monotonic(example_list))

example_list2 = [5, 4, 3, 2, 1]
print(is_monotonic(example_list2))

example_list3 = [1, 3, 2, 4, 5]
print(is_monotonic(example_list3))

#დავალება 9

def reverse_case(lst):
    return [s.swapcase() for s in lst]

# Example usage
example_list = ["Green", "Blue", "rED"]
print(reverse_case(example_list))

#დავალება 10

import random

def rock_paper_scissors():
    # Define the possible choices
    choices = ["rock", "paper", "scissors"]

    # Get the user's choice
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    # Get the computer's random choice
    computer_choice = random.choice(choices)

    print(f"Computer chose {computer_choice}.")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") \
        or (user_choice == "paper" and computer_choice == "rock") \
        or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Example usage
rock_paper_scissors()


#დავალება 11

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for _ in range(9):
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column to place your mark (0-2): ").split())
            if board[row][col] != " ":
                print("Position already taken. Please try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers separated by space (0-2).")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a tie!")

# Run the game
tic_tac_toe()











