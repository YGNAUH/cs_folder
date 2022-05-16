# Regular Expression (regex)
#recursion:

dp = [" "]
def regex_rec(s, p):
    if s == "" and p =="":
        return True
    elif s != "" and p == "":
        return False
    elif s == "" and p != "":
        if len(p) > 1:
            if p[1] == "*":
                return regex_rec(s, p[2:])
            else:
                return False
        else:
            if p == "*": return True
            else: return False
    else:
        if p[0].isalnum():
            dp[0] = p[0]
            if len(p) == 1:
                if s[0] == p[0]:
                    return regex_rec(s[1:],p[1:])
                else:
                    return False
            else:
                if p[1] == "*":
                    if p[0] != s[0]:
                        return regex_rec(s,p[2:])
                    else:
                        return regex_rec(s[1:],p) or regex_rec(s,p[2:])
                else:
                    if s[0] == p[0]: 
                        return regex_rec(s[1:],p[1:])
                    else:
                        return False
             
        elif p[0] == ".":
            dp[0] = s[0]
            if len(p) > 1:
                if p[1] == "*":
                    dp[0] = "."
                    return regex_rec(s[1:],p[1:]) or regex_rec(s,p[2:])
            return regex_rec(s[1:],p[1:])


        elif p[0] == "*":
            p1 = dp[0] + p[1:]
            p2 = dp[0] + "*" + p[1:]
            return regex_rec(s,p[1:]) or regex_rec(s,p1) or regex_rec(s,p2)
            
'''s = input()
p = input()
print(regex_rec(s,p))
'''

def regex_dp(s, p):
    m, n = len(s) + 1, len(p) + 1
    dp = [[False] * n for _ in range(m)]
    dp[0][0] = True
    for i in range(2, n, 2):
        if dp[0][i-2] == 1 and p[i-1] == "*":
            dp[0][i] = True                                          
    for i in range(1,m):
        for j in range(1,n):
            if p[j-1] == "*":
                if dp[i][j-2] == True:
                    dp[i][j] = True
                elif dp[i-1][j] == 1 and p[j-2] == s[i-1]:
                    dp[i][j] = True
                elif dp[i-1][j] == 1 and p[j-2] == ".":
                    dp[i][j] = True
            else:
                if dp[i-1][j-1] == True and p[j-1] == s[i-1]:
                    dp[i][j] = True
                elif dp[i-1][j-1] == True and p[j-1] == ".":
                    dp[i][j] = True
    return dp[m-1][n-1]
s = input()
p = input()
print(regex_dp(s,p))