while True:
    try:
        month=int(input())
        n=month-1
        def func(n):
            if n<2:
                return 1
            else:
                return func(n-1)+func(n-2)
        print(func(n))
    except:
        break