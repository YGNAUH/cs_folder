while 1:
    try:
        n = int(input())
        weight = list(map(int, input().split()))
        number = list(map(int, input().split()))
        dict = {}
        for i in range(n):
            dict[weight[i]] = [weight[i]*ii for ii in range(1,number[i]+1)]
        object_weight = []
        for i in weight:
            combine_list = []
            for j in dict[i]:
                if j not in object_weight and j not in combine_list:
                    combine_list.append(j)
                for k in object_weight:
                    if j + k not in combine_list and j+k not in object_weight:
                        combine_list.append(j+k)
            object_weight += combine_list
        print(len(object_weight)+1)       

    except:
        break