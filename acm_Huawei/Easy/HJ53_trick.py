while(1):
    try:
        n = int(input())
        if n <= 2:
            print(-1)
        else:
            n = n-2
            div, res = divmod(n,4)
            if res == 1:
                print(2)
            if res == 2:
                print(3)
            if res == 3:
                print(2)
            if res == 0:
                print(4)



    except:
        break