while(1):
    try:
        year, month, day = input().split()
        year, month, day = int(year), int(month), int(day)
        dict = {
            1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 
            9:30, 10:31, 11:30, 12:31,
        }
        if year % 4 == 0 and year % 100 != 0 :
            dict[2] = 29
        daystotal = 0
        for i in range(1,month):
            daystotal += dict[i]
        daystotal += day
        print(daystotal)
    except:
        break