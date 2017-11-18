class Money:
    def __init__(self, dollars=0, cents=0):
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        return "$" + str(self.dollars + (self.cents / 100))

    def __repr__(self):
        return "$".format(self.dollars, self.cents)

    def __add__(self, other):
        x1 = self.dollars
        y1 = self.cents
        x2 = other.dollars
        y2 = other.cents
        x = x1 + x2
        y = y1 + y2
        z1 = y % 100
        z2 = y / 100
        x = x + z2
        y = z1
        return Money( x, y)

    def __sub__(self, other):
        x1 = self.dollars * 100
        y1 = self.cents
        x2 = other.dollars * 100
        y2 = other.cents
        x = x1 + y1
        y = x2 + y2
        if x > y:
            x3 = x - y
        else:
            x3 = y - x
        x4 = int(x3 / 100)
        y4 = x3 % 100
        return Money(x4, y4)

    def __eq__(self, other):
        if self.dollars == other.dollars and self.cents == other.cents:
            print('TRUE')
            return 'TRUE'
        else:
            print('FALSE')
            return 'FALSE'

    def __lt__(self, other):
        x1 = self.dollars * 100
        y1 = self.cents
        x2 = other.dollars * 100
        y2 = other.cents
        x = x1 + y1
        y = x2 + y2
        if x < y:
            print('TRUE')
            return 'TRUE'
        else:
            print('FALSE')
            return 'FALSE'

    def __gt__(self, other):
        x1 = self.dollars * 100
        y1 = self.cents
        x2 = other.dollars * 100
        y2 = other.cents
        x = x1 + y1
        y = x2 + y2
        if x > y:
            print('TRUE')
            return 'TRUE'
        else:
            print('FALSE')
            return 'FALSE'

    def __le__(self, other):
        x1 = self.dollars * 100
        y1 = self.cents
        x2 = other.dollars * 100
        y2 = other.cents
        x = x1 + y1
        y = x2 + y2
        if x <= y:
            print('TRUE')
            return 'TRUE'
        else:
            print('FALSE')
            return 'FALSE'

    def __ge__(self, other):
        x1 = self.dollars * 100
        y1 = self.cents
        x2 = other.dollars * 100
        y2 = other.cents
        x = x1 + y1
        y = x2 + y2
        if x >= y:
            print('TRUE')
            return 'TRUE'
        else:
            print('FALSE')
            return 'FALSE'

    def get_dollars(self, dollars):
        return self.dollars

    def get_cents(self, cents):
        return self.cents

    def set_dollars(self, dollars):
        self.dollars = dollars

    def set_cents(self, cents):
        if 0 < cents < 99:
            self.cents = cents
        else:
            print("Please enter the amount between 0 and 99")


'''
def main():
    dollar_amount = int(input("Please Enter The Dollar Amount"))
    cents_amount = float(input("Please Enter The Dollar Amount"))
    m1 = Money(dollar_amount,cents_amount)
    m1.set_dollars(dollar_amount)
    m1.set_cents(cents_amount)
    dollar_amount = int(input("Please Enter The Dollar Amount"))
    cents_amount = float(input("Please Enter The Dollar Amount"))
    m2 = Money(dollar_amount, cents_amount)
    m2.set_dollars(dollar_amount)
    m2.set_cents(cents_amount)
main()
'''

def main():
    m1 = Money(2,25)
    m2 = Money(3,75)
    m3 = Money(4,50)
    add = m1 + m2
    sub = m1 - m2 
    m1 < m2
    m1> m2
    m1 == m2
    m1 <= m2
    m1>= m2
    print (m1)
    print(m2)
    print(m3)
    print(add)
    print(sub)
main()