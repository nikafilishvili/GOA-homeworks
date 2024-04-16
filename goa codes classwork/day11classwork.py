 
num1 = int(input("please enter number: "))
num2 = int(input("please enter number: "))
num3 = int(input("please enter number: "))
operation = input("please enter operation ,+, ,-, ,/, ,*,: ")

if operation == "+":
    print(num1 + num2 + num3)
elif operation == "-":
    print(num1 - num2 - num3)
elif operation == "/":
    print(num1 / num2 / num3)
elif operation == "*":
    print(num1 * num2 * num3)
else:
    print("operation you entered is not valid")