total_expenses = 0
budget = float(input("Enter the total budget of yours"))
expenses = int(input("Enter the total number of expenses you have"))
for i in range(0,expenses):
    expense = float(input("Enter the expense "))
    total_expenses += expense
if total_expenses < budget:
    print("Budget is over by", budget - total_expenses)
else:
    print("Budget is under by",total_expenses - budget)
