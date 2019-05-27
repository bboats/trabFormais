#!/usr/bin/python3
#Marcos Vinicius de Oliveira Pinto - 288560
#################################MAIN##########################################
###TO-DO###
#Execution interface
#	Ask if user inputs the word or gives textfile
#	Ask if user wants to exit
#Comment the code better
#Clean any unused libraries and temporary test files
############

#from mainLib import *	#all aux functions
from AutomataClasses import *
import sys
flag = 'kb'
##!!!change this so "input.txt" is obtained through input/terminal args!!!!###
for arg in sys.argv[1:]:
	if arg == '-file':
		flag = 'file'
	if arg == '-keyboard':
		flag = 'kb'
	if arg == '-v' or arg == '-help':
		print('\n>>Trabalho Final de Linguagens Formais e Automatos<<')
		print('\ndefinition of script pipiippopopo...')
		print('\n------------|Avaiable arguments|------------')
		print('   -file: give the list of words to be recognized through a .txt file.')
		print('   -keyboard: give the list of words to be recognized through user input.')
		print('   -v: show this help screen\n')
		sys.exit()
###FILE MANIPULATION -- (reading and splitting the file into easily acessible variables)
automataFileName = input('Name or PATH to the language file?:\n')
if automataFileName[-4:]  != '.txt':
	automataFileName+= '.txt'

print(automataFileName)
AFNFile = open(automataFileName,"r")
lines = (AFNFile.read()).split('\n')

automataName,language = lines[0].split('=')  ### original format is "automataName = {language}"
#lines[1] has no purpose other than formatting so it is useless to this program
AFNoperations = lines[2:]
afn = Afn(automataName,language,AFNoperations)
afd = Afd(*afn.determinizeOperations())

wordsFile = open("txtfiles/"+"words.txt","r")
words = (wordsFile.read()).split('\n')
#print(afd.operations)
#print(afd.finalStates)
#print(afd.initialState)

###The program needs to 
print('\tTesting all words from words.txt:',)
for word in words:
	afd.processWord(word)
