def maxProfit(prices):
    dp = [0]*len(prices)
    idx_min = prices.index(min(prices))
    idx_max = prices.index(max(prices))

    if idx_max > idx_min:
        return (prices[idx_max]-prices[idx_min])
    else:
        for i in range(1,len(prices)):
            dp[i] = prices[i] - min(prices[0:i+1])
    return max(dp)
        
print(maxProfit([7,6,5,4,3,1]))
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([10,12,1,5,8,9,13]))