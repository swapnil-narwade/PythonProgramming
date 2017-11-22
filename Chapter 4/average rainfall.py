year = int(input("Enter the number of year you want the rainfall to be shown"))
b = [[] for i in range(0, year)]
a = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
     'October', 'November', 'December']
for i in range(0, year):
    print("Enter the rainfall for year ", i + 1)
    for j in range(0, 12):
        rainfall = float(input("Enter the rainfall for this month"))
        print("Rainfall for month ", j + 1, a[j], "=", rainfall)
        b[i].append(rainfall)
average = 0
for l in range(0, 12):
    total = 0
    for k in range(0, year):
        total += b[k][l]
    average = total / year
    print("Average of month ", l + 1, a[l], "=", average)
