#--------------- Area de Imports --------------------------
import NodoArbol
NA= NodoArbol
import subprocess
#----------------------------------------------------------

class AVL(object):

	#Metodos constructor.
	#--------------------
	def __init__(self, root = None, nivel = 0, f = None):
		self.root = root
		self.nivel = nivel
		self.f = f

	#Metodos sets y gets.
	#--------------------

	def getRoot(self):
		return self.root

	def setRoot(self, val):
		self.root = val

	def getNivel(self):
		return self.nivel

	def setNivel(self, val):
		self.nivel = val

	def getF(self):
		return self.f

	def setF(self, val):
		self.f = val



	#Acciones.
	#---------

	def insertar(self, valor):
		self.root = self.insert(valor,self.root)

	def insert(self,valor,raiz):
		#Si no existe arbol, entoces creamos un nuevo nodo raiz
		if raiz == None:
			raiz = NA.NodoArbol()
			raiz.setValor(valor)

		#Si no compara el valor de la raiz con el valor que entra
			#Si el valor de la comparacion es menor a 0, entonces el valor se va
			#hacia el hijo izquierdo
		elif self.comparar(valor,raiz.getValor()) < 0:

			#Insertamos el valor en el nodo izquierdo
			raiz.setIzquierda(self.insert(valor,raiz.getIzquierda()))

			#si la suma de ambos hijos es 2 entonces el arbol esta desbalanceado
			if(self.altura(raiz.getDerecha())-self.altura(raiz.getIzquierda()) == -2):

				#Si el valor es menor entonces es una rotacion simple 
				if (self.comparar(valor,raiz.getIzquierda().getValor())<0):

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
			if(self.altura(raiz.getDerecha()) - self.altura(raiz.getIzquierda()) == 2):

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
		nodoaux = nodo.getIzquierda()
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
		nodoaux = nodo.getDerecha()
		#El hijo derecho del nodo va ser su propio nodo izquierdo
		nodo.setDerecha(nodoaux.getIzquierda())
		#Ahora para establecemos el hijo izquierdo del auxiliar como el nodo 
		nodoaux.setIzquierda(nodo)
		#Establecemos la altura del nodo entrante
		nodo.setAltura(self.MAX(self.altura(nodo.getDerecha()),self.altura(nodo.getIzquierda()))+1)
		#Establecemos la altura 
		nodoaux.setAltura(self.MAX(self.altura(nodoaux.getDerecha()),nodo.getAltura())+1)
		#Retornamos el nodo auxiliar para que sea la nueva raiz
		return nodoaux

	def RotacionDobleIzquierda(self,nodo):
		nodo.setIzquierda(self.RotacionDerecha(nodo.getIzquierda()))
		return self.RotacionIzquierda(nodo)

	def RotacionDobleDerecha(self,nodo):
		nodo.setDerecha(self.RotacionIzquierda(nodo.getDerecha()))
		return self.RotacionDerecha(nodo)

	def impreArbol(self, nodo, padre):
		if nodo != None:
			if padre == None:
				#Creamos el Archivo
				self.f=open("C:\graficas\AVL.txt","w")
				#Escribimos en el archivo
				#----------------- Propiedades de la Grafica-------------------------------
				self.f.write("digraph Matriz{ bgcolor=gray \n")
				self.f.write("node [fontcolor=\"white\", height=0.5, color=\"white\"]\n")
				self.f.write("[shape=circle, style=filled, color=blue]")
				self.f.write("rankdir=UD \n")
				self.f.write("edge  [color=\"white\", dir=fordware]\n")
				self.f.write(str(nodo.getValor()) +";\n")
				self.impreArbol(nodo.getIzquierda(), nodo)
				self.impreArbol(nodo.getDerecha(), nodo)
				self.f.write("}")
				self.f.close()
				subprocess.Popen("dot -Tpng C:\graficas\AVL.txt -o C:\graficas\AVL.png")
			else:
				self.f.write(str(padre.getValor()) +"->" +str(nodo.getValor()) +";\n")
				self.impreArbol(nodo.getIzquierda(), nodo)
				self.impreArbol(nodo.getDerecha(), nodo)
			