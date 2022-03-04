# 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,
# 小写字母都变成对应的数字，数字和其他的符号都不做变换，
#密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，
m = input()
while (m == "1"):
    n = list(input())
    LsUpper = {"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g",\
        "g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n",\
        "n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"}
    LsLower = {"a":"2","b":"2","c":"2","d":"3","e":"3","f":"3",\
        "g":"4","h":"4","i":"4","j":"5","k":"5","l":"5","m":"6",\
        "n":"6","o":"6","p":"7","q":"7","r":"7","s":"7","t":"8","u":"8","v":"8","w":"9","x":"9","y":"9","z":"9"}
    for i in range(len(n)):
        if n[i].isupper():
            s = n[i].lower()
            s = LsUpper[s]
            print(s,end = "")
        elif n[i].islower():
            s = n[i]
            s = LsLower[s]
            print(s,end = "")
        elif n[i].isdigit():
            print(n[i],end="")
        if i == (len(n))-1:
            print()
while(m == "2"):
    n = input()
    for i in range(len(n)):
        if n[i].isupper():
            if n[i]!= "Z":
                print(str.lower(chr(ord(n[i])+1)),end="")
            else:
                print("a")
        elif n[i].isdigit():
            print(n[i])
        elif n[i].islower():
            if n[i] in "abc":
                print("2",end="")
            elif n[i] in "def":
                print("3",end="")
            elif n[i] in "ghi":
                print("4",end="")
            elif n[i] in "jkl":
                print("5",end="")
            elif n[i] in "mno":
                print("6",end="")
            elif n[i] in "pqrs":
                print("7",end="")
            elif n[i] in "tuv":
                print("8",end="")
            elif n[i] in "wxyz":
                print("9",end="")