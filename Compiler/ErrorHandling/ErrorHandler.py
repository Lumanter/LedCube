import os

def resetErrorLog():
    file = open(os.path.abspath('.//ErrorHandling//errorLog.txt'), "w")
    file.write("")
    file.close()

def logError(error):
    file = open(os.path.abspath('.//ErrorHandling//errorLog.txt'), "a")
    file.write(error + "\n")
    file.close()

def areCompileErrors():
    file = open(os.path.abspath('.//ErrorHandling//errorLog.txt'), "r")
    errors = ""
    with file:
        errors = file.read()
    areCompileErrors = (errors != "")
    file.close()
    return areCompileErrors