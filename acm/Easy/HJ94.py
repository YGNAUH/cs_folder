while(1):
    try:
        n = int(input())
        names = input().split()
        m = int(input())
        votes = input().split()
        
        dict = {"Invalid":0}
        for i in range(m):
            if votes[i] in names:
                if votes[i] not in dict:
                    dict[votes[i]] = 1
                else:
                    dict[votes[i]] += 1
            else:
                dict["Invalid"] += 1
        
        for i in names:
            if i in dict:
                print(i,":",dict[i])
            else:
                print(i," : ",0)
        print("Invalid:", dict["Invalid"])
        
    except:
        break