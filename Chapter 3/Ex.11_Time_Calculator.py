time = int(input("Enter the number of seconds"))
if time < 3600 and time >=60:
    minutes = (time / 60)
    sec = time % 60
    print("Total time is = ",format( minutes,'.0f'),"minutes and ",sec,"seconds")
elif time <86400 and time >= 3600:
    hour = int(time /3600)
    minutes = (time % 3600) / 60
    sec =  ((time % 3600) % 60)
    print("total time is = ", format(hour,'.0f'),"hour",format(minutes,'.0f'),"minutes",format(sec,'.0f'),"seconds")
elif time >= 86400:
    day = (time / 86400)
    hour = (time % 86400)/3600
    minutes = ((time %86400) % 3600)/60
    sec = ((time %86400) % 3600)% 60
    print("total time is = ",format(day,'0.0f'),"days", format(hour,'.0f'),"hour",format(minutes,'.0f'),"minutes",format(sec,'.0f'),"seconds")
else :
    print("total seconds", time)