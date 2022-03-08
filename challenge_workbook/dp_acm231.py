#bag question
#recursion solution and DP solution
n = 4
w,v = [2,1,3,2],[3,2,4,2]
W = 5
res = 0
#i: no. of decision made, j: remained weight
dp = [[-1 for i in range(W+1)] for j in range(n+1)]
'''for i in range(n+1):
    dp.append([])
    for j in range(W+1):
        dp[i].append(-1)
'''
#recursion method:
def rec(i,j):
    if dp[i][j] >= 0:
        return dp[i][j]
    
    
    if (i == n):
        res = 0
        
        
    elif (j < w[i]):
        res = rec(i+1, j)
        
    else:
        res  = max(rec(i+1, j), rec(i+1, j-w[i])+v[i])
    dp[i][j] = res
    return  res

# DP method
dp = [[0 for i in range(W+1)] for j in range(n+1)]
def dpSolve():
    for i in range(n-1, -1, -1):
        for j in range(0, W+1):
            if (j < w[i]):
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j-w[i]]+v[i])
#Test
r = rec(0,W)
print(dp)
dpr = dpSolve()
print(dp)
