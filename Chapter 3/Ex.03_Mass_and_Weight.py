weight = 0
mass = int(input("enter the mass"))
if mass > 1000:
    print("The Mass is too much")
elif mass < 10:
    print("The Mass is too less")
else:
    weight = mass * 9.8
    print("The weight is = ", weight)