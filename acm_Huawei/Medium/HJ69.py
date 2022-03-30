while 1:
    try:
        x = int(input())
        y = int(input())
        z = int(input())
        array1 = []
        for i in range(x):
            array1.append(list(map(int,input().split())))
        array2 = []
        for i in range(y):
            array2.append(list(map(int,input().split())))
        matrix = [[0 for i in range(z)] for j in range(x)]
        for i in range(x):
            for j in range(z):
                sum = 0
                for k in range(y):
                    sum += array1[i][k]*array2[k][j]
                matrix[i][j] = sum
        for i in range(x):
            print(" ".join(map(str,matrix[i])))
    except:
        break