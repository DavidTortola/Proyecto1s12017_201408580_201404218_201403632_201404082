#Clase nodo para arboles AVL.

class NodoArbol(object):

	#Metodos construcor.
	#-------------------

	def __init__(self, raiz = None, derecha = None, izquierda = None, valor = None, altura = 0, papa= None):
		self.raiz=raiz
		self.derecha=derecha
		self.izquierda=izquierda
		self.valor=valor
		self.altura=altura
		self.papa = papa
	#Metodos sets y gets.
	#--------------------

	def setValor(self, valor):
		self.valor=valor
	def setDerecha(self,derecha):
		self.derecha=derecha
	def setIzquierda(self,izquierda):
		self.izquierda=izquierda
	def setRaiz(self,raiz):
		self.raiz=raiz
	def setAltura(self,altura):
		self.altura=altura
	def setPapa(self,papa):
		self.papa= papa

	def getPapa(self):
		return self.papa
	def getValor(self):
		return self.valor
	def getDerecha(self):
		return self.derecha
	def getIzquierda(self):
		return self.izquierda
	def getRaiz(self):
		return self.raiz
	def getAltura(self):
		return self.altura