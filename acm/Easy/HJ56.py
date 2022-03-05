while (1):
    try:
        n = int(input())
        count = 0
        for i in range(1,n+1):
            num = i
            list = []
            list.append(1)
            for j in range(2, int(num**0.5) + 1):
                if num % j == 0:
                    list.append(j)
                    if int(num/j) != j:
                        list.append(num/j)
            s = sum(list)
            if s == num:
                count += 1
        print(count-1)
    except:
        break