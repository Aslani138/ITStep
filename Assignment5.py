#დავალება 1

#Given list
myList = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]

# Adding the 3rd (index 2), 9th (index 8), and 14th (index 13) elements
result = myList[2] + myList[8] + myList[13]

# Printing the result
print(result)


#დავალება 2

import random

# Creating an empty list
numbers = []

# Filling the list with 10 random numbers
for i in range(10):
    numbers.append(random.randint(1, 100))

# Printing the list, minimum and maximum values
print("List of numbers:", numbers)
print("Minimum value:", min(numbers))
print("Maximum value:", max(numbers))


#დავალება 3

# Creating the list
myList = [43, '22', 12, 66, 210, ["hi"]]

# a. Prints an index of 210
index210 = myList.index(210)
print("Index of 210:", index210)

# b. Adds the text "hello" to the last element
myList[-1].append("hello")

# c. Deletes the element at the second index and prints the list
myList.pop(2)
print("ჩვენი სია მეორე ელემენტის წაშლის შემდეგ", myList)

# d. Create new list myList2 with value myList and clear myList
myList2 = myList.copy()
myList2.clear()

# Printing the lists
print("myList:", myList)
print("myList2:", myList2)


#დავალება 4

# Example matrices
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Adding corresponding elements
sumMatrix = []
for i in range(len(matrix1)):
    row_sum = []
    for j in range(len(matrix1[i])):
        row_sum.append(matrix1[i][j] + matrix2[i][j])
    sumMatrix.append(row_sum)

# Printing the result
print("Sum of the two matrices:")
for row in sumMatrix:
    print(row)


#დავალება 5

# Example 3x3 matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# transposition of the matrix
transposedMatrix = []
for i in range(len(matrix)):
    transposedRow = []
    for j in range(len(matrix[i])):
        transposedRow.append(matrix[j][i])
    transposedMatrix.append(transposedRow)

# Printing the original and transposed matrix
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposedMatrix:
    print(row)



