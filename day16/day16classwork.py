anime = ["naruto", "haikyu", "bluelock", "jujutsukaisen", "demonslayer"]
favAnime = (anime[2])
print(favAnime)



#შევქმენი ცვლადი
cars = []

#5 ჯერ გავუშვით ინფუთი
for i in range(5):
    car = input("please enter your car name: ")

#შემოტანილი ელემენტები გადავიტანეთ cars ცვლადში
    cars.append(car)

#დავპრინტეთ ცვლადი
print(cars)

#შევცვალე 0 ინდექსის მნიშვნელობა
cars[0] = car

#ამოვშალეთ 4 იდექსის მნიშვნელობა
cars.pop(4)

#დავპრინტეთ
print(cars)

