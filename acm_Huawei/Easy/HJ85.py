while(1):
    try:
        n = input()
        i,k = 0, 2
        list = []
        if n == n[::-1]:
            print(len(n))
        else:
            for i in range(len(n)):
                for j in range(i+2,len(n)+1):
                    if n[i:j] == n[i:j][::-1]:
                            list.append(j-i)
            if list:
                print(max(list))
            else:
                print(0)
    except:
        break