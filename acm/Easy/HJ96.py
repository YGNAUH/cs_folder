while(1):
    try:
        n = input()
        list = []

        for i in range(len(n)):
            if n[i].isdigit():
                if i != 0 and i != len(n)-1:
                    if n[i-1].isdigit() == 0:
                        list.append('*')
                        list.append(n[i])
                    if n[i+1].isdigit() == 0:
                        if n[i-1].isdigit() == 0:
                            list.append("*")
                        else:
                            list.append(n[i])
                            list.append("*")
                    elif n[i-1].isdigit() == 1 and n[i+1].isdigit() == 1:
                        list.append(n[i])
                if i == 0:
                    list.append('*')
                    list.append(n[i])
                    if n[i+1].isdigit() == 0:
                        list.append("*")
                if i == len(n)-1:
                    if n[i-1].isdigit() == 0:
                        list.append('*')
                        list.append(n[i])
                        list.append('*')
                    else:
                        list.append(n[i])
                        list.append("*")
            else:
                list.append(n[i])
        print("".join(list))
    except:
        break