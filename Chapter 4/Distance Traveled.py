DISTANCE = 1
speed = int(input("Enter the speed of your vehicle : "))
hour = int(input("Enter the hours your vehicle traveled : "))
for i in range(0,hour):
    DISTANCE = speed * (i + 1)
    print("Distance traveled for hour", i + 1, "is : ", DISTANCE)
