fileToHandle = raw_input("Drop file here ")
compOrDecomp = raw_input("Compress ? y / n ")

if(compOrDecomp == "y"):
    print "Yeet -> Yote"
    readFile = open(fileToHandle,"r")
    currentChar = 'a';
    charStack = []
    countStack = []
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
    for x in range (0,len(charStack)):
        print charStack[x], " * ", countStack[x]
    writeFile = open(fileToHandle.replace(".yeet",".yote"), "w")
    for x in range(0, len(charStack)):
        writeFile.write(charStack[x]) #1 byte
        writeFile.write(chr(countStack[x])) #1 byte in ascii
    writeFile.flush()
    #while(currentChar != '\0'):
        #currentChar = readFile.read(1)
        #if(charStack[len(charStack)-1] != currentChar):
            #charStack.append(currentChar)
            
else:
    print "Yote -> Yeet"
    readFile = open(fileToHandle,"r")
    writeFile = open(fileToHandle.replace(".yote","_DE.yeet"), "w")
    fileLen = len(readFile.read())
    readFile.seek(0)
    for x in range (0,fileLen/2):
        charToWrite = readFile.read(1)
        charCount = readFile.read(1)
        for a in range (0, ord(charCount)):
            writeFile.write(charToWrite)
    writeFile.flush()
    
