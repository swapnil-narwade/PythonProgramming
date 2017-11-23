def maximum(num1,num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        a = "none, Both are same"
        return a


def main():
    print("Welcome to the max of two")
    val1 = int(input("Enter the value one"))
    val2 = int(input("Enter the value two"))
    answer = maximum(val1, val2)
    if answer == val1:
        print("Maximum of two is value one", val1)
    elif answer == val2:
        print("Maximum of two is value two", val2)
    else:
        print("maximum of two is ", answer)


main()
