weigth = int(input("Enter the weight of shipping packet"))
charge = 0
if weigth <= 2 and weigth > 0:
    charge = weigth * 1.10
    print("Total charge is = ",charge)
elif weigth <= 6 and weigth > 2:
    charge = weigth * 2.20
    print("Total charge is = ",charge)
elif weigth <= 10 and weigth > 6:
    charge = weigth * 3.70
    print("Total charge is = ",charge)
elif weigth > 10:
    charge = weigth * 3.80
    print("Total charge is = ",charge)
else:
    print ("Weight can not be negative or zero")
