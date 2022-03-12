while(1):
    try:
        n,m  = map(int,(input().split()))
        dp = [[ 0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if j == 0 or i == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp[m][n])
    except:
        break