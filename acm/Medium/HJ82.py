while True:
    try:
        a,b = map(int,input().split('/'))
        a = a * 10
        b = b * 10
        res = []
        while a:
            for i in range(a,0,-1):
                if(b % i == 0):
                    print(b,i,b % i, b/i)
                    res.append('1' + '/' + str(int(b / i)))
                    a = a - i
                    break
        print('+'.join(res))
    except:
        break


