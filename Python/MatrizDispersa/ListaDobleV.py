#Clase lista doble de forma vertical (agrega nodos de arriba a abajo).



#Importaciones.
#--------------

import NodoMatriz  #Se utilizan nodos tipo matriz en la lista doble.
nm = NodoMatriz

class ListaDobleV():



	#Metodos constructor.
	#-------------------

	def __init__(self, inicio = None, fin = None, tamanio = 0):
		self.inicio = None
		self.fin = None
		self.tamanio = 0



	#Metodos sets y gets.
	#--------------------

	def getInicio(self):
		return self.inicio

	def setInicio(self, val):
		self.inicio = val

	def getFin(self):
		return self.fin

	def setFin(self, val):
		self.fin = val

	def getTamanio(self):
		return self.tamanio

	def setTamanio(self, val):
		self.tamanio = val



	#Metodos de la lista doble.
	#--------------------------

	#Devuelve true o false si la lista es vacia o no.
	def esVacia(self):   
		if self.tamanio == 0:
			return True
		else:
			return False

    #Inserta nuevo nodo en la lista.
	def agregar(self, val):   
		nuevoNodo = nm.NodoMatriz(val)   #Se crea el nodo a insertar.
		if self.esVacia() == True:		   #Si es vacia se agrega primero.
			self.inicio = nuevoNodo
			self.fin = nuevoNodo
		else:							
			self.insertarEnOrden(nuevoNodo)	   #Si ya hay elementos, se agrega en orden alfabetico.
		self.tamanio = self.tamanio + 1	   #Se aumenta en uno el tamanio de la lista.

	#Recorre la lista e inserta alfabeticamente.
	def insertarEnOrden(self, nuevoNodo):

		nodoAux = self.inicio   #Crea un auxiliar para recorrer la lista.
		insertado = False       #Boolean para saber si se inserto al recorrer.

		while nodoAux != None:  #Recorre la lista utilizando el nodo auxiliar.

			if self.esMayor(nuevoNodo.getValor(), nodoAux.getValor()) == True:  #Si es mayor el valor a insertar sigue recorriendo.

				nodoAux = nodoAux.getAbajo()

			else:   #Si el valor a insertar es menor que el actual, inserta enmedio de la lista.

				if nodoAux == self.inicio:   #Si el valor actual es inicio, se inserta el nuevo valor al principio.

					nuevoNodo.setAbajo(nodoAux)
					nodoAux.setArriba(nuevoNodo)
					self.inicio = nuevoNodo

					insertado = True
					break

				else:   #Si el noddo actual esta en medio de la lista, el nuevo nodo se inserta en medio de la lista.

					nuevoNodo.setArriba(nodoAux.getArriba())
					nodoAux.getArriba().setAbajo(nuevoNodo)
					nuevoNodo.setAbajo(nodoAux)
					nodoAux.setArriba(nuevoNodo)

					insertado = True
					break

		if insertado == False:	#Si no se inserto el nuevo nodo al recorrer la lista, se inserta al final de ella.
			self.fin.setAbajo(nuevoNodo)
			nuevoNodo.setArriba(self.fin)
			self.fin = nuevoNodo

	#Recibe dos valores y devuelve true si val1 es mayor alfabeticamente.
	def esMayor(self, val1, val2):
		contador = 1
		letraInsertar = ord(val1[:contador])
		letraComparar = ord(val2[:contador])
		if letraInsertar > letraComparar:
			return True
		elif letraInsertar < letraComparar:
			return False
		else:
			#Si la primer letra es la misma, recorre los strings hasta encontrar una diferencia.
			while letraComparar != None and letraInsertar != None:
				contador = contador + 1
				letraInsertar = val1[:contador]
				letraInsertar = ord(letraInsertar[-1:])
				letraComparar = val2[:contador]
				letraComparar = ord(letraComparar[-1:])
				if letraInsertar > letraComparar:
					return True
				elif letraInsertar < letraComparar:
					return False
				else:
					if len(val1) < contador and len(val2) < contador:	#Si el contador es mayor al tamanio es porque son iguales las palabras
						return True

	#Recorre e imprime en consola la lista doble.
	def imprimirLista(self):
		nodoAux = self.inicio
		while nodoAux != self.fin.getAbajo():
			print str(nodoAux.getValor())
			nodoAux = nodoAux.getAbajo()

	#Busca un valor en la lista y devuelve el nodo que hace match, si lo encuentra.
	def buscar(self, val):

		if self.esVacia() == False:

			nodoAux = self.inicio
			while nodoAux != self.fin.getAbajo():
				if nodoAux.getValor() == val:
					return nodoAux
				nodoAux = nodoAux.getAbajo()
		return None

	def eliminar(self, valor):
		if self.esVacia()==False:
			nodoAux=self.inicio
			while nodoAux!=self.fin.getAbajo():
				if nodoAux.getValor() == valor:
					#Eliminar
					#Si es el primer nodo en la lista
					if nodoAux == self.inicio:
						#Si existe un nodo siguiente
						if nodoAux.getAbajo() != None:
							self.inicio = nodoAux.getAbajo()
							nodoAux.getAbajo().setArriba(None)
							self.tamanio = self.tamanio - 1
							break
						#Si es el unico nodo en la lista
						else:
							self.inicio = None
							self.fin = None
							self.tamanio = 0
							break
					#Si es el ultimo nodo en la lista
					elif nodoAux == self.fin:
						#Si existe un nodo anterior (no es el unico nodo en la lista)
						if nodoAux.getArriba() != None:
							self.fin = nodoAux.getArriba()
							nodoAux.getArriba().setDerecha(None)
							self.tamanio = self.tamanio - 1
							break
						#Si no existe un nodo anterior
						else:
							self.inicio = None
							self.fin = None
							self.tamanio = 0
							break
					#Si no es ni el primero ni el ultimo
					else:
						nodoAux.getArriba().setDerecha(nodoAux.getAbajo())
						nodoAux.getAbajo().setArriba(nodoAux.getArriba())
						self.tamanio=self.tamanio - 1
						break
				else:
					nodoAux = nodoAux.getAbajo()