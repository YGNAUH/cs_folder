def fun(str1,str2):
    if str1 == '' and str2 == '':
        return True
    elif str1 == '' and str2 != '':
        return False
    elif str1 != '' and str2 == '':
        if str1.replace('*', '') == '':
            return True
        else:
            return False
    else:
        m, n = len(str1), len(str2)
        if str1[m-1] == str2[n-1] or (str1[m-1] == '?' and str2.isalnum()):
            return fun(str1[:m-1], str2[:n-1])
        elif str1[m-1] == '*':
            return fun(str1[:m-1], str2) or fun(str1, str2[:n-1])
        else:
            return False

while 1:
    try:
        a = input().lower()
        b = input().lower()
        

    except:
        break