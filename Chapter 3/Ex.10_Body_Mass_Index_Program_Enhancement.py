weight = int(input("Enter the WEIGHT"))
height = int(input("Enter the HEIGHT"))
BMI = float((weight * 703) / (height ** 2))
if BMI < 18.5 :
    print ("Weight is underweight",format(BMI,'.2f'))
elif BMI >=18.5 and BMI < 25:
    print("Weight is optimal", format(BMI, '.2f'))
else:
    print("weight is overweight",format(BMI,'.2f'))
