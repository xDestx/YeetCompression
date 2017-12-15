def compress(readFile, newFileName):
    currentChar = 'a';
    charStack = []
    countStack = []
    readFile = open(readFile,"r")
    fileLen = len(readFile.read())
    readFile.seek(0)
    for i in range (0,fileLen):
        currentChar = readFile.read(1)
        if(len(charStack) == 0 or charStack[len(charStack)-1] != currentChar):
            charStack.append(currentChar)
            countStack.append(1)
        else:
            countStackValue = countStack[len(countStack)-1]
            if(countStackValue < 255):
                countStack[len(countStack)-1] = countStack[len(countStack)-1] + 1
            else:
                charStack.append(currentChar)
                countStack.append(1)
    loopDuration = (len(charStack)/8)
    if(len(charStack)%8 != 0):
        loopDuration = loopDuration + 1
        
    writeFile = open(newFileName, "w")
    try:
        for x in range (0, loopDuration):
            startingPosition = x * 8
            markByteArr = []
            markByte = 0b0
            #array of bytes
            for a in range(startingPosition, startingPosition+8):
                if(countStack[a] == 0):
                    markByteArr.append(0b0)
                else:
                    markByteArr.append(0b1)
            for a in range(0,8):
                markByte = markByte|markByteArr[a]<<a
            writeFile.write(chr(markByte))
            #Mark written, now write the rest
            #The mark gives information about the next 8 unique bytes
            for a in range(0,8):
                writeFile.write(charStack[startingPosition+a])
                if(countStack[startingPosition+a] != 1):
                    writeFile.write(chr(countStack[startingPosition+a]))
    except:
        print "oops"
    writeFile.flush()
    
fileToHandle = raw_input("Drop File Here ")
compress(fileToHandle, fileToHandle + ".dang")
