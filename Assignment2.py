#დავალება 1

#Input a number from the user
number = int(input("შეიყვანეთ რიცხვი: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("even")
else:
    print("odd")


#დავალება 2

#Input text from the user
text = str(input("შეიყვანეთ ტექსტი: "))

# Check for each word and print the result
if "small" in text:
    print("small")
elif "tall" in text:
    print("tall")
elif "middle" in text:
    print("middle")
else:
    print("შეყვანილ ტექსტში სიტყვები 'small','middle' და 'tall' ვერ მოიძებნა")


#დავალება 3

# User input for the first number
firstNum = float(input("შეიყვანეთ პირველი რიცხვი: "))

# User input for the second number
secondNum = float(input("შეიყვანეთ მეორე რიცხვი: "))

# User input for the operator
operator = input("შეიყვანეთ ოპერატორი: ")

# Calculating and printing the result based on the operator
if operator == "+":
    result = firstNum + secondNum
elif operator == "-":
    result = firstNum - secondNum
elif operator == "*":
    result  = firstNum * secondNum
elif operator == "/":
    if secondNum != 0:
        result = firstNum / secondNum
    else:
        result = "ნულზე გაყოფა არ შეიძლება"
elif operator == "%":
    if secondNum != 0:
        result = firstNum % secondNum
    else:
        result = "ნულზე გაყოფა არ შეიძლება"
elif operator == "**":
    result = firstNum ** secondNum
elif operator == "//":
    if secondNum != 0:
        result = firstNum // secondNum
    else:
        result = "ნულზე გაყოფა არ შეიძლება"
else:
    result = "გამოიყენეთ მხოლოდ შემდეგი ოპერატორები: +, -, *, /, %, **, //"

print("Result: ", result)
