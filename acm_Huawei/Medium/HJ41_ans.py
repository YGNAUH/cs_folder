while True:
    try:
        n = int(input())
        m = list(map(int,input().split()))
        x = list(map(int,input().split()))
    
        amount = []
        weights = {0,}
        for i in range(n):
            for j in range(x[i]):
                amount.append(m[i])
        for i in amount:
            for j in list(weights):
                weights.add(i+j)
        print(len(weights))
    except:
        break