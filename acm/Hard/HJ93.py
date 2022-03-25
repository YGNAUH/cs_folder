def sepList(sum3, sum5, sum_other):
    if len(sum_other) == 0:
        if sum3 == sum5:
            return True
        else:
            return False
    else:
        return sepList(sum3 + sum_other[0], sum5, sum_other[1:]) or sepList(sum3, sum5 + sum_other[0], sum_other[1:])

while 1:
    try:
        n = int(input())
        numList = list(map(int,input().split()))
        part_5 = []
        part_3 = []
        part_other = []
        for i in numList:
            if i % 5 == 0:
                part_5.append(i)
            elif i%3 == 0:
                part_3.append(i)
            else:
                part_other.append(i)
        if (sepList(sum(part_3),sum(part_5),part_other)):
            print("true")
        else:
            print("false")
    except:
        break