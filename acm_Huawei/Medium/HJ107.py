def decFinder(n):
        dec = 0
        for i in range(int(n)):      
            if i **3 == n:
                dec = i
            elif (i**3) < n and (i+1)**3 > n:
                dec = i
                break
        return dec

def pointFinder(dec):
    left = 0
    right = 10
    while (right - left > 1):
        m = int((left + right)/2)/10
        if (dec + m) ** 3 == n:
            return m
        elif (dec + m) ** 3 > n:
            
            right = int(m*10)
        else:
            
            left = int(m*10)
    
    return left/10

while(1):
    try:
        n = float(input())
        if n < 0:
            n = -n
            dec = decFinder(n)
            for i in range(int(n)):      
                if i **3 == n:
                    dec = i
                elif (i**3) < n and (i+1)**3 > n:
                    dec = i
                    break
            if dec ** 3 == n:
                print(-float(dec))
            else:
                p = pointFinder(dec)
                x = dec + p + 0.05
                if x**3 <= n:
                    print(-int((dec+p+0.1)*100)/100)
                else:
                    print(-(dec+p))
        else:
            dec = decFinder(n)
            
            for i in range(int(n)):      
                if i **3 == n:
                    dec = i
                elif (i**3) < n and (i+1)**3 > n:
                    dec = i
                    break
            #print(dec, n**(1/3))
            if dec ** 3 == n:
                print(float(dec))
            else:
                p = pointFinder(dec)
                x = dec + p + 0.05
                if x**3 <= n:
                    print(int((dec+p+0.1)*100)/100)
                else:
                    print(dec+p)
    except:
        break