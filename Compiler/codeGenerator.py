finalCode = ""


def writeCode(lineOfCode):
    global finalCode
    finalCode += lineOfCode


def delay(time, timeUnit):
    instruction = "delay," + str(time) + ',' + str(timeUnit) + "\n"
    writeCode(instruction)


def turn(x, y, z, state):
    instruction = "turn," + str(x) + ',' + str(y) + ',' + str(z) + ',' + str(state).lower() + "\n"
    writeCode(instruction)


def blink(x, y, z, time, timeUnit, state):
    instruction = "blink," + str(x) + ',' + str(y) + ',' + str(z) + ',' + str(time) + ',' + str(timeUnit) + ',' + str(
        state).lower() + "\n"
    writeCode(instruction)
