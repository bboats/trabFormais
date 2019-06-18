#!Python3

def showMenu(options,title='|'):
	'''showMenu: Displays a menu from a given list of options exit will always be option 0 and implicit
	Receives a list of strings, each string represents an option for the menu
	Can also receive a title for the menu as second parameter'''
	print('Marcos Vinicius de Oliveira Pinto - 00288560')
	print(10*'#',title,10*'#','\n')


	for index,option in enumerate(options):
		print(index+1,':',option)

	print('0 : Exit')
	print()
	print((22+len(title))*'#','\n')

	return input('OpNumber?: ')

opt = ['Open a language.txt file','Test words (from keyboard)','Test words (from .txt file)']

showMenu(opt)