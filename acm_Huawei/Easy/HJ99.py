while(1):
    try:
        n = int(input())
        list = []
        count = 0
        for i in range(n+1):
            l1 = len(str(i))
            l2 = len(str(i**2))
            if str(i**2)[l2-l1:l2] == str(i):
                list.append(i)
                count += 1
        print(count)
                  
    except:
        break