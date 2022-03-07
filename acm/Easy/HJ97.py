while(1):
    try:
        n = int(input())
        num = list(map(int,input().split()))
        count_negative = 0
        pos_num = []
        for i in range(n):
            if num[i] < 0:
                count_negative += 1
            elif num[i] > 0:
                pos_num.append(num[i])
        average = str(sum(pos_num)/len(pos_num))
        average = average.split(".")
        if len(average[1]) > 1:
            if int(average[1][1]) < 5:
                average[1] = average[1][0]
            else:
                average[1] = str(int(average[1][0]) + 1)
        average = ".".join(average)
        print(count_negative, average)

    except:
        break