while True:
    try:
        n = input()
        dict = {}
        for i in range(len(n)):
            if n[i] not in dict:
                dict[n[i]] = 1
            else:
                dict[n[i]] += 1
        
        m = min(dict.values())
        
        list = []
        for i in range(len(n)):
            if dict[n[i]] != m:
                list.append(n[i])
        print("".join(list))
    except:
        break