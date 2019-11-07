#Python Script to run when opening a .NCS file
global SyntaxError
lineNum = 1
changeStart = -1



printCaffeine = True
    
class caffeineFunctions:
    class regVarDecl:
        print(0)
    class plusPlusPlusETC:
        print(0)
    class plusEquals:
        print(0)
    class minusEquals:
        print(0)
    class timesEquals:
        print(0)
    class divideEquals:
        print(0)
    class dontPrint:
        def __init__(self, inLine):
            self.inLine = inLine

        def run(self):
            global printCaffeine
            printCaffeine = False

        def Check(self, inLine):
            if inLine == ';;dontPrint();': 
                caffeineFunctions.dontPrint.run(None)
                return True
            else:
                return False

    class whiteSpace:
        
        print(0)
    class intSign:
        print(0)
    class err:
        print(0)

def changePC():
    global printCaffeine
    global changeStart
    changeStart += 1
    if changeStart > 1:
        printCaffeine = True


def getLine(x):
    if x%10 == 0 and printCaffeine == True: 
        return ';;print("CAFFEINE!");'
    elif x%10 == 0 and printCaffeine == False:
        changePC()
    line = input("")
    return line
while True:
    currentLine = getLine(lineNum)
    if currentLine != ';;print("CAFFEINE!");':
        caffeineFunctions.dontPrint.Check(None, currentLine)
        lineNum += 1
    else:
        print("CAFFEINE!!!!!!!!!")
        currentLine = getLine(lineNum+1)
        lineNum += 1

