while True:
    try:
        n = int(input())
        x = input().split()
        f = x[::-1]
        print(f)
        k = int(input())
        if k == 0:
            print(0)
        else:
            print(f[k-1])
        
    except:
        break
