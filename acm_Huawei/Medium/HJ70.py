while 1:
    try:
        n = int(input())
        matrix_list = []
        for i in range(n):
            matrix_list.append(list(map(int,input().split())))
        mul = input()
        mul_matrix = []
        res = 0
        for i in mul:
            if i.isalpha():
                mul_matrix.append(matrix_list[ord(i)-ord("A")])
            elif i == ")" and len(mul_matrix) > 1:
                a = mul_matrix.pop()
                b = mul_matrix.pop()
                res += b[0]*b[1]*a[1]
                mul_matrix.append([b[0],a[1]])
        print(res)
    except:
        break
