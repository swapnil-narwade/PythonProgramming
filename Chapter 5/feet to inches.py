def feet_to_inches(foot):
    return foot * 12


def main():
    print("Feet to Inches")
    foots = int(input("Enter the number of feet you want : "))
    total = feet_to_inches(foots)
    print("Number of inches : ", total)
    print("Bye")


main()
