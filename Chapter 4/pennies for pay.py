day = int(input("Enter the number of days you worked"))
pennies = 1
total = 0
if day == 0:
    print("The total amount earned is $0.00")
else:
    for i in range(1, day + 1):
        pennies = 2 ** i
        pennies -= 1
    total = float(pennies / 100)
    print("The total amount earned is $ ", total)
