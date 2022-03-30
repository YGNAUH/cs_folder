while 1:
    try:
        n = int(input())
        numList = []
        for i in range(n):
            a = int(input())
            if a not in numList:
                numList.append(int(a))
        numList = sorted(numList)
        print(numList)
        for i in numList:
            print(i)
    except:
        break