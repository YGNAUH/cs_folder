def maxValue(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]

            elif i == 0:
                dp[i][j] = grid[i][j] + dp[i][j-1]

            elif j == 0:
                dp[i][j] = grid[i][j] + dp[i-1][j]
            
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + grid[i][j]
    return dp[-1][-1]

grid = [[1]]
mV = maxValue(grid)
print(mV)