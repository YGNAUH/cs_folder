# input 16,2进制转十进制

'''a = list(map(str,input()))
print(a)
if a[0] == "0" and a[1] == "x":
    h = "".join(a)
    print(h)
    i = int(h,16)
    print(i)
if a[0] == "0" and a[1] == "b":
    b = "".join(a)
    print(b)
    i = int(b,2)
    print(i)'''


'''while True: 
    try: 
        num=input() 
        a=int(num,16) 
        print(a) 
    except: break'''


while True:
    try:
        str1 = input()
        str2 = str1[2:]
        n = len(str2)
        dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        x1 = 0
        for word in str2:
            if word in dic:
                x1 = x1 + dic[word]*16**(n-1)
                n = n - 1
            else:
                x1 = x1 + int(word)*16**(n-1)
                n = n - 1
        print(x1)

    except:
        break