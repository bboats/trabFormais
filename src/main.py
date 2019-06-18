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
import AutomataClasses
import menu


userChoice = ''




wordsFile = open("txtfiles/"+"words.txt","r")
words = (wordsFile.read()).split('\n')
#print(afd.operations)
#print(afd.finalStates)
#print(afd.initialState)

###The program needs to 
print('\tTesting all words from words.txt:',)
for word in words:
	afd.processWord(word)
