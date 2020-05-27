from ErrorHandling.ErrorHandler import *
from CodeProduction.codeGenerator import getFinalCode

from Semantic.Utils import *

from Lexic.lexicAnalysis import lexicAnalysis
from Syntax.syntacticAnalysis import syntacticAnalyzer

import os

def compile(code):

    resetErrorLog()

    lexicAnalysis(code)

    if not areCompileErrors():

        ast = syntacticAnalyzer.parse(code)

        if not areCompileErrors():

            ast.translation()
            if not areCompileErrors():

                log = getPrints()
                producedCode = getFinalCode()

                if producedCode != "":

                    log += "\n" + "Generated cube code:" + "\n" + producedCode

                    file = open('producedCode.txt', "w")
                    file.write(producedCode)
                    file.close()

                    # Convert to raw string
                    #producedCode = producedCode.encode('unicode_escape')
                    # send produceCode via serial

                return log
            else:
                return getErrors()
        else:
            return getErrors()
    else:
        return getErrors()


