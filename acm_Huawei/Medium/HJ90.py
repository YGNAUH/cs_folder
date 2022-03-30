while 1:
    try:
        n = input().split(".")
        
        flag = True
        if len(n)!= 4:
            flag = False
        
        for i in range(len(n)):
            if not n[i] or (len(n[i]) > 1 and  n[i][0] == "0"):
                flag = False
                break
            

            for j in range(len(n[i])):
                if not n[i][j].isdigit():
                    flag = False
                    break
                if j == len(n[i])-1:
                    a = int("".join(n[i]))
                    if a > 255:
                        flag = False
                        break
                   
        if (flag):print("YES")
        else: print("NO")


    except:
        break