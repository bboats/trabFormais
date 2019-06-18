#!/usr/bin/python3
#Marcos Vinicius de Oliveira Pinto - 288560
#################################MAIN##########################################
###TO-DO###
#GUI with tkinter
#Comment the code better
#Clean any unused libraries and temporary test files
############

import AutomataClasses #AFD and AFN classes
import menu #text-based user interface (for use without tkinter) 
from sys import exit #sys.exit 

options = ['Carregar um automato a partir de um .txt','Testar palavras a partir de um .txt','Testar uma palavra a partir do teclado']


mainMenu = menu.Menu(options,'- no language -')
while 1:
	userChoice = mainMenu.showMenu()

	if userChoice == 1:
		afd = menu.openLanguage()
		mainMenu = menu.Menu(options,afd.automataName)

	elif userChoice == 2:
		for word in menu.testWordsTxt(): #textWordsTxt returns a list of words from a given file
			afd.processWord(word)
		input('(press enter to go back to the menu)')

	elif userChoice == 3:
		afd.processWord(menu.testWordsKb())
		input('(press enter to go back to the menu)')

	elif userChoice == 0:
		exit('Fim do script por decisao do usuario')

