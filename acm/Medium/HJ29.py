while 1:
    try:
        n = input()
        listOut = []
        for i in n:
            if i.isupper():
                listOut.append(chr(ord(i.lower())+1)) 
            elif i.islower():
                listOut.append(chr(ord(i.upper())+1)) 
    except:
        break