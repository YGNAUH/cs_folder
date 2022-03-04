while True:
    try:
        list = input()
        round, res = divmod(len(list),8)
        
        a = []
        for i in range(round + 1):
            if i < round:
                a.append(list[(i*8):((i+1)*8)])
            else:
                if res != 0:
                    x = list[(i*8):(i*8)+res]
                    zero = "0"* (8-res)
                    adder = "".join([x,zero])
                    a.append(adder)
        
        print("\n\r".join(a))
    except:
        break