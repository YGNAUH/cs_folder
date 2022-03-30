while 1:
    try:
        endSong = int(input())
        startSong= 1
        buttons = input()
        currentSong = 1
        pages = [1,2,3,4]
        startPage = 1
        endPage = 4
        for i in buttons:
            if i == "U":
                if currentSong == startSong:
                    currentSong = endSong
                    endPage = endSong
                    startPage = endSong - 3
                    pages = [i for i in range(startPage,endPage+1)]
                else:
                    currentSong -= 1
                    if currentSong < startPage:
                        
                        startPage = currentSong
                        endPage = startPage + 3
                        pages = [i for i in range(startPage,endPage+1)]
            if i == "D":
                if currentSong == endSong:
                    currentSong = startSong
                    pages = [1,2,3,4]
                    startPage = 1
                    endPage = 4
                else:
                    currentSong += 1
                    if currentSong > endPage:
                        endPage = currentSong
                        startPage = endPage - 3
                        pages = [i for i in range(startPage,endPage+1)]
            print(currentSong,pages)
        if endSong <= 4:
            pages = [i for i in range(startSong,endSong+1)]
        print(" ".join(map(str,pages)))           
        print(currentSong)
        
    except:
        break