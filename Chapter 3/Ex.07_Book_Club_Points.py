book = int(input("Enter the number of books purchased this month"))
if book == 0:
    print("Total points are = 0")
elif book == 1:
    print("Total points are = 5")
elif book == 2:
    print("Total points are = 15")
elif book == 3:
    print("Total points are 30")
elif book == 4:
    print("Total points are 60")
else:
    print("Enter the correct book Purchase number")
