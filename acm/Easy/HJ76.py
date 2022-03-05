while(1):
    try:
        n = int(input())
        list = []
        if n == 1:
            list.append(1)
        else:
            a = 1 + n*(n-1)
            list.append(a)
            for i in range(n-1):
                list.append(a+2)
                a = a+2
        print("+".join(map(str, list)))
    except:
        break