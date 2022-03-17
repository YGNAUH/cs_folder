while 1:
    try:
        n = input().split()
        res = []
        i = 0
        while i < len(n):
          
            if n[i].count('"') == 2:
                res.append(n[i].replace('"',""))
                i += 1

            if n[i].count('"') == 1:
                temp = n[i].replace('"',"")
                for j in range(i+1,len(n)):
                    if n[j].count('"') == 1:
                        temp = temp + " " + n[j].replace('"',"")
                        break
                    else:
                        temp = temp + " " + n[j]
                res.append(temp)
                i = j + 1
            else:
                res.append(n[i])
                i += 1
        print(len(res))
        for i in res:
            print(i)            
        
                    
    except:
        break