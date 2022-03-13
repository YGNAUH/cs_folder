def check(s):
    if len(s) <= 8:
        return 0
    a, b, c, d = 0, 0, 0, 0
    for item in s:
        if ord('a') <= ord(item) <= ord('z'):
            a = 1
        elif ord('A') <= ord(item) <= ord('Z'):
            b = 1
        elif ord('0') <= ord(item) <= ord('9'):
            c = 1
        else:
            d = 1
    if a + b + c + d < 3:
        return 0
    for i in range(len(s)-3):
        test = s.split(s[i:i+3])
        print(test)
        if len(s.split(s[i:i+3])) >= 3:
            return 0
    return 1

while 1:
    try:
        print('OK' if check(input()) else 'NG')
    except:
        break
