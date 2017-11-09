primary_color1 = input("Enter the first primary color")
primary_color2 = input("Enter the second primary color")
if (primary_color1 == 'red' and primary_color2 == 'blue') or (primary_color1 == 'blue' and primary_color2 == 'red'):
    print("Result color is Purple")
elif (primary_color1 == 'red' and primary_color2 == 'yellow') or (primary_color1 == 'yellow' and primary_color2 == 'blie'):
    print("Result color is Orange")
elif (primary_color1 == 'blue' and primary_color2 == 'yellow') or (primary_color1 == 'yellow' and primary_color2 == 'blue'):
    print("Result color is Green")
else:
    print("Error")


