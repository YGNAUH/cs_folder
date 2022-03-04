#漂亮名字，每个字母可代表1-26，不同字母不同数字，算名字最大数值
n = int(input())
for i in range(n):
    str = input()
    counter = {}
    for i in range(len(str)):
        if str[i] not in counter:
            counter[str[i]] = str.count(str[i])
    print(counter)
    num = counter.values()
    num = sorted(list(num),reverse=1)
    print(num)
    r = 0
    for i in range(len(num)):
        r += (26-i)*num[i]
        print(i,r)
    print(r)

