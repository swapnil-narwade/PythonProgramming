year = int(input("Enter the year you want to chaeck for leap year "))
if year % 100 ==0:
    if year % 400 == 0:
        print ("{} february has 29 days".format(year))
    elif year % 4 == 0:
        print (" year {} february has 29 days".format(year))
    else:
        print ("year {} february has 28 days".format(year))
elif year % 4 == 0:
    print (" year {} february has 29 days".format(year))
else:
    print ("year {} february has 28 days".format(year))

