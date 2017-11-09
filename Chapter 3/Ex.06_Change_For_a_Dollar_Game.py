pennies = int(input("Enter the number of Pennies"))
nickel = int(input("Enter the number of Nickels"))
dime = int(input("Enter the number of Dimes"))
quarter = int(input("Enter the number of Quaters"))
total = (pennies + (nickel * 5) + (dime * 10) +(quarter * 25))
if total == 100:
    print("Congratulations You won the game")
else:
    print("You lost")
