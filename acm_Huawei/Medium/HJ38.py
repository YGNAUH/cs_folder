while 1:
    try:
        height = int(input())
        distance = height
        for i in range(5):
            height = height/2
            dec = list(str(int(height*10**7)))
            
            if int(dec[-1]) > 5:
                dec[-2] = str(int(dec[-2]) + 1)
            height = float("".join(dec))/(10**7)
            if i <= 3:
                distance += height*2
            
        print(distance)   
        print(height)
        
            

    except:
        break