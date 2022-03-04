#小数点转整数 四舍五入
n = float(input())
i = n//1
d = n % 1
print(d)
if d >= 0.5:
    print(int(i+1))
else:
    print(int(i))



# method 2:
while(1):
    try:
        n = input()
        i = int(n.split('.')[0])
        d = int(n.split('.')[1])
        if d >= 5:
            print(i+1)
        else:
            print(i)
    except:
        break