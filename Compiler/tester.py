import re
import codecs
import os
import sys
sys.path.append('./syntax/')

from syntacticAnalysis import syntacticAnalyzer
from lexicalAnalysis import lexicalAnalyzer


testDirectory = './codeSamples/'
testType = "lexic" #lexic, syntax or semantic

def askTestName(directory):
	foundedFiles = []
	fileNumber = ''
	response = False
	filesCounter = 1
	print "Files in " + directory
	for base, dirs, files in os.walk(directory):
		foundedFiles.append(files)
	for file in files:
		print str(filesCounter) + ". " + file
		filesCounter = filesCounter + 1
	while response == False:
		fileNumber = raw_input('\nNumber of the file to test: ')
		for file in files:
			if file == files[int(fileNumber) - 1]:
				response = True
				break
	print "Testing file \"%s\"...\n" %files[int(fileNumber)-1]
	return files[int(fileNumber)-1]

def retrieveFile(filePath):
	fileReader = codecs.open(filePath,"r","utf-8")
	fileAsUnicode = fileReader.read()
	fileReader.close()
	fileAsString = str(fileAsUnicode.decode('utf-8'))
	return fileAsString

def lexicTest(data):
    lexicalAnalyzer.input(data)
    print "-------TokenType: TokenValue-------"
    while True:
        token = lexicalAnalyzer.token()
        if not token: 
            break
        print str(token.type) +": "+ str(token.value)
    print "------------------------------------"

def syntaxTest(data):
	abstractSyntaxTree = syntacticAnalyzer.parse(data)
	def printTuple(myTuple):
		for subTuple in myTuple:
			if isinstance(subTuple[0], tuple):
				printTuple(subTuple)
			else:
				print subTuple
	print "\n" + "Syntax Analysis Result:" + "\n"
	printTuple(abstractSyntaxTree)

testName = askTestName(testDirectory)
testPath = testDirectory + testName
testAsString = retrieveFile(testPath)

if testType is "lexic":
	lexicTest(testAsString)
elif testType is "syntax":
	syntaxTest(testAsString)
else:
	print "semantic is not ready yet"

