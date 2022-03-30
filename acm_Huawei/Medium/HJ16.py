while(1):
    try:
        m, n = map(int,input().split())
        vlist, plist, qlist = [],[],[]
        for i in range(n):
            v, p, q = map(int,input().split())
            vlist.append(v)
            plist.append(p)
            qlist.append(q)
        dp = [[ 0 for i in range(0, m+1,10)] for j in range(n+1)]
        print(dp)
        
    except:
        break