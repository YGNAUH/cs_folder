while (1):
    try:
        n = input()
        space = ord(" ")
        letterCount = 0
        spaceCount = 0
        digitCount = 0
        elseCount = 0
        for i in range(len(n)):
            if ord(n[i]) != space:
                if n[i].isalpha():
                    letterCount += 1
                else:
                    if n[i].isdigit():
                        digitCount += 1
                    else:
                        elseCount += 1
            else:
                spaceCount += 1
        print(letterCount)
        print(spaceCount)
        print(digitCount)
        print(elseCount)
    except:
        break    