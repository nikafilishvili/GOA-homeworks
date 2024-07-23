#1
print("hello world")

#2
user = input("please enter: ")
print(user)

#3
#comment lines

#4
for i in range(10):
    print(i)

#7
def guess():
    #this is correct num
    correct_number = 7
    guessed_correctly = False
    #this is what person guessed
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == correct_number:
        #this is what to print if answer is correct
        print("Congratulations! You guessed the correct number.")
        guessed_correctly = True
    else:
        #this is what to print if answer in incorrect
        print("Wrong guess. Try again.")
guess()

#8
# def password():
#     correct_password = "password123"
#     password_entered = False
#     while not password_entered:
#         password = input("Enter the password: ")
#         if password == correct_password:
#             print("Password accepted. Access granted.")
#             password_entered = True
#         else:
#             print("Incorrect password. Please try again.")
# password()

#9
num = input("please enter number: ")
print(num + 5)
#this code is gona error because we need intenger to make plus and num is string

#10
age = 30
height = 1.89
name = "nika"
is_student = True

#11
a = 5
b = 10

c = a
a = b
b = c

#12
name = input("please enter your name: ")
age = int(input("please enter your age: "))
height = float(input("please enter your height: "))

#15
int = 12
float = 1.2
string = "hello"
boolean = True

#17
num = 11
print(type(num))

#18
num1 = 5
num2 = 10
print(num1 + num2)
print(num1 * num2)
print(num1 - num2)
print(num1 / num2)

#19
a = 2
b = 3
print(a > b)
print(a < b)
print(a == b)
print(a != b)

#20
num1 = 10
num2 = 26
print(num1 + num2)
print(num1 * num2)
print(num1 - num2)
print(num1 / num2)

#22
num = 2
print(num * num)

#26
str = str(int)
float = float(int)
int = int(float)

#30
int = int(string)

#31
print(5 < 10)

#32
print(10 > 5 or 6 < 8)
print(90 > 12 and 5 > 32)

#33
print(10 > 5)
print(10 < 5)
print(10 >= 5)
print(10 <= 5)
print(10 == 5)
print(10 != 5)

#34
if 10 > 20:
    print("correct")
else:
    print("incorrect")

#35
print(10 > 5 or 10 < 100)

#36
num1 = 9
num2 = 72
print(num1 + num2)
print(num1 * num2)
print(num1 - num2)
print(num1 / num2)

#37
num1 = 34
num2 = 69
print(num1 + num2)
print(num1 * num2)
print(num1 - num2)
print(num1 / num2)

#38
if 100 > 33:
    print("correct")
else:
    print("incorrect")

#39
if 100 > 33:
    print("correct")
else:
    print("incorrect")

#41
nums = [1, 2, 3, 4, 5]
print(nums)

#42
nums = [1, 2, 3, 4, 5]

nums.append(6)
nums.remove(5)
#43
