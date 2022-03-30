while(1):
    try:
        n = int(input())
        list = input().split()
        idx = int(input())
        if idx == 0:
            uplist = [int(i) for i in list]
            uplist = sorted(uplist)
            print(" ".join(map(str, uplist)))
        else:
            downlist = [int(i) for i in list]
            downlist = sorted(downlist,reverse=1)
            print(" ".join(map(str, downlist)))
    except:
        break