class NodoArbol(object):
	def __init__(self):
		self.raiz=None
		self.derecha=None
		self.izquierda=None
		self.valor=None
		self.altura=0
	
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


