
#1

academy = input("please neter which programming academy are you learning: ")

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