while True:
    try:
        a,b=list(map(int, input().split()))
        if a < b:
            a,b=b,a
        for i in range(a,a*b+1,a):
            if i%b==0:
                print(i)
                break
    except:
        break

