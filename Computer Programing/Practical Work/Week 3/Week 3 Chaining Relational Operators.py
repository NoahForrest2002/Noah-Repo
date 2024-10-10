age = int(input("Input your age: "))
print(18 < age <= 65)

print(18 < age and age <= 65)
height =  int(input("Input your height: "))
weight = int(input("Input your weight: "))
print(100 < weight and weight < 200)

print(height > 131 and height < 160)
age = int(input("Input your age: "))
if age > 100:
    print("you are decrepit and elderly,")
    print("congrats g")
elif age > 80:
	print("you are fairly old")
elif age > 40:
	print("you are middle aged")
else:
	print("you are not very old - yet")
