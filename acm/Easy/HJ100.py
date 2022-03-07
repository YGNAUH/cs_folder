while(1):
    try:
        n = int(input())
        starter = 2
        sum = 0
        for i in range(n):
            sum += starter
            starter += 3
        print(sum)
    except:
        break