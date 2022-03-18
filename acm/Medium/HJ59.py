while 1:
    try:
        n = input()
        dict = {''}
        strList = []
        for i in n:
            if i not in dict:
                dict.add(i)
                if n.count(i) == 1:
                    strList.append(i)
        if len(strList) >= 1:
            print(strList[0])
        else:
            print(-1)
    except:
        break