while 1:
    try:
        DNA = input()
        strLen = int(input())
        CG = []
        for i in range(0,len(DNA)-strLen+1):
            subDNA = DNA[i:i+strLen]
            CG.append((subDNA.count("C") + subDNA.count("G"))/strLen)
        idx = CG.index(max(CG))
        maxSUB = DNA[idx:idx+strLen]
        print(maxSUB)
    except:
        break