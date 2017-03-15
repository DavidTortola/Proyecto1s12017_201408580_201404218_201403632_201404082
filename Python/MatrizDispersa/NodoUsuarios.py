class NodoUsuarios(object):
	def __init__(self, valor = None, letra = None, dominio = None, siguiente = None, anterior = None, arriba = None, abajo = None):
		self.siguiente = siguiente
		self.anterior = anterior
		self.arriba = arriba
		self.abajo = abajo
		self.dato = valor
		self.letra = letra
		self.dominio = dominio

	def getSiguiente(self):
		return self.siguiente
	def setSiguiente(self, valorAux):
		self.siguiente = valorAux
	def getAnterior(self):
		return self.anterior
	def setAnterior(self, valorAux):
		self.anterior = valorAux
	def getArriba(self):
		return self.arriba
	def setArriba(self, valorAux):
		self.arriba = valorAux
	def getAbajo(self):
		return self.abajo
	def setAbajo(self, valorAux):
		self.abajo = valorAux

	
	def setValor(self,dato):
		self.dato=dato
		
	def getValor(self):
		return self.dato

	def getPrimero(self):
		return self.primero

	def setPrimero(self,primero):
		self.primero=primero

	def getUltimo(self):
		return self.ultimo

	def setUltmio(self,ultimo):
		return self.ultimo

	def getLetra(self):
		return self.letra

	def setLetra(self, valorAux):
		self.letra = valorAux

	def getDominio(self):
		return self.dominio

	def setDominio(self, valorAux):
		self.dominio = valorAux
