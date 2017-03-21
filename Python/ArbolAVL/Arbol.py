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
					raiz= self.RotacionIzquierda(raiz)

				#De lo contrario es una rotacion doble hacia la izquierda
				else:

					#La raiz va obtener el valor de la rotacion
					raiz= self.RotacionDobleIzquierda(raiz)


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

	 	nodo = self.buscar(valor,self.root,None)
	 	self.restarAltura(nodo)
		self.match=False
		print nodo.getPapa().getValor()
		self.delete(nodo)

	def restarAltura(self, nodo):
		if nodo != None:
			nodo.setAltura(nodo.getAltura()-1)
			self.restarAltura(nodo.getIzquierda())
			self.restarAltura(nodo.getDerecha())


	def delete(self,nodo):

		if nodo.getDerecha() != None :
			derecha = True
			
		else :
			derecha = False

		if nodo.getIzquierda()!= None:
			izquierda = True
		else:
			izquierda = False 

		print derecha
		print izquierda

		if derecha == False and izquierda == False:
			print"Caso 1 "
			return self.caso1(nodo)
		if derecha != True and izquierda ==False:
			print"Caso 2 "
			return self.caso2(nodo)
		if derecha == False and izquierda != False:
			print"Caso 2 "
			return self.caso2(nodo)
		if derecha!= False and izquierda != False:
			print"Caso 3 "
			return self.caso3(nodo)

	def caso1(self,nodo):
		nodoaux= nodo.getPapa()

		izquierda = nodoaux.getIzquierda()
		derecha = nodoaux.getDerecha()
		if izquierda != None:
			if izquierda.getValor()== nodo.getValor():
				nodo.getPapa().setIzquierda(None)
		if derecha != None:
			if derecha.getValor()== nodo.getValor():
				nodo.getPapa().setDerecha(None)
		

		return False

	def caso2(self,nodo):

		hijoizquierdo = nodo.getPapa().getIzquierda()
		hijoderecho = nodo.getPapa().getDerecha()

		if nodo.getIzquierda()!= None:
			Actual =nodo.getIzquierda()
		else:
			Actual= nodo.getDerecha()


		if(hijoizquierdo==nodo):
			nodo.getPapa().setIzquierda(Actual)
			Actual.setPapa(nodo.getPapa())
			nodo.setDerecha(None)
			nodo.setIzquierda(None)

			return True

		if hijoderecho==nodo:
			nodo.getPapa().setDerecha(Actual)
			Actual.setPapa(nodo.getPapa())
			nodo.setDerecha(None)
			nodo.setIzquierda(None)
			return True

		return False

	def caso3(self, nodo):

		ultimoizquierda = self.recorrerIzquierda(nodo.getDerecha())
		if ultimoizquierda!= None:
			nodo.setValor(ultimoizquierda.getValor())
			self.delete(ultimoizquierda)

			return True

		return False

	def recorrerIzquierda(self, nodo):
		if nodo.getIzquierda()!=None:
			return recorrerIzquierda(nodo.getIzquierda())

		return nodo 


	def buscar(self,valor, nodo,padre):
		if nodo!= None:
			if padre == None:

				if valor > nodo.getValor() :
					self.buscar(valor,nodo.getDerecha(),nodo)
				else:
					self.buscar(valor, nodo.getIzquierda(),nodo)
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



'''	def delete(self,valor,nodo,padre):
		if nodo!= None:
			if padre == None:

				self.delete(valor,nodo.getDerecha(),nodo)
				self.delete(valor, nodo.getIzquierda(),nodo)
				
			else:
				
				if valor == nodo.getValor():
					print nodo.getValor()
					print "Hizo match "
					self.match=True
					if nodo.getDerecha()!=None:
						print "Hay nodo derecha, se puede subir"
						nodoaux = nodo
						
						
						if padre.getDerecha() == nodo :
							nodo = nodo.getDerecha() 
							padre.setDerecha(nodo)
							nodo.setIzquierda(nodoaux.getIzquierda())
						else:
							nodo = nodo.getIzquierda() 
							padre.setIzquierda(nodo)
							nodo.setDerecha(nodoaux.getDerecha())

					elif nodo.getIzquierda()!= None:
						print "hay nodo izquierda, se puede subir"
					else:
						print "Es hoja"
				else:
					if self.match!=True:
						self.delete(valor,nodo.getDerecha(),nodo)
						self.delete(valor, nodo.getIzquierda(),nodo)
						

'''


			