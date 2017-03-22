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

	def obtenerAltura(self):
		val1 = None
		val2 = None
		
		if self.izquierda != None:
			val1 = self.izquierda.obtenerAltura()
		
		if self.derecha != None:
			val2 = self.derecha.obtenerAltura()

		if val1 != None and val2 != None:

			if val1 < val2:
				self.altura = val2 + 1
			elif val1 > val2:
				self.altura = val1 + 1
			else:
				self.altura = val1 + 1
		
		else:

			if val1 != None:
				self.altura = val1+1
			elif val2 != None:
				self.altura = val2+1
			else:
				self.altura = 0
		return self.altura


	def getFE(self):
		val1 = 0
		val2 = 0
		fe = 0
		if self.izquierda != None:
			val1 = self.izquierda.getAltura()
		if self.derecha != None:
			val2 = self.derecha.getAltura()

		return (val2-val1)