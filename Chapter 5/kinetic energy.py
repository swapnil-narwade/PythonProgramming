def kinetic_energy(val1, val2):
    e = format((1 / 2 * val1 * val2 ** 2), ',.2f')
    return e


def main():
    print("Welcome to kinetic energy")
    mass = int(input("Enter the mass of object in kilogram"))
    velocity = int(input("Enter the velocity of object in meter per second"))
    kinetically = kinetic_energy(mass, velocity)
    print("Kinetic energy of object is ", kinetically)


main()
