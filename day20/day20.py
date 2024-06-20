# #1 
# def nums():
#     for i in range(20 + 1):
#         print(i)
# nums()

# #2
# def natural_nums():
#     for i in range(1, 10 + 1):
#         print(i)
# natural_nums()

# #3
# def nums():
#     for i in range(100 + 1):
#         if i % 2 == 0:
#             print(i)          
#     for i in range(100 + 1):
#         if i % 2 != 0:
#             print(i)
# nums()

# #4
# def sum_nums():
#     num = int(input("please enter number: "))
#     sum = 0
#     for i in range(1, num + 1):
#         sum += i
#         print(sum)
# sum_nums()

# #5 
# def nums():
#     for i in range(1, 50 + 1):
#         if i % 5 == 0:
#             print(i)
# nums()

# #6
# def even_nums():
#     even_nums = 2
# while even_nums <= 20:
#     print(even_nums)
#     even_nums += 2
# even_nums()

# #7
# def sum_numbers():
#     num = 1
# sum = 0
# while sum_numbers <= 10:
#     sum += sum_numbers
#     sum_numbers += 1
# sum_numbers()

# #8
# def guess():
#     correct_number = 7
#     guessed_correctly = False
#     guess = int(input("Guess the number between 1 and 10: "))
#     if guess == correct_number:
#         print("Congratulations! You guessed the correct number.")
#         guessed_correctly = True
#     else:
#         print("Wrong guess. Try again.")
# guess()

# #9
# def list():
#     numbers = [1, 2, 3, 4, 5]
#     index = 0
#     while index < len(numbers):
#         numbers[index] *= 2
#     index += 1
#     print(numbers)
# list()

#10
def password():
    correct_password = "password123"
    password_entered = False
    while not password_entered:
        password = input("Enter the password: ")
        if password == correct_password:
            print("Password accepted. Access granted.")
            password_entered = True
        else:
            print("Incorrect password. Please try again.")
password()
