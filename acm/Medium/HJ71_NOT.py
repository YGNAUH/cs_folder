while 1:
    try:
        a = input()
        b = input()
        for i in b:
           i.lower()
        i = 0
        while i < len(a):
            if a[i].isalpha():
                a[i].lower()

    except:
        break