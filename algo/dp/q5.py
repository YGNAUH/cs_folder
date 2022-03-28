def maxSubArray_loops(nums):
    max_sub = nums[0]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            max_sub = max(sum(nums[i:j]), max_sub)
    return max_sub
# O(n^2) not suitable
nums = list(map(int, input().split()))
#print(maxSubArray(nums))

def maxSubArray(nums):
    dp = [0]*len(nums)
    dp[0]  = nums[0]
    if len(nums) > 1:
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
    return max(dp)
print(maxSubArray(nums))