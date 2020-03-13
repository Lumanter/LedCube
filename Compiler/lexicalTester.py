from lexicalAnalyzer import lexicalAnalyzer
import re
import codecs
import os
import sys

def escogerArchivo(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1
    
	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)
	for file in files:
		print str(cont) + ". " + file
		cont = cont + 1
	while respuesta == False:
		numArchivo = raw_input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo) - 1]:
				respuesta = True
				break
	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]
	return files[int(numArchivo)-1]

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

def printTokens(analyzer):
    print "-------TokenType: TokenValue-------"
    while True:
        token = analyzer.token()
        if not token: 
            break
        print str(token.type) +": "+ str(token.value)
    print "------------------------------------"

testDirectory = './codeSamples/'
testName = askTestName(testDirectory)
testPath = testDirectory + testName

fileReader = codecs.open(testPath,"r","utf-8")
testAsString = fileReader.read()#
fileReader.close()

testAsString = str(testAsString.decode('utf-8'))

lexicalAnalyzer.input(testAsString)
printTokens(lexicalAnalyzer)