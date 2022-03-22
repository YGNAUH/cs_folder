while 1:
    try:
        n = int(input())
        numList = list(map(int,input().split()))
        uniList = []
        for i in numList:
            if i not in uniList:
                uniList.append(i)
        
        

    except:
        break