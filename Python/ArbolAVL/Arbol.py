import NodoArbol
NA= NodoArbol


class AVL(object):
	def __init__(self):
		self.root= None

	def insertar(self, valor):
		self.root = self.insert(valor,self.root)

	def insert(self,valor,raiz):
		#Si no existe arbol, entoces creamos un nuevo nodo raiz
		if raiz==None:
			raiz=NA.NodoArbol()
			raiz.setValor(valor)

		#Si no compara el valor de la raiz con el valor que entra
			#Si el valor de la comparacion es menor a 0, entonces el valor se va
			#hacia el hijo izquierdo
		elif self.comparar(valor,raiz.getValor()) < 0:

			#Insertamos el valor en el nodo izquierdo
			raiz.setIzquierda(self.insert(valor,raiz.getIzquierda()))

			#si la suma de ambos hijos es 2 entonces el arbol esta desbalanceado
			if(self.altura(raiz.getIzquierda())-self.altura(raiz.getDerecha())==2):

				#Si el valor es menor entonces es una rotacion simple 
				if (self.comparar(valor,raiz.getIzquierda().valor())<0):

					#La raiz va obtener el valor de la rotacion
					raiz= self.RotacionIzquierda(raiz)

				#De lo contrario es una rotacion doble hacia la izquierda
				else:

					#La raiz va obtener el valor de la rotacion
					raiz= self.RotacionDobleIzquierda(raiz)


			#Si el valor de la comparacion es mayor a 0, entonces el valor se va
			#hacia el hijo derecho
		elif self.comparar(valor,raiz.getValor()) > 0:

			#Insertamos el valor en el nodo derecho
			raiz.setDerecha(self.insert(valor,raiz.getDerecha()))

			#si la suma de ambos hijos es 2 entonces el arbol esta desbalanceado
			if(self.altura(raiz.getDerecha())-self.altura(raiz.getIzquierda())==2):

				#Si el valor es mayor a 0 entonces es una rotacion doble
				if (self.comparar(valor,raiz.getDerecha().getValor())>0):

					#La raiz toma el valor de la rotacion hacia la derecha
					raiz= self.RotacionDerecha(raiz)

				#De lo contrario es una rotacion doble hacia la derecha
				else:

					#La raiz toma el valor de la rotacion doble hacia la derecha
					raiz= self.RotacionDobleDerecha(raiz)

		#Establecemos la altura del arbol
		raiz.setAltura(self.MAX(self.altura(raiz.getIzquierda()),self.altura(raiz.getDerecha()))+1)

		#Retornamos el valor que va tener la nueva raiz 
		return raiz

	def comparar(self,v1,v2):
		resultado= 0
		if v1<v2 :
			resultado=-1
		elif v1>v2:
			resultado=1
		else:
			resultado = 0 
		return resultado

	def altura(self,nodo):
		if nodo==None:
			return -1
		else:
			return nodo.altura

	def MAX(self,v1,v2):
		if v1>v2:
			return v1
		else:
			return v2

	def RotacionIzquierda(self,nodo):
		#Creamos un nodo auxiliar
		nodoaux= nodo.getIzquierda()
		#El hijo izquierdo del nodo va ser su propio nodo derecho
		nodo.setIzquierda(nodoaux.getDerecha())
		#Ahora para establecemos el hijo derecho del auxiliar como el nodo 
		nodoaux.setDerecha(nodo)
		#Establecemos la altura del nodo entrante
		nodo.setAltura(self.MAX(self.altura(nodo.getIzquierda()),self.altura(nodo.getDerecha()))+1)
		#Establecemos la altura 
		nodoaux.setAltura(self.MAX(self.altura(nodoaux.getIzquierda()),nodo.getAltura())+1)
		#Retornamos el nodo auxiliar para que sea la nueva raiz
		return nodoaux

	def RotacionDerecha(self,nodo):
		#Creamos un nodo auxiliar
		nodoaux= nodo.getDerecha()
		#El hijo izquierdo del nodo va ser su propio nodo derecho
		nodo.setDerecha(nodoaux.getIzquierda())
		#Ahora para establecemos el hijo derecho del auxiliar como el nodo 
		nodoaux.setIzquierda(nodo)
		#Establecemos la altura del nodo entrante
		nodo.setAltura(self.MAX(self.altura(nodo.getDerecha()),self.altura(nodo.getIzquierda()))+1)
		#Establecemos la altura 
		nodoaux.setAltura(self.MAX(self.altura(nodoaux.getDerecha()),nodo.getAltura())+1)
		#Retornamos el nodo auxiliar para que sea la nueva raiz
		return nodoaux

	def imprimir(self,nodo):
		nodoaux=nodo
		print "Raiz-"+str(nodoaux.getValor())
		nodoaux = nodoaux.getDerecha()
		while nodoaux!=None:
			print "Derecho-"+str(nodoaux.getValor())
			nodoaux=nodoaux.getDerecha()

		nodoaux = nodo.getIzquierda()
		while nodoaux!=None:

			print "Izquierda-"+str(nodoaux.getValor())
			nodoaux=nodoaux.getIzquierda()

	def imprimirarbol(self):
		self.imprimir(self.root)
