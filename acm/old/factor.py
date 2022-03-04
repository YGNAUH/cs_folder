# 寻找一个数的因子，当因子大于该数平方根时，loop断开
n = int(input())
d = 2
r = []
while(1):
    if n == 1:
        print("1")
        break
    elif n % d == 0:
        r.append(d)
        n = n/d
        print(r,n)
    else:
        d += 1
        if d > pow(n,1/2):
            r.append(n)
            break

r = [str(x) for x in r]
r = " ".join(r)
print(r)