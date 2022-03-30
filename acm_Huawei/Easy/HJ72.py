while(1):
    try:
        n = input()
        mon = 100
        count1,count2,count3 = 0,0,0
        val = [5, 3, 1/3]
        list = []
        for i in range(0,21):
            for j in range(0,34):
                k = 100-i-j
                if i*val[0] + j*val[1] + k*val[2] == 100:
                    
                    list.append([i, j, k])
        
        for i in range(len(list)):
            print(" ".join(map(str,list[i])))
        
    except:
        break