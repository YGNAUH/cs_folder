while 1:
    try:
        n = input()
        i = 0
        digitList = []
        digitLen = []
        while i < len(n):
            if n[i].isdigit():
                iStart = i
                if i != len(n)-1:
                    for j in range(i+1,len(n)):
                        if n[j].isdigit() == 0:
                            digitList.append(n[iStart:j])
                            digitLen.append(j-i)
                            i = j+1
                            break
                        else:
                            if j == len(n)-1:
                                digitList.append(n[iStart:len(n)])
                                digitLen.append(j-i+1)

                                i = j + 1
                else:
                    digitList.append(n[-1])
                    i += 1
            else:
                i += 1
        idx = (digitLen.index(max(digitLen)))
        maxnum = max(digitLen)
        count = digitLen.count(maxnum)
        if count == 1:
            outputList = [digitList[idx],str(maxnum)]
        else:
            outputList = []
            for i in digitList:
                print(i)
                if len(i) == maxnum:
                    outputList.append(i)
            strJoin = "".join(outputList)
            outputList = [strJoin,str(maxnum)]
        print(",".join(outputList)) 
        
    except:
        break