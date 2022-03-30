n = input()
dict = []
count = 0
for i in range(len(n)):
    if n[i] not in dict:
        dict.append(n[i])
        count += 1
print(count)
