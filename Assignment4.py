#დავალება 1

userInput = input("შემოიყვანეთ სიტყვა რომ შემოწმდეს არის თუარა პალინდრომი: ")

#მოვაშოროთ სფეისები და გადავიყვანოთ lowercase-ში
userInput = userInput.replace(" ", "").lower()

#შევამოწმოთ არის თუარა პალინდრომი
if userInput == userInput[::-1]:
    print("შემოყვანილი ტექსტი პალინდრომია")
else:
    print("შემოყვანილი სიტყვა არ არის პალინდრომი")


#დავალება 2

text = input("შემოიყვანეთ ტექსტი: ")

#გადავიყვანო თითოეული ჩერექთერი ASCII ს მნიშვნელობებში და დავპრინტოთ
for char in text:  
    print(ord(char), end=" ")