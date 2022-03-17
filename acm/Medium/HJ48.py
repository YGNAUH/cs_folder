while 1:
    try:
        
        string = list(map(int, input().split()))
        link = [] 
        link.append(string[1])
        for i in range(1, string[0]):
            
            link.insert(link.index(string[2*i+1]) + 1, string[2*i])
        
        link.remove(string[-1])
        print(' '.join(map(str, link)))
   
         
    except:
        break