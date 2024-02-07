#დავალება 1

number = int(input("შემოიყვანეთ რიცხვი: "))

if number > 0:
    while number > 0:
        print(number, end=", ")
        number -= 1
elif number == 0:
    print(number)
else:
    while number < 0:
        print(number, end=", ")
        number += 1


#დავალება 2

totalSum = 0

while True:
    userInput = input("შემოიყვანეთ რიცხვები და ბოლოს დაწერეთ 'sum' რომ გამოისახოს მათი ჯამი: ")
    if userInput == "sum":
        print(totalSum)
        break
    userInput = float(userInput)
    if userInput > 0:
        totalSum += userInput


#დავალება 3

import random

lives = 10

# Ask user to define the interval
lowerBound = int(input("შემოიყვანეთ ქვედა ზღვარი: "))
upperBound = int(input("შემოიყვანეთ ზედა ზღვარი: "))

# Generate a random number in the given interval
numberToGuess = random.randint(lowerBound, upperBound)

print(f"გამოიცანით რიცხვი {lowerBound}-დან {upperBound}-მდე შუალედში. შენ გაქვს {lives} ცდა.")

while lives > 0:
    guess = int(input("Enter your guess: "))

    if guess == numberToGuess:
        print("გილოცავ შენ გაიმარჯვე!")
        break
    elif guess < numberToGuess:
        lives -= 1
        print(f"შეიყვანეთ უფრო მაღალი რიცხვი, შენ დაგრჩა {lives} ცდა ")
    else:
        lives -= 1
        print(f"შეიყვანეთ უფრო დაბალი რიცხვი, შენ დაგრჩა {lives} ცდა ")
    if lives == 0:
        print("სამწუხაროდ შენ დამარცხდი")