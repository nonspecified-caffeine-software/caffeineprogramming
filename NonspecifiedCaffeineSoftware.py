#Python Script to run when opening a .NCS file
global SyntaxError
global printCaffeine
printCaffeine = True
lineNum = 1

def getLine(x):
    if x%10 == 0 and printCaffeine == True: 
        return ';;print("CAFFEINE!");'
    line = input("")
    return line
    
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
            printCaffeine = False
        

        def Check(self, inLine):
            if inLine == ';;dontPrint();': 
                self.run()
                return True
            else:
                return False

    class whiteSpace:
        
        print(0)
    class intSign:
        print(0)
    class err:
        print(0)

while True:
    currentLine = getLine(lineNum)
    if currentLine != ';;print("CAFFEINE!");':
        lineNum += 1
    else:
        print("CAFFEINE!!!!!!!!!")
        currentLine = getLine(lineNum+1)
        lineNum += 1
