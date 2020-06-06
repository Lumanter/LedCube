finalCode = ""

def getFinalCode():
    global finalCode
    return finalCode

def wipeCode():
    global finalCode
    finalCode = ""

def writeCode(lineOfCode):
    global finalCode
    finalCode += lineOfCode


def readFinalCode():
    return
    #print finalCode
    #print "\n\n\n"

def delay(time, timeUnit):
    instruction = "d," + str(time) + ',' + str(timeUnit) + "\n"
    writeCode(instruction)


def turn(x, y, z, state):
    if x < 8 and y < 8 and z < 8:
        instruction = "t" + str(x) + str(y) + str(z) + str(state)[0] + "\n"
        writeCode(instruction)


def blink(x, y, z, time, timeUnit, state):
    instruction = "b" + str(x) + str(y) + str(z) + "," + str(time) + ',' + str(timeUnit) + ',' + str(
        state)[0] + "\n"
    writeCode(instruction)
