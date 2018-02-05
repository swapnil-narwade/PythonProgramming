import random


def main():
    odd = 0
    even = 0
   # random.seed(40)
    for i in range(0, 100):
        number = random.randint(0, 500)
        if number%2 == 0:
            even += 1
            print(number)
        else:
            odd += 1
            print(odd)
    print("total even ", even)
    print("total odd ", odd)


main()
