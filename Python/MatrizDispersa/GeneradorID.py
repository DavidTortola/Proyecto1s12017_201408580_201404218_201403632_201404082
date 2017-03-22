#Clase que genera un id de n caracteres alfanumericos al azar.

#Imports.
#--------
import ListaDobleH
LDH=ListaDobleH
import random
class GeneradorID(object):

	def __init__(self):
		self.valores = LDH.ListaDobleH()
		self.valores.agregar("1")
		self.valores.agregar("2")
		self.valores.agregar("3")
		self.valores.agregar("4")
		self.valores.agregar("5")
		self.valores.agregar("6")
		self.valores.agregar("7")
		self.valores.agregar("8")
		self.valores.agregar("9")
		self.valores.agregar("0")
		self.valores.agregar("a")
		self.valores.agregar("b")
		self.valores.agregar("c")
		self.valores.agregar("d")
		self.valores.agregar("e")
		self.valores.agregar("f")
		self.valores.agregar("g")
		self.valores.agregar("h")
		self.valores.agregar("i")
		self.valores.agregar("j")
		self.valores.agregar("k")
		self.valores.agregar("l")
		self.valores.agregar("m")
		self.valores.agregar("n")
		self.valores.agregar("o")
		self.valores.agregar("p")
		self.valores.agregar("q")
		self.valores.agregar("r")
		self.valores.agregar("s")
		self.valores.agregar("t")
		self.valores.agregar("u")
		self.valores.agregar("v")
		self.valores.agregar("w")
		self.valores.agregar("x")
		self.valores.agregar("y")
		self.valores.agregar("z")

	#Metodo principal, recibe un valor integer y devuelve una cadena de este valor de tamanio de carac alfanumericos.
	def generarID(self, valor):
		cadena = ""
		cont = 0
		while cont < valor:
			cont2 = 0
			num = random.randint(0,34)
			nodoAux = self.valores.getInicio()
			while nodoAux != None and cont2 <= num:
				nodoAux = nodoAux.getDerecha()
				cont2 = cont2 + 1
			cadena = cadena + nodoAux.getValor()
			cont = cont + 1
		return cadena
