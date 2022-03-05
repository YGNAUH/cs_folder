while(1):
    try:
        m,n = map(int, input().split())
        x1, y1, x2, y2 = map(int, input().split()) 
        add_x = int(input())
        add_y = int(input())
        x, y = map(int, input().split()) 
        print("starting")
        if (m <= 9) and (n<= 9):
            print(0)
        else:
            print(-1)

        if x1 <= m-1 and x2 <= m-1:
            if y1 <= n-1 and y2 <= n-1:
                print(0)
            else:
                print(-1)
        else:
            print(-1)

        if add_x <= m-1 and (n+add_x) <= 9:
            print(0)
            
        else:
            print(-1)
        
        if add_y <= n-1 and (n + add_y) <= 9:
            print(0)
            
        else:
            print(-1)
        
        if x <= m-1:
            if y <= n-1:
                print(0)
            else:
                print(-1)
        else:
            print(-1)
        


    except:
        break