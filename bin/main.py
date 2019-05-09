#Marcos Vinicius de Oliveira Pinto - 288560
#################################MAIN##########################################
from mainLib import *	#all aux functions

##!!!change this so "input.txt" is obtained through input/terminal args!!!!###

###FILE MANIPULATION -- (reading and splitting the file into easily acessible variables)
AFNFile = open("txtfiles/"+"input.txt","r")
lines = (AFNFile.read()).split('\n')

automataName,language = lines[0].split('=')  ### original format is "automataName = {language}"

#Formats the language so it can be easily split later
language = formatLanguage(language)
states,transitions,initialState,finalStates = language.split(",,")

#Turns all 4 into lists using comma as the separator
states = states.split(',')
transitions = transitions.split(',')
initialState = initialState.split(',')
finalStates = finalStates.split(',')

#lines[1] has no purpose other than formatting so it is useless to this program
AFNoperations = lines[2:]
AFNoperations = formatOperations(AFNoperations)

#Determinization of the given automata
#AFDoperations = determinizeOperations()

##/\continue from here, determinizeOperations() needs to be made

print(AFNoperations)