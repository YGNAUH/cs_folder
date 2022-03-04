a = input()
a = list(a[::-1])
newlist = []
for i in range(len(a)):
    if (a[i] not in newlist):
        newlist.append(a[i])
print("".join(newlist))