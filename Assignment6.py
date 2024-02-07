# დავალება 1

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)


user_input1 = input("შემოყვანეთ პირველი სიტყვა: ")
user_input2 = input("შემოიყვანეთ მეორე სიტყვა: ")

if(is_anagram(user_input1,user_input2)):
    print("ანაგრამაა")
else:
    print("არ არის ანაგრამა")


# დავალება 2

def count_char_occurrences(input_string, char_to_count):   
    # Ensure char_to_count is a single character
    if len(char_to_count) != 1:
        print("გთხოვთ შემოიყვანოთ მხოლოდ 1 სიმბოლო")
    count = 0
    for char in input_string:
        if char == char_to_count:
            count += 1
    return count

user_input1 = input("შემოყვანეთ სიტყვა: ")
user_input2 = input("შემოიყვანეთ მოსაძებნი სიმბოლო: ")

print(count_char_occurrences(user_input1, user_input2))


# დავალება 3

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # first two Fibonacci numbers
    sequence = [0, 1]

    # Generate the remaining Fibonacci numbers up to n
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence

user_input1 = input("შემოიტანეთ რიცხვი ფიბონაჩის მიმდევრობისთვის: ")

print(generate_fibonacci(int(user_input1)))
