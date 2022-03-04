while(1):
    try:
        n, k = input().split()
        xlist = input()
        x = [int(i) for i in xlist.split()]
        x = sorted(x)
        x = x[:int(k)]
        print(" ".join(map(str,x)))
    except:
        break