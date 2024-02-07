#დავალება 1
num1 = int(input("შემოიტანეთ პირველი რიცხვი: "))
num2 = int(input("შემოიტანეთ მეორე რიცხვი: "))
num3 = int(input("შემოიტანეთ მესამე რიცხვი: "))

sum = num1 + num2 + num3
print("რიცხვების ჯამია: ", sum)


#დავალება 2
cubeLength = int(input("შემოიტანეთ კუბის გვერდის სიგრძე: "))

# Calculate volume (V) of the cube
cubeVolume = cubeLength ** 3
# Calculate surface area (S) of the cube
cubeSurfaceArea = 6 * cubeLength ** 2

print("კუბის მოცულობაა: ",cubeVolume, "ხოლო კუბის ზედაპირის ფართობი: ", cubeSurfaceArea)



#დავალება 3
monitor = float(input("შემოიტანეთ მონიტორის ფასი: "))
systemBlock = float(input("შემოიტანეთ სისტემური ბლოკის ფასი: "))
keyboard = float(input("შემოიტანეთ კლავიატურის ფასი ფასი: "))
mouse = float(input("შემოიტანეთ მაუსის ფასი: "))

computerPrice = monitor + systemBlock + keyboard + mouse

print("კომპიუტერის ფასია: ",computerPrice)