n = int(input())
list = []
i = 2
root = n**0.5
while (n>1):
    if i > root:
        list.append(n)
        n = n/n
    while (n % i == 0):
        list.append(i)
        n = int(n/i)
    i = i + 1
print(" ".join(map(str, list)))