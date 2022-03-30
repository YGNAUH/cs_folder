while 1:
    try:
        IP_base255 = input().split(".")
        IP_base10 = int(input())
        ip_255 = []
        for i in IP_base255:
            ip_255.append(bin(int(i))[2:].zfill(8))
        ip_255 = int("".join(ip_255),2)
        print(ip_255)


        ip_10 = bin(IP_base10)[2:]
        div,res = divmod(len(ip_10),8)
        if res != 0:
            div += 1
        ip_10 = ip_10.zfill(div*8)
        ip_10_list = []
        for i in range(0, len(ip_10),8):
            ip_10_list.append(int(ip_10[i:i+8],2))
        ip_10_list = ".".join(map(str,ip_10_list))
        print(ip_10_list)
    except:
        break