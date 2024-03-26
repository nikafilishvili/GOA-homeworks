
#1

c = float(input("please neter temperature: "))
f = ((c * 1.8) + 32)

#2

age = int(input("please enter your age: "))
print(age < 20 and age > 12)

#3

length = float(input("please enter legth of rectangular: "))
width = float(input("please enter width of rectangular: "))
area = length * width
print(area)

#4

num = int(input("please enter number: "))
print(num > 100 and num % 9 == 0)

#5

print(100 > 110 and 30 < 3)
print(60 < 30 and 100 > 30)
print(200 > 135 and 100 < 67)
print(155 > 35 and 65 < 134)

print(176 > 200 or 32 < 12)
print(200 < 34 or 100 > 66)
print(189 > 79 or 200 < 55)
print(199 > 36 or 300 < 679)