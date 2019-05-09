#Format the language so it can be split more easily (turns commas between parameters into double commas)
def formatLanguage(lang: list):
	#turns language into list so it can be mutable
	language = list(lang)

	aux = 0 #aux value so we know if we have a normal comma or double comma

	for index,i in enumerate(language):
		if i == "{":
			aux = 1
			language[index] = ''
		
		if i == "}":
			aux = 0
			language[index] = ''

		if i == ',' and aux == 0:
			language[index] = ',,'

		if i == '(' or i == ')':
			language[index] = ''




	return ''.join(language)


def formatOperations(operations):
	for index,operation in enumerate(operations):
		operations[index]=list(operation)

	for index2,operation in enumerate(operations):
		for index,char in enumerate(operation):
			if char == "(" or char == ")":
				operation[index] = ""
		operations[index2] = ("".join(operation)).split("=")

	return operations