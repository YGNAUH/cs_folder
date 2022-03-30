while 1:
    try:
        n = int(input())
        num = []
        for i in range(1,n+1):
            if "7" in str(i):
                num.append(i)
            else:
                if i % 7 == 0:
                    num.append(i)
        print(len(num))
    except:
        break