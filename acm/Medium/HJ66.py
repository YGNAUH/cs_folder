while 1:
    try:
        n = input().split()
        dict = {"reset":"reset what","reset board":"board fault",
        "board add":"where to add", "board delete":"no board at all",
        "reboot backplane":"impossible","backplane abort":"install first"}
        commandList = list(dict.keys())
        for i in range(len(commandList)):
            commandList[i] = commandList[i].split()
        if len(n) == 1:
            if n[0] in "reset":
                print(dict["reset"])
            else:
                print("unknown command")
        elif len(n) == 2:
            count = 0
            for i in range(1,len(commandList)):
                #if n[0] in commandList[i][0] and n[1]  in commandList[i][1]:
                l0,l1 = len(n[0]),len(n[1])
                if n[0] == commandList[i][0][0:l0] and n[1] == commandList[i][1][0:l1]:
                    dictStr = " ".join(commandList[i])
                    count += 1
            if count == 1:
                print(dict[dictStr])
            else:
                print("unknown command")
        else:
            print("unknown command")
    except:
        break

   
	
