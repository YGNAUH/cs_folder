while 1:
    try:
        n = int(input())
        arr = list(map(int,input().split()))
        dp = [0 for zero in range(n)]
        for i in range(n-2,-1,-1):
            dpCom = [0 for zero in range(n)]
            
            for j in range(i+1,n):
                if arr[j] > arr[i]:
                    dpCom[j] += 1
                    dpCom[j] += dp[j]
            dp[i] = max(dpCom)
        
        print(max(dp)+1)


    except:
        break