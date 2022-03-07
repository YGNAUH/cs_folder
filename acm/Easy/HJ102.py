while(1):
    try:
        str = input()
        unilist = {}
        for i in range(len(str)):
            if str[i] not in unilist:
                unilist[str[i]] = 1
            else:
                unilist[str[i]] += 1
        orderlist = {}
        uniletter = list(unilist)
        for i in uniletter:
            element = []
            if unilist[i] not in orderlist:
                orderlist[unilist[i]] = [ord(i)]
            else:
                orderlist[unilist[i]].append(ord(i))
        ordered_value = sorted(list(orderlist),reverse=1)
        list4print = []
        for i in ordered_value:
            ord_sorted = sorted(orderlist[i])
            for j in ord_sorted:
                list4print.append(chr(j))
        print("".join(list4print))            
    except:
        break