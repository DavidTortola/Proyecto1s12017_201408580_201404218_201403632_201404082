#Nodo con parametros para estructuras tipo arbol.

class NodoArbol(object):
	
	#Metodos constructor.
	#--------------------
	def __init__(self, valor = None, izquierda = None, dererecha = None, fe = 0):
		self.valor = valor
		self.izquierda = izquierda
		self.derecha = derecha
		self.fe = fe


	#Metodos sets y gets.
	#--------------------

	def getValor(self):
		return self.valor

	def setValor(self, val):
		self.valor = val

	def getIzquierda(self):
		return self.izquierda

	def setIzquierda(self, val):
		self.izquierda = val

	def getDerecha(self):
		return self.derecha

	def setDerecha(self, val):
		self.derecha = val

	def getFe(self):
		return self.fe

	def setFe(self, val):
		self.fe = val