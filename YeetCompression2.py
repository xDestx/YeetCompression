
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
    writeFile = open(fileToHandle.replace(".yeet",".yote"), "w")
    binData = ""
    #Using a string... :(
    
    for x in range (0, len(charStack)):
        if(countStack[x] > 1):
            binData = binData + '00000001'
        else:
            binData = binData + '00000000'
        strToAdd = binToStr(ord(charStack[x]))
        binData = binData + strToAdd
        if(countStack[x] > 1):
            strToAdd = binToStr(countStack[x])
            binData = binData + strToAdd
            
    offset = len(binData)%8
    for x in range(0,offset):
        binData = binData + '0'
        
    writeFile = open(newFileName, "w")
    for x in range(0,len(binData)/8):
        writeFile.write(convertToBin(binData[x*8:(x*8)+8]))
    writeFile.flush()
        
    #Always read first byte
    #for x in range (0,len(charStack)):
     #   print charStack[x], " * ", countStack[x]
    #writeFile = open(fileToHandle.replace(".yeet",".yote"), "w")
    #for x in range(0, len(charStack)):
    #    writeFile.write(charStack[x]) #1 byte
    #    writeFile.write(chr(countStack[x])) #1 byte in ascii
    #writeFile.flush()
    
    
def convertToBin(strOfBin):
    return chr(int(strOfBin,2))

def binToStr(thingToString):
    myString = bin(thingToString).replace("0b","")
    offsetStr = len(myString)%8
    addition = ""
    for a in range (0,offsetStr):
        addition = addition + '0'
    return addition + myString

fileToHandle = raw_input("Drop File Here ")
compress(fileToHandle, fileToHandle + ".dang")
