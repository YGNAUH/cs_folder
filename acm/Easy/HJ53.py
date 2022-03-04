while True:
    try:
        n = int(input())
        triangle_list = [[1],[1,1,1]]
        
        for i in range(1,n-1):
            list = []
            list.append(1)
            add_num = int(2*i+1)
            
            for j in range(add_num-1):
                if j >= 1:
                    list.append(triangle_list[i][j-1]+triangle_list[i][j]+triangle_list[i][j+1])
                else:
                    
                    list.append(triangle_list[i][j]+triangle_list[i][j+1])
            list.append(triangle_list[i][-1]+triangle_list[i][-2])
            list.append(1)
            triangle_list.append(list)
       
        list = triangle_list[n-1]
        
        for i in range(len(list)):
            if (list[i] % 2 == 0):
                print(i+1)
                break
            else:
                if i == len(list) - 1:
                    print(-1)            
    except:
        break