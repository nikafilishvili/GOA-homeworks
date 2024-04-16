
#1

academy = input("please enter which programming academy are you learning: ")

if academy == "GOA":
    print("correct")
else:
    print("wrong choice")

#2

price = int(input("please neter price of item you want to buy: "))
budget = int(input("please enter your budget: "))

if budget >= price:
    print("budget is enough")
else:
    print(price - budget)

#3

user_num = int(input("please enter number: "))

if user_num >= 5:
    print(user_num * 2)
else:
    print(user_num * 4)

#4

ticket_price = 10
ticket_num = int(input("please enter how many tickets do you want: "))

if ticket_num < 5:
    print(ticket_num * 10)
else:
    print(ticket_num * 7)

#5

num1 = int(input("please enter number: "))
num2 = int(input("please neter number: "))
operation = input("please enter which operations do you want to do from this four  +, -, *, /. : ")
                
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)