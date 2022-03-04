x = input().split(".")
if len(x) > 1:
    dec = float(x[-1][0])
    if dec >= 5:
        print(int(x[0])+1)
    else:
        print(int(x[0]))
else:
    print(x[0])
