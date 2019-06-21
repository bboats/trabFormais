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
from tkinter import *
from tkinter import filedialog

options = ['Carregar um automato a partir de um .txt','Testar palavras a partir de um .txt','Testar uma palavra a partir do teclado']


mainMenu = menu.Menu(options,'- no language -')

root = Tk()
root.geometry("500x400")
root.resizable(0,0)

titleFrame = Frame(root,bg="gray",height=50,width=600)
titleFrame.pack(side="top",fill='x')
leftFrame = Frame(root,bg="gray",width=300,height=350)
leftFrame.pack(side="left",fill='both')
leftFrame.pack_propagate(0)
rightFrame = Frame(root,bg="gray",width=200,height=350)
rightFrame.pack(side="right",fill='both')
rightFrame.pack_propagate(0)

def testPrint():
	print("olar sou um botao")
	title['text'] = "Mudou"
	title.pack()

def limpaCaixa():
	caixaPalavras.delete('1.0', END)

def nothing():
	pass

######################
##########CABECALHO##########
######################

title = Label(titleFrame,text="AUTOMATO NAO CARREGADO!", font=("Helvetica",16),bg="gray",fg="red")
title.pack(fill="x",expand=1,pady=(5,0))

#############################


######################
#####LADO ESQUERDO#########
######################

###Botão para abrir txt da linguagem###
abrirLinguagem = Button(leftFrame,text="Abrir Linguagem",command=testPrint,font=("Sans Serif",16))
abrirLinguagem.pack(pady=(30,30),ipadx=50)

###Botão para abrir txt das palavras###
abrirPalavras = Button(leftFrame,text="Testar Palavras de um .Txt",command=nothing,font=("Sans Serif",16))
abrirPalavras.pack()

####Caixa de input manual e seus botões####
caixaPalavras = Text(leftFrame,height=9,width=33,borderwidth=6,relief=RIDGE)
caixaPalavras.insert(END, ' Insira palavras separadas aqui!\n    (Separadas por virgula)')
caixaPalavras.pack(pady=(20,5))

###Botão submit p/ caixa de input
enviaPalavras = Button(leftFrame,text="Testar as palavras!",command=nothing)
enviaPalavras.pack(side="left",anchor="n",padx=(30,80))

###Botão clear p/ caixa de input
limpaPalavras = Button(leftFrame,text="Clear",command=limpaCaixa)
limpaPalavras.pack(side="left",anchor="n")


######################

######################
#####LADO DIREITO#####
######################

#imagem de enfeite
img = PhotoImage(file="images/faustao.png")
teste = Label(rightFrame, image=img)
teste.img = img
teste['bg'] = teste.master['bg']
teste.pack(pady=(30,0))



#botao para fechar o programa
exitButton = Button(rightFrame,text="Sair",command=root.quit)
exitButton.pack(ipadx=50,pady=(20,20),side="bottom")

######################






### THIS OPENS A FILE AND ITS AWESOME AND COMPLETE!!!!
#print( filedialog.askopenfilename(initialdir="/",title="Escolha o arquivo de linguagem",filetypes=(("text files","*.txt"),("all files","*.*"))))

root.mainloop()


'''
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

'''