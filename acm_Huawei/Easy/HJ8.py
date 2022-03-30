n = int(input())
list = []
dict = {}
for i in range(n):
    list.append(input().split())
    if int(list[i][0]) not in dict:
        dict[int(list[i][0])] = int(list[i][1])
    else:
        dict[int(list[i][0])] += int(list[i][1])
dicKey = sorted([*dict])
for i in range(len(dict)):
    print(dicKey[i],dict[dicKey[i]])