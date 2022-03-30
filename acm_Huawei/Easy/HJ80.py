while(True):
    try:
        l1 = int(input())
        arr1 = input().split()
        l2 = int(input())
        arr2 = input().split()
        newlist = []
        for i in range(l1):
            if int(arr1[i]) not in newlist:
                newlist.append(int(arr1[i]))
        for i in range(l2):
            if int(arr2[i]) not in newlist:
                newlist.append(int(arr2[i]))
        newlist = sorted(newlist)
        print("".join(map(str,newlist)))
    except:
        break