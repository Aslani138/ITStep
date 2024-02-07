#დავალება 1

def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

input_sentence = "The wind howled and howled all night long"
print(word_frequency(input_sentence))


#დავალება 2

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter a mathematical operator (+, -, *, /): ")

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Cannot divide by zero"
    }

    if operator in operations:
        result = operations[operator](num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid operator")

calculator()
