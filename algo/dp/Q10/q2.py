# Cake price
price_list = [0,2,3,6,7,11,15]

#recursion:
def cakemax_rec(n):
    if n == 0 or n == 1:
        return price_list[n]
    else:
        max_price = 0
        for i in range(n):
            max_price = max(max_price, price_list[n-i] + cakemax_rec(i))
        return max_price

print(cakemax_rec(5))

#memorization
mem = [0,2,0,0,0,0,0]
def cakemax_mem(n):
    if n < 2:
        return price_list[n]
    if mem[n] != 0:
        return mem[n]
    else:
        max_price = 0
        for i in range(n):
            max_price = max(max_price, price_list[n-i] + cakemax_rec(i))
        mem[n] = max_price
        return max_price

print(cakemax_mem(5))

def cakemax_dp(n):
    dp = [0,2,0,0,0,0,0,0]
    if n < 2:
        return dp[n]
    else:
        for i in range(2, n+1):
            for j in range(i):
                dp[i]  = max(dp[i] , dp[j] + price_list[i-j])
        return dp[n]
print(cakemax_dp(5))