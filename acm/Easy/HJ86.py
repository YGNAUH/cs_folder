while(1):
    try:
        n = int(input())
        b = bin(n)[2:]
        i, k = 0,1
        count1 = []
        while i < len(b) and k < len(b):
            if b[k] == "1":
                if k == len(b) - 1:
                    count1.append(k-i+1)
                else:
                    if b[k+1] != 1:
                        count1.append(k-i+1)
                k = k+1
            else:
                i = k + 1
                k = k + 1
        if not count1:
            if n != 0:
                print(1)
            else:
                print(0)
        else:
            print(max(count1))


    except:
        break