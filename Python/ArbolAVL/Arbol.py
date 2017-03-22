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
		self.match=False 
		self.retorno =None	

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
		self.EnlazarPapas(self.root,None)

	def insert(self,valor,raiz):
		#Si no existe arbol, entoces creamos un nuevo nodo raiz
		if raiz == None:
			raiz = NA.NodoArbol()
			raiz.setValor(valor)

		#Si no compara el valor de la raiz con el valor que entra
			#Si el valor de la comparacion es menor a 0, entonces el valor se va
			#hacia el hijo izquierdo
		elif self.comparar(valor,raiz.getValor()) < 0:

			nodoaux= self.insert(valor,raiz.getIzquierda())

			#Insertamos el valor en el nodo izquierdo
			raiz.setIzquierda(nodoaux)


			#si la suma de ambos hijos es 2 entonces el arbol esta desbalanceado
			if(self.altura(raiz.getDerecha())-self.altura(raiz.getIzquierda()) == -2):

				#Si el valor es menor entonces es una rotacion simple 
				if (self.comparar(valor,raiz.getIzquierda().getValor())<0):

					#La raiz va obtener el valor de la rotacion
					raiz = self.RotacionIzquierda(raiz)

				#De lo contrario es una rotacion doble hacia la izquierda
				else:

					#La raiz va obtener el valor de la rotacion
					raiz = self.RotacionDobleIzquierda(raiz)


			#Si el valor de la comparacion es mayor a 0, entonces el valor se va
			#hacia el hijo derecho
		elif self.comparar(valor,raiz.getValor()) > 0:

			nodoaux= self.insert(valor,raiz.getDerecha())
			#Insertamos el valor en el nodo derecho
			raiz.setDerecha(nodoaux)


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


	def EnlazarPapas(self,nodo,padre):
		nodo.setPapa(padre)
		if nodo!= None:
			if nodo.getDerecha()!= None :
				self.EnlazarPapas(nodo.getDerecha(),nodo)
			if nodo.getIzquierda()!= None :
				self.EnlazarPapas(nodo.getIzquierda(),nodo)

	#Metodo que compara dos entradas, si se usan letras compara el ASCII.
	def comparar(self,v1,v2):
		resultado= 0
		if v1<v2 :
			resultado=-1
		elif v1>v2:
			resultado=1
		else:
			resultado = 0 
		return resultado

	#Obtiene la altura de un nodo.
	def altura(self,nodo):
		if nodo==None:
			return -1
		else:
			return nodo.altura

	#Devuelve el valor que es mayor, si se usan letras compara el ASCII.
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
		nodoaux.setAltura(self.MAX(self.altura(nodoaux.getIzquierda()), nodo.getAltura())+1)
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

	#Grafica el arbol
	def impreArbol(self, nodo, padre):
		if nodo != None:
			if padre == None:
				#Creamos el Archivo
				self.f=open("Graficas\AVL.txt","w")
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
				subprocess.Popen("dot -Tpng Graficas\AVL.txt -o Graficas\AVL.png")
			else:
				self.f.write(str(padre.getValor()) +"->" +str(nodo.getValor()) +";\n")
				self.impreArbol(nodo.getIzquierda(), nodo)
				self.impreArbol(nodo.getDerecha(), nodo)


	def eliminar(self,valor):
		#Busco el nodo a eliminar
	 	nodo = self.buscar(valor,self.root,None)
		self.match=False #Se renueva la bandera para buscar
		self.EnlazarPapas(self.root,None)
		#Se elimina el nodo
		self.delete(nodo)


	def delete(self,nodo):

		if nodo.getDerecha() != None :
			derecha = True
			
		else :
			derecha = False

		if nodo.getIzquierda()!= None:
			izquierda = True
		else:
			izquierda = False 


		if derecha == False and izquierda == False:

			return self.caso1(nodo)
		if derecha != False and izquierda ==False:

			return self.caso2(nodo)
		if derecha == False and izquierda != False:

			return self.caso2(nodo)
		if derecha!= False and izquierda != False:

			return self.caso3(nodo)

	def caso1(self, nodo):

		if nodo.getPapa() == None:	#Si se va a eliminar la raiz
			self.root = None

		else:
			#Se obtiene el papa, se obtienen sus hijos
			nodoPapa = nodo.getPapa()
			izquierda = nodoPapa.getIzquierda()
			derecha = nodoPapa.getDerecha()

			#Se elimina el hijo con el valor que se quiere borrar
			if izquierda != None:
				if izquierda.getValor() == nodo.getValor():
					nodo.getPapa().setIzquierda(None)


			if derecha != None:
				if derecha.getValor() == nodo.getValor():
					nodo.getPapa().setDerecha(None)
			self.colocarAlturas(self.root)
		return False

	def caso2(self,nodo):

		if nodo.getPapa()!=None:
			hijoizquierdo = nodo.getPapa().getIzquierda()
			hijoderecho = nodo.getPapa().getDerecha()

			if nodo.getIzquierda() != None:
				Actual = nodo.getIzquierda()
			else:
				Actual = nodo.getDerecha()

			if hijoizquierdo == nodo:
				nodo.getPapa().setIzquierda(Actual)
				Actual.setPapa(nodo.getPapa())
				self.colocarAlturas(self.root)
				return True

			if hijoderecho == nodo:
				nodo.getPapa().setDerecha(Actual)
				Actual.setPapa(nodo.getPapa())
				self.colocarAlturas(self.root)
				return True
		else:

			der = nodo.getDerecha()
			iz = nodo.getIzquierda()
			if der!=None:
				self.root = der
				der.setPapa(None)
			elif iz!=None:
				self.root = iz
				iz.setPapa(None)
			self.colocarAlturas(self.root)
		self.colocarAlturas(self.root)
		return False

	def caso3(self, nodo):

		#Obtiene el ultimo a la izquierda
		ultimoizquierda = self.recorrerIzquierda(nodo.getDerecha())

		if ultimoizquierda == nodo.getDerecha():
			ultimoizquierda = None

		if ultimoizquierda != None: #Si el nodo derecha tiene hijo izquierdo.

			if nodo.getPapa() == None:
				self.root = ultimoizquierda
			else:

				if nodo.getPapa().getDerecha() == nodo:
					nodo.getPapa().setDerecha(ultimoizquierda)
				elif nodo.getPapa().getIzquierda() == nodo:
					nodo.getPapa().setIzquierda(ultimoizquierda)

			ultimoizquierda.getPapa().setIzquierda(None)

			ultimoizquierda.setIzquierda(nodo.getIzquierda())
			ultimoizquierda.setDerecha(nodo.getDerecha())
			ultimoizquierda.setPapa(nodo.getPapa())

			nodo.getIzquierda().setPapa(ultimoizquierda)
			nodo.getDerecha().setPapa(ultimoizquierda)

			self.colocarAlturas(self.root)
			return True

		else:	#Si el nodo derecha no tiene hijo izquierdo.
			nodoDerecho = nodo.getDerecha()

			if nodo.getPapa() == None:
				self.root = nodoDerecho
			else:
				if nodo.getPapa().getDerecha() == nodo:
					nodo.getPapa().setDerecha(nodoDerecho)
				elif nodo.getPapa().getIzquierda() == nodo:
					nodo.getPapa().setIzquierda(nodoDerecho)

			nodoDerecho.setPapa(nodo.getPapa())
			nodoDerecho.setIzquierda(nodo.getIzquierda())
			self.colocarAlturas(self.root)
		return False

	def recorrerIzquierda(self, nodo):
		if nodo.getIzquierda()!=None:
			return self.recorrerIzquierda(nodo.getIzquierda())

		return nodo 


	def buscar(self, valor, nodo, padre):
		if nodo!= None:
			if padre == None:

				if valor > nodo.getValor() :
					self.buscar(valor,nodo.getDerecha(),nodo)
				elif valor < nodo.getValor() :
					self.buscar(valor, nodo.getIzquierda(),nodo)
				else:
					self.retorno = nodo
					return self.retorno

			else:
				if valor == nodo.getValor():

					print "Hizo match "
					self.match=True
					self.retorno = nodo

				else:
					if self.match!=True:
						if valor > nodo.getValor() :
							self.buscar(valor,nodo.getDerecha(),nodo)
						else:

							self.buscar(valor, nodo.getIzquierda(),nodo)
		return self.retorno

	def colocarAlturas(self, nodo):
		nodo.obtenerAltura()