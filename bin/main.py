#Marcos Vinicius de Oliveira Pinto - 288560
#################################MAIN##########################################
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


##/\continue from here, determinizeOperations() needs to be made
