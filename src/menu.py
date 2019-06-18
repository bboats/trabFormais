#!Python3
import AutomataClasses
from os import system, name

###########################
##### main menu class #####
###########################
class Menu:
	"""text-based menu class, receives a list of options and a title as init arguments"""
	def __init__(self, options, title='|'):
		self.options = options
		self.title = title


	def showMenu(self,title='|'):
		"""showMenu: Displays a menu from a given list of options exit will always be option 0 and implicit
		Receives a list of strings, each string represents an option for the menu
		Can also receive a title for the menu as second parameter"""

		#clears the screen#
		#windows
		if name == 'nt': 
			_ = system('cls') 

		#mac/linux 
		else: 
			_ = system('clear') 


		print('Marcos Vinicius de Oliveira Pinto - 00288560')
		print(10*'#',self.title,10*'#','\n')


		for index,option in enumerate(self.options):
			print(index+1,':',option)

		print('0 : Exit')
		print()
		print((22+len(self.title))*'#','\n')

		return int(input('OpNumber?: '))




#########################
#### menu operations ####
#########################

def openLanguage():
	#makes the user input again if file is not found (or any other error happens)
	done = 0
	while done == 0:
		automataFileName = input('Name or PATH to the LANGUAGE file?:\n')
		if automataFileName[-4:]  != '.txt':
			automataFileName+= '.txt'
		try:
			AFNFile = open(automataFileName,"r")
			done = 1
		except:
			print('File does not exist! (press enter to try again)')
			input()
		
	

	lines = (AFNFile.read()).split('\n')
	automataName,language = lines[0].split('=')  ### original format is "automataName = {language}"
	#lines[1] has no purpose other than formatting so it is useless to this program
	AFNoperations = lines[2:]
	afn = AutomataClasses.Afn(automataName,language,AFNoperations)
	afd = AutomataClasses.Afd(*afn.determinizeOperations())
	return afd



def testWordsTxt():
	done = 0
	while done == 0:
		wordsFileName = input('Name or PATH to the WORDS file?:\n')
		if wordsFileName[-4:]  != '.txt':
			wordsFileName+= '.txt'
		try:
			wordsFile = open(wordsFileName,"r")
			done = 1 #if the open() does not fail then there were no errors and the while loop can end
		except:
			print('File does not exist! (press enter to try again)')
			input()

	return (wordsFile.read()).split('\n')


def testWordsKb():
	return input('Word? ')