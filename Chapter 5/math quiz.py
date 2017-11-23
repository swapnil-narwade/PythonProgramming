import random


def add(num1, num2):
    return num1 + num2


def main():
    print("Welcome to math quiz")
    first_num = random.randint(100, 501)
    second_num = random.randint(100, 501)
    total = add(first_num, second_num)
    print("  ", first_num, "\n +", second_num)
    answer = int(input("enter your answer"))
    print("  ", first_num, "\n +", second_num, "\n =  ", answer)
    if answer == total:
        print("congratulations, you passed")
    else:
        print("Your answer is wrong")
        print("the correct answer is =", total)


main()