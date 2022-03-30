while(1):
    try:
        str = input()
        count = 0
        for i in str:
            if (ord(i)) >= 65 and (ord(i)) <= 90:
                count += 1
        print(count)
    except:
        break