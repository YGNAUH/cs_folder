while(1):
    try:
        n = int(input())
        count = 0
        while n > 2:
            div,res = divmod(n,3)
            n = div + res
            count += div
        if n == 2: 
            count += 1
        if count != 0:
            print(count)
        
    except:
        break