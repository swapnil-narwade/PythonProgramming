PRICE = 99
quantity = int(input("Enter the number of software purchased"))
total_sale = 0
if quantity >=10 and quantity <19:
    total_sale = quantity * PRICE * 0.8
    print("Total amount is",total_sale)
elif quantity >=20 and quantity < 49 :
    total_sale = quantity * PRICE * 0.7
    print("Total amount is", total_sale)
elif quantity >= 50 and quantity < 99:
    total_sale = quantity * PRICE * 0.6
    print("Total amount is", total_sale)
elif quantity >= 100:
    total_sale = quantity * PRICE * 0.5
    print("Total amount is", total_sale)
else:
    total_sale = quantity * PRICE
    print("Total sale is ",total_sale)