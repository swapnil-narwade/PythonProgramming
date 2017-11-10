print ("Reboot the computer and try to connect")
fix = input("Did that fix the problem?")
if fix == 'no':
    print ("reboot the router and try to connect")
    fix = input("Did that fix the problem?")
    if fix == 'no':
        print ("make sure the cables between the router and modem are plugged in firmely")
        fix = input("Did that fix the problem?")
        if fix == 'no':
            print ("move the router to a new location and try to connect")
            fix = input("Did that fix the problem?")
            if fix == 'no':
                print ("get a new router")
print ("")



