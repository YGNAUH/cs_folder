def nthUglyNumber(n):
    dp = [0]*n
    dp[0] = 1
    a,b,c = 0,0,0
    for i in range(1, n):
        dp[i] = min(dp[a]*2, dp[b]*3,dp[c]*5)
        if dp[a]*2 == dp[i]:
            a += 1
        if dp[b]*3 == dp[i]:
            b += 1
        if dp[c]*5 == dp[i]:
            c += 1
    return dp[-1]
print(nthUglyNumber(11))