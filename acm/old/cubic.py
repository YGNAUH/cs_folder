#求立方根
#二分
#pow(n,1/3)
while(1):
    try:
        def cubic(n):
            i = n//1
            s = 0
            b = i
            m = (s+b)//2
            while (b-s>1):
                if m **3 < i:
                    s = m
                    m = (s+b)//2
                elif m **3 > i:
                    b = m
                    m = (s+b)//2
                else:
                    break
            if n == 1:
                return n       
            if m**3 == n:
                return m
            else:
                if n <= 1:
                    b = 1
                m = (s+b)/2
                i=0
                while(i<= 10):
                    #print(s,m,"0")
                    if m**3 < n:
                        s = m
                        m = (s+b)/2
                        i += 1
                        #print(s,m,"1")
                    elif m**3 > n:
                        b = m
                        m = (s+b)/2
                        i += 1
                        #print(s,m,"2")
                    else:
                        return m
                return s
        n = float(input())
        if n >= 0:
            ans = cubic(n)
            print("%.1f"%ans)
            p = pow(n,1/3)
            print(p)
        else:
            ans = -cubic(-n)
            print("%.1f"%ans)



    except:
        break