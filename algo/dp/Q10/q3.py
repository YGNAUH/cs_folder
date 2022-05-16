# frog upstairs 
# can jump 1 stairs or 2

#recursion method
def frogJump_rec(n):
    if n == 1 or n == 0:
        return 1
    else:
        return frogJump_rec(n-1) + frogJump_rec(n-2)

print(frogJump_rec(4))
#memorization method

mem = [0]*1000
mem[0], mem[1] = 1,1
def frogJump_mem(n):
    if n == 1 or n == 0:
        return 1
    if mem[n] != 0:
        return mem[n]
    else:
        mem[n] = frogJump_mem(n-1) + frogJump_mem(n-2)
        return mem[n]

print(frogJump_mem(4))

dp = [0]*100
def frogJump_dp(n):
    dp[0],dp[1] = 1, 1
    if n < 2:
        return dp[n]
    else:
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
print(frogJump_dp(4))


    
