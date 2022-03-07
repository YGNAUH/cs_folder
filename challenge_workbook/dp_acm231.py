#bag question
#recursion solution and DP solution
n = 4
w,v = [2,1,3,2],[3,2,4,2]
W = 5

#i: no. of decision made, j: remained weight
def rec(i,j):
    res = 0
    if (i == n):
        res = 0
    elif (j < w[i]):
        res = rec(i+1, j)
    else:
        res = max(rec(i+1, j), rec(i+1, j-w[i])+v[i])
    print(res)
    return res

rec(0,W)
