while(1):
    try:
        n = int(input())
        prime_num = [2]
        for i in range(2, n):
            for j in range(2,i):
                if i % j == 0:
                    break
                else:
                    if j == i-1:
                        prime_num.append(i)
        print(prime_num)
        pairs = []
        for i in prime_num:
            if i > n/2:
                break
            else:
                if int(n - i) in prime_num:
                    pairs.append([i,int(n-i)])
            
        print(pairs[-1][0])
        print(pairs[-1][1])

    except:
        break