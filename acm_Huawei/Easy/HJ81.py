while(1):
    try:
        short = input()
        long = input()
        for i in range(len(short)):
            if short[i] not in long:
                print("false")
                break
            else:
                if i == len(short)-1:
                    print("true")
    except:
        break