#输入n值，n为下次输入的个数，0为正序，1为倒序

#读取列表，输出列表
while(1):
    try:
        n = int(input())
        ls = list(map(int,input().split()))
        s = 0
        m = int(input())
        if m == 0:
            for i in range(n-1):
                s = i
                for j in range(i+1,n):
                    if ls[s] > ls[j]:
                        s = j
                sv = ls[s] 
                iv = ls[i]
                ls[i] = sv
                ls[s] = iv  
            ls = [str(x) for x in ls]
            ls = " ".join(ls)
            print(ls)
            
        else:
            for i in range(n-1):
                s = i
                for j in range(i+1,n):
                    if ls[s] < ls[j]:
                        s = j
                sv = ls[s] 
                iv = ls[i]
                ls[i] = sv
                ls[s] = iv 
            for i in ls:
                print(i, end = " ")
    except:
        break

x = [1, 2, 5, 7]
x=[str(i) for i in x]
x = int("".join(x))
