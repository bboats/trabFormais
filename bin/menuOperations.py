import AutomataClasses

def openLanguage ():
	automataFileName = input('Name or PATH to the language file?:\n')
	if automataFileName[-4:]  != '.txt':
		automataFileName+= '.txt'

	try:
		AFNFile = open(automataFileName,"r")
	except:
		print('File does not exist! (press enter to go back to the menu)')
		input()
	

	lines = (AFNFile.read()).split('\n')
	automataName,language = lines[0].split('=')  ### original format is "automataName = {language}"
	#lines[1] has no purpose other than formatting so it is useless to this program
	AFNoperations = lines[2:]
	afn = AutomataClasses.Afn(automataName,language,AFNoperations)
	afd = AutomataClasses.Afd(*afn.determinizeOperations())
	return afd


print(openLanguage().operations)