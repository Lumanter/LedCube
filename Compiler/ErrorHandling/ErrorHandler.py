import os

def resetErrorLog():
    file = open(os.path.abspath('..//Compiler//ErrorHandling//errorLog.txt'), "w")
    file.write("")
    file.close()

def logError(error):
    print "Error logged - " + error
    file = open(os.path.abspath('..//Compiler//ErrorHandling//errorLog.txt'), "a")
    file.write(error + "\n")
    file.close()

def areCompileErrors():
    errors = getErrors()
    areCompileErrors = (errors != "")
    return areCompileErrors

def getErrors():
    file = open(os.path.abspath(os.path.abspath('..//Compiler//ErrorHandling//errorLog.txt')), "r")
    errors = ""
    with file:
        errors = file.read()
    file.close()
    return errors