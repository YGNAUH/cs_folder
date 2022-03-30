numList = []
count = 0
while 1:
    try:
        n = int(input())
        if n < 0:
            count += 1
        else:
            numList.append(n)
    except:
        break
ave = 0.0
if len(numList) > 0:
    ave = str(float(sum(numList))/(len(numList)))
    ave = ave.split(".")
    if len(ave[1]) > 2:
        if int(ave[1][1]) > 5:
            ave[1] = str(int(ave[1][0])+1)
    ave[1] = ave[1][0]
    ave = ".".join(ave)
print(count)
print(ave)