#Fibonacci Question: 
# 3 approaches involved: recursion, memorization, dynamic programming

# Fibonacci recursion:
def fib_rec(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return(fib_rec(n-1) + fib_rec(n-2))

# memorization 
def fib_mem(n, dp):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = fib_mem(n-2,dp) + fib_mem(n-1,dp)
    return dp[n]

#dp:
def fib_dp(n):
    dp = [0,1]
    if n < 2:
        return dp[n]
    else:
        for i in range(2,n+1):
            dp.append(dp[i-2]+dp[i-1])
        return dp[n]

fib_rec_3 = fib_rec(5)
print(fib_rec_3)

fib_dp_3 = fib_dp(5)
print(fib_dp_3)

dp_mem = [0]*6
print(fib_mem(5,dp_mem))