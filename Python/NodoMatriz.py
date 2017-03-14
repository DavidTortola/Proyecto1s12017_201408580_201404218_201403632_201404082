#Clase nodo para la matriz dispersa, con cuatro apuntadores y un valor.

class NodoMatriz(object):

	#Metodos constructor.
	#-------------------

	def __init__(self, valor = None, derecha = None, izquierda = None, arriba = None, abajo = None, x = None, y = None):
		self.valor = valor   	   #Campo para almacenar el valor del nodo.
		self.derecha = derecha     #Apuntador hacia la derecha.
		self.izquierda = izquierda #Apuntador hacia la izquierda.
		self.arriba = arriba       #Apuntador hacia arriba.
		self.abajo = abajo         #Apuntador hacia abajo.
		self.x = x                 #Campo con la posicion x del nodo.
		self.y = y                 #Campo con la posicion y del nodo.

	#Metodos sets y gets para los campos.
	#------------------------------------

	def getValor(self):
		return self.valor

	def setValor(self, val):
		self.valor = val

	def getDerecha(self):
		return self.derecha

	def setDerecha(self, val):
		self.derecha = val

	def getIzquierda(self):
		return self.izquierda

	def setIzquierda(self, val):
		self.izquierda = val

	def getArriba(self):
		return self.arriba

	def setArriba(self, val):
		self.arriba = val

	def getAbajo(self):
		return self.abajo

	def setAbajo(self, val):
		self.abajo = val

	def getX(self):
		return self.x

	def setX(self, val):
		self.x = val

	def getY(self):
		return self.y

	def setY(self, val):
		self.y = val