list = input()
x = input()
newlist = [i.upper() for i in list]
print(newlist)
upX = x.upper()
count = 0
for i in range(len(newlist)):
    if upX == newlist[i]:
        count += 1
print(count)