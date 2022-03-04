while True:
    try:
        x = input().split()
        n = int(x[0])
        k = int(x[1])
        a = input().split()
        for i in range(n):
            for j in range(i + 1,n):
                if float(a[i]) > float(a[j]):
                    a[i], a[j] = a[j], a[i]
        a = a[:k]
        print(a)
        print(" ".join(a))
    except:
        break