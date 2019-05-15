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
from oopLib import *
##!!!change this so "input.txt" is obtained through input/terminal args!!!!###

###FILE MANIPULATION -- (reading and splitting the file into easily acessible variables)
AFNFile = open("txtfiles/"+"input.txt","r")
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
