# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
#保证输入的整数最后一位不是0
'''while(1):
    r = []
    try:
        n = int(input())
        i = 1
        dec = 0
        while(n >= i):
            i *= 10
            dec += 1
        #print(dec)
        for i in range(dec):
            d = n%10
            n = int(round((n-d)/10))
            r.append(d)
        #print(r)
        i = 0
        while (1):
            ls = []
            for j in range(i+1,len(r)):
                if r[j] == r[i]:
                    ls.append(j)
            #print(ls,len(ls))

            for k in range(len(ls)):
                r.pop(ls[k]-k)

                #print(k,ls[k],"  ",r)
            #print(r,i,len(r))
            i += 1
            
            if i == len(r)-1 or i == len(r):
                #print("here")
                break
        for x in r:
            print(str(x),end = "")
    except:
        break'''

num = list(input())
num1 = []
for i in range(len(num)):
    n=num[-i-1]
    if num1.count(n) == 1:
        continue
    num1.append(n)
for m in range(len(num1)):
    print(num1[m],end='')

