length1 = int(input("Enter the length of first rectangle"))
width1 = int(input("Enter the width of first rectangle"))
length2 = int(input("Enter the length of second rectangle"))
width2 = int(input("Enter the width of first rectangle"))
area1 = length1 * width1
area2 = length2 * width2
if area1 < area2:
    print("Area of rectangle two is bigger")
elif area1 > area2:
    print("Area of rectangle one is bigger")
else: print("Area of both rectangle is same")
