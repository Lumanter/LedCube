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
                    #send produceCode
                    log += "\n" + "Generated cube code:" + "\n" + producedCode

                return log
            else:
                return getErrors()
        else:
            return getErrors()
    else:
        return getErrors()


