while(1):
    try:
        n = int(input())
        bi = bin(n)[2:]
        print(bi.count("1"))
    except:
        break