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
    