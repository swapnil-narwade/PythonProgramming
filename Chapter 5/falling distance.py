GRAVITY = 9.8


def falling_distance(time):
    distance = 1/2 * (GRAVITY * (time ** 2))
    return float(format(distance, '0.2f'))


def mail():
    for i in range(0, 10):
        distance = falling_distance(i)
        print("Distance travelled is ", distance)


mail()
