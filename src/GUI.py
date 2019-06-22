#Marcos Vinicius de Oliveira Pinto - 288560
#Arquivo contendo a clase do menu principal, ele que permite ao usuario decidir o que fazer


import AutomataClasses #AFD and AFN classes
from tkinter import *
from tkinter import filedialog


### Global variables for window colors ###
bg1 = "gray12"

#############################################

class MenuClass():
	"""GUI menu for the program using tkinter"""
	def __init__(self):
		#inicializa a janela Tk
		self.root = Tk()
		self.root.iconbitmap(r'images\faustao.ico')
		self.root.title('Trabson de Formais - Marcos Vinicius de Oliveira Pinto')
		self.root.geometry("500x410")
		self.root.resizable(0,0)

		#inicializa as três frames que compoem o layout
		self.titleFrame = Frame(self.root,height=0,width=600,bg=bg1)
		self.titleFrame.pack(side="top",fill='x')
		self.leftFrame = Frame(self.root,width=300,height=350,bg=bg1)
		self.leftFrame.pack(side="left",fill='both')
		self.leftFrame.pack_propagate(0)
		self.rightFrame = Frame(self.root,width=200,height=350,bg=bg1)
		self.rightFrame.pack(side="right",fill='both')
		self.rightFrame.pack_propagate(0)


		#automato default (não carregado)
		self.afd = False


		######################
		##########CABECALHO##########
		######################
		#texto do titulo (nome da linguagem/automato)
		self.titleImg = PhotoImage(file="images/title.png")
		self.title = Label(self.titleFrame,image=self.titleImg)
		self.title.titleImg = self.titleImg
		self.title['bg'] = self.title.master['bg']
		self.title.pack(pady=(5,0))



		#############################


		######################
		#####LADO ESQUERDO#########
		######################

		###Botão para abrir txt da linguagem###
		self.abrirLinguagem = Button(self.leftFrame,text="Abrir Linguagem",command=self.abreLinguagem,font=("Sans Serif",16))
		self.abrirLinguagem.pack(pady=(20,30),ipadx=50)


		###Botão para abrir txt das palavras###
		self.abrirPalavras = Button(self.leftFrame,text="Testar Palavras de um .Txt",command=self.palavrasTxt,font=("Sans Serif",16))
		self.abrirPalavras.pack(padx=(3,3),pady=(3,3))

		####Caixa de input manual e seus botões####
		self.caixaPalavras = Text(self.leftFrame,height=9,width=33,borderwidth=6,relief=RIDGE)
		self.caixaPalavras.insert(END, ' Insira palavras separadas aqui!\n    (Separadas por virgula)')
		self.caixaPalavras.pack(pady=(20,14))

		###Botão submit p/ caixa de input
		self.enviaPalavras = Button(self.leftFrame,text="Testar as palavras!",command=self.palavrasKB)
		self.enviaPalavras.pack(side="left",anchor="n",padx=(35,80),pady=(2,2))

		###Botão clear p/ caixa de input
		self.limpaPalavras = Button(self.leftFrame,text="Clear",command=self.limpaCaixa)
		self.limpaPalavras.pack(side="left",anchor="n")


		######################

		######################
		#####LADO DIREITO#####
		######################

		#box sobre automato atual
		self.displayAutomato = Label(self.rightFrame, text="Nenhum automato carregado!",bg="red",font=("Sans Serif",9,'bold'))
		self.displayAutomato.pack(pady=(20,0),ipadx=100,ipady=10,padx=(0,10))


		#imagem de enfeite
		self.img = PhotoImage(file="images/tetris.png")
		self.displayImg = Label(self.rightFrame, image=self.img)
		self.displayImg.img = self.img
		self.displayImg['bg'] = self.displayImg.master['bg']
		self.displayImg.pack(pady=(20,0))



		#botao para fechar o programa
		self.exitButton = Button(self.rightFrame,text="Sair",command=self.root.quit)
		self.exitButton.pack(ipadx=50,pady=(0,20),side="bottom")




		######################
		#mantém o menu em display usando mainloop()
		self.root.mainloop()
		

	def abreLinguagem(self):
		languagepath = filedialog.askopenfilename(title="Escolha o arquivo de linguagem",filetypes=(("text files","*.txt"),("all files","*.*")))
		try:
			AFNFile = open(languagepath,"r")
			self.afd = ""
		except:
			return 0
		lines = (AFNFile.read()).split('\n')
		AFNFile.close()
		automataName,language = lines[0].split('=')  ### original format is "automataName = {language}"
		#lines[1] has no purpose other than formatting so it is useless to this program
		AFNoperations = lines[2:]
		afn = AutomataClasses.Afn(automataName,language,AFNoperations)

		self.afd = AutomataClasses.Afd(*afn.determinizeOperations()) #self.afd recebe o AFD gerado
		#muda o titulo da janela para o nome do automato carregado

		self.displayAutomato['text'] = "Automato: " + automataName
		self.displayAutomato['bg'] = "green"


	def palavrasTxt(self):
		#se nao ter carregado nenhuma linguagem não faz nada
		if self.afd == False:
			return 0

		#abre janela de seleção de arquivo
		wordsFilePath = filedialog.askopenfilename(title="Escolha o arquivo de palavras",filetypes=(("text files","*.txt"),("all files","*.*")))
		
		#checa se o usuario selecionou um arquivo válido/selecionou at all
		try:
			wordsFile = open(wordsFilePath,"r")
		except:
			return 0
		wordsList = (wordsFile.read()).split('\n')

		#cria a janela para mostrar o resultado dos testes
		self.respostasJanela = Toplevel(self.root,bg=bg1)
		self.respostasJanela.title("Resultados")
		self.respostasJanela.resizable(0,0)
		self.respostasJanela.minsize(250,0)


		textoResultados = ""
		#gera a string de resultados
		for word in wordsList: #textWordsTxt returns a list of words from a given file
			textoResultados = self.afd.processWord(word)
			#checa se a palavra foi aceita (caso seja, a cor é verde, senão a cor é vermelha)
			if textoResultados.rfind("ACEITA") != -1:
				color = "green"
			else:
				color = "red"
			#empacota o resultado na subjanela de resultados, com a cor correspondente
			self.respostasLabel = Label(self.respostasJanela,text=textoResultados,font=("Sans Serif",13,'bold'),fg=color,bg=bg1,anchor=W)
			self.respostasLabel.pack(padx=(5,0),fill='x',expand=1)

		#mantém o foco do programa na janela dos resultados até ela ser fechada
		self.respostasJanela.grab_set()


	def palavrasKB(self):
		if self.afd == False:
			return 0

		wordsList = self.caixaPalavras.get("1.0",END)[0:-1] #pega texto da caixa e remove /n final
		wordsList = wordsList.split(",")


		#cria a janela para mostrar o resultado dos testes
		self.respostasJanela = Toplevel(self.root,bg=bg1)
		self.respostasJanela.title("Resultados")
		self.respostasJanela.resizable(0,0)
		self.respostasJanela.minsize(250,0)


		textoResultados = ""
		#preenche a string de resultados
		for word in wordsList: #textWordsTxt returns a list of words from a given file
			textoResultados = self.afd.processWord(word)
			#checa se a palavra foi aceita (caso seja, a cor é verde, senão a cor é vermelha)
			if textoResultados.rfind("ACEITA") != -1:
				color = "green"
			else:
				color = "red"
			#empacota o resultado na subjanela de resultados, com a cor correspondente
			self.respostasLabel = Label(self.respostasJanela,text=textoResultados,font=("Sans Serif",13,'bold'),fg=color,bg=bg1,anchor=W)
			self.respostasLabel.pack(padx=(5,20),fill='x')

		#mantém o foco do programa na janela dos resultados até ela ser fechada
		self.respostasJanela.grab_set()

		#limpa a caixa antes de retornar
		self.caixaPalavras.delete('1.0', END)


	def limpaCaixa(self):
		self.caixaPalavras.delete('1.0', END)
	









