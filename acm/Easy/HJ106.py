while(1):
    try:
        s = input().split()[::-1]
        list4print = []
        for i in range(len(s)):
            list4print.append(s[i][::-1])
        print("  ".join(list4print))
    except:
        break