while(1):
    try:
        n = int(input())
        num_col = 0
        starter = 1
        adder_hrz = [x for x in range(2,n+1)]
        adder_vrt = [x for x in range(1,n)]
        while num_col < n-1:
            list = []
            list.append(starter)
            num = starter
            for i in range(num_col, n-1):
                num +=  adder_hrz[i]
                list.append(num)
            print(" ".join(map(str, list)))
            starter += adder_vrt[num_col]
            num_col += 1
        if num_col == n-1:
            print(starter)

    except:
        break