while 1:
    try:
        n = input().split()
        xStr = n[-2]
        sortedX = sorted(xStr)
        broStr = []
        idx = int(n[-1]) - 1
        for i in range(1,int(n[0])+1):
            if n[i] != xStr and sorted(n[i]) == sortedX:
                broStr.append(n[i])
        broStr = sorted(broStr)
        print(len(broStr))
        print(broStr[idx])
    except:
        break