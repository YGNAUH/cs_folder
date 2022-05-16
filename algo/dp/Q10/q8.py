def lengthOfLongestSubstring(s):
    if s == "":
        return 0
    else:
        dp = [0]*len(s)
        dp[0] = 1
        current_str = s[0]
        if len(s) > 1:
            for i in range(1, len(s)):
                if s[i] not in current_str:
                    dp[i]  = dp[i-1] + 1
                    current_str += s[i]
                else:
                    for j in range(len(current_str)):
                        if s[i] == current_str[j]:
                            dp[i] = dp[i-1] - j
                            current_str = current_str[j+1:] + s[i]
                            break
        return max(dp)
s = input()
print(lengthOfLongestSubstring(s))