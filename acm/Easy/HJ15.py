n = int(input())
bi = bin(n)[2:]
count = 0
for i in range(len(bi)):
    if bi[i] == "1":
        count += 1
print(count)
