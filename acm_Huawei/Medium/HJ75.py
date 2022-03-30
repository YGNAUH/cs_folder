while 1:
    try:
        a = input()
        b = input()
        if len(a) > len(b):
            a,b = b,a
        dp = [0 for i in range(len(a))]
        

        for i in range(len(a)):
            if i != len(a) - 1:
                for j in range(i+1,len(a)):
                    if a[i:j+1] in b:
                        
                        dp[i] = j-i+1
                    else:
                        break
            else:
                if a[i] in b:
                    dp[i] = 1

        print(max(dp))
    except:
        break