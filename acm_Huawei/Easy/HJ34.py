while(1):
    try:
        n = input()
        list = []
        for i in n:
            list.append(ord(i))
        list = sorted(list)
        charList = [chr(x) for x in list]
        print("".join(charList))
    except:
        break