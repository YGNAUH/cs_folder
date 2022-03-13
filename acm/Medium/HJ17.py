while (1):
    try:
        strDict = ["A","W","D","S"]
        strList = input().split(";")
        pos = [0,0]
        for i in range(len(strList)):
            strL = []
            num = []
            for j in range(len(strList[i])):
                if strList[i][j].isalpha():
                        strL.append(strList[i][j])
                if strList[i][j].isdigit():
                        num.append(strList[i][j])
            if len(strL) == 1:
                if strL[0] in strDict:
                    moveNum = int("".join(num))
                    if strL[0] == "W":
                        pos[1] += moveNum
                    if strL[0] == "S":
                        pos[1] -= moveNum
                    if strL[0] == "A":
                        pos[0] -= moveNum
                    if strL[0] == "D":
                        pos[0] += moveNum
        pos = ",".join(map(str,pos))
        print(pos)

    except:
        break