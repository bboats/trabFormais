import itertools

class Afn:
	"""docstring for Afn"""
	def __init__(self, automataName, language, operations):
		self.automataName = automataName
		self.language = self.formatLanguage(language)
		self.operations = self.formatOperations(operations)
		self.states,self.transitions,self.initialState,self.finalStates = self.language.split(",,")
		self.states = self.states.split(',')
		self.transitions = self.transitions.split(',')
		self.initialState = self.initialState.split(',')
		self.finalStates = self.finalStates.split(',')


	def formatLanguage(self,lang):
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

	##formatOperations: receives the list of operations for an automata and returns it formatted for splitting
	def formatOperations(self,operations):
		for index,operation in enumerate(operations):
			operations[index]=list(operation)

		for index2,operation in enumerate(operations):
			for index,char in enumerate(operation):
				if char == "(" or char == ")":
					operation[index] = ""
			operations[index2] = ("".join(operation)).split("=")

		return operations