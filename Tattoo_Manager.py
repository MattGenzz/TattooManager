class Evento():
	def __init__(self):
		self.nome = ""
		self.descricao = ""
		self.valor = 0
		self.data = ""
		self.local = ""
		
	def inserir(self):
		self.nome = str(input("Insira o nome do cliente: "))
		self.descricao = str(input("Insira a descrição da tattoo do cliente: "))
		self.valor = input("Insira o valor da tattoo: ")
		self.data = str(input("Insira a data do evento: "))
		self.local = str(raw_input("Insira o local do evento: "))
		
	def salvar(self):
		import os
		
		if os.path.isfile("banco.csv"):
			##salva
		else:
			with open("banco.csv",'w+') as arq:
				arq.write(str(self.nome))
				arq.write(str(self.descricao))
				arq.write(str(self.valor))
				arq.write(str(self.data))
				arq.write(str(self.local))