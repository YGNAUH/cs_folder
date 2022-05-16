def translateNum(num):
    num = str(num)
    dp = [0]*(len(num)+1)
    dp[0], dp[1] = 1,1
    if len(num) > 1:
        for i in range(1,len(num)):
            if int(num[i-1:i+1]) < 26 and int(num[i-1]) != 0:
                dp[i+1] = dp[i] + dp[i-1]
            else:
                dp[i+1] = dp[i]
    return dp[-1]
num = int(input())
print(translateNum(num))