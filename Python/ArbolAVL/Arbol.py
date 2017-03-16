#--------------- Area de Imports --------------------------
import NodoArbol
NA= NodoArbol
import subprocess
#----------------------------------------------------------

class AVL(object):
	def __init__(self):
		self.root= None
		self.nivel=0
		self.f=None

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
		nodo.setIzquierda(self.RotacionIzquierda(nodo.getIzquierda()))
		return self.RotacionIzquierda(nodo)

	def RotacionDobleDerecha(self,nodo):
		nodo.setDerecha(self.RotacionDerecha(nodo.getDerecha()))
		return self.RotacionDerecha(nodo)

	def imprimir(self,nodo):
		#Creamos el Archivo
		self.f=open("C:\graficas\AVL.txt","w")
		#Escribimos en el archivo
		#----------------- Propiedades de la Grafica-------------------------------
		self.f.write("digraph Matriz{ bgcolor=gray \n")
		self.f.write("node [fontcolor=\"white\", height=0.5, color=\"white\"]\n")
		self.f.write("[shape=circle, style=filled, color=blue]")
		self.f.write("rankdir=UD \n")
		self.f.write("edge  [color=\"white\", dir=fordware]\n")
		#----------------- Fin Propiedades de la Grafica-------------------------------
		if nodo.getDerecha()!=None or nodo.getIzquierda()!=None:

			print "Raiz -"+str(nodo.getValor())+"- Raiz //// Nivel: "+ str(self.nivel)
			#Establecemos el nivel 1 
			self.nivel=1
			#Imprimimos primero los hijos izquierdos
			self.imprimirIzquierda(nodo)
			#Establecemos el nivel 1 
			self.nivel=1
			#Luego imprimimos los hijos derechos
			self.imprimirDerecho(nodo)
		else:
			self.f.write(str(nodo.getValor()))

		self.f.write("\n}")
		self.nivel=0

		subprocess.Popen("dot -Tpng C:\graficas\AVL.txt -o C:\graficas\AVL.png")
		
	def imprimirDerecho(self,derecho):

		nodoaux = derecho.getDerecha()

		iz = False

		aux2=nodoaux

		first=True

		while nodoaux!=None:

			print "Derecho -"+str(nodoaux.getValor())+"- Derecho //// Nivel: "+ str(self.nivel)

			if first==True:

				self.f.write(str(derecho.getValor())+"->"+str(nodoaux.getValor())+";\n")

				first=False

			else:
				self.f.write(str(aux2.getValor())+"->"+str(nodoaux.getValor())+";\n")


			
			if nodoaux.getIzquierda()!=None:

				self.nivel=self.nivel+1

				aux = self.nivel

				self.imprimirIzquierda(nodoaux)

				iz=True

			nodoaux=nodoaux.getDerecha()

			if iz ==False:

				self.nivel=self.nivel+1

			else:

				self.nivel=aux

				iz=False

	def imprimirIzquierda(self,izquierda):

		nodoaux = izquierda.getIzquierda()

		der=False

		aux2=nodoaux

		first=True

		while nodoaux!=None:

			print "Izquierdo -"+str(nodoaux.getValor())+"- Izquierdo //// Nivel: "+ str(self.nivel)

			if first==True:

				self.f.write(str(izquierda.getValor())+"->"+str(nodoaux.getValor())+";\n")

				first=False

			else:

				self.f.write(str(aux2.getValor())+"->"+str(nodoaux.getValor())+";\n")


			if aux2.getDerecha()!=None and nodoaux.getIzquierda()==None:

				aux = self.nivel

				self.imprimirDerecho(aux2)

			
			nodoaux=nodoaux.getIzquierda()


			if der ==False:

				self.nivel=self.nivel+1
			else:

				self.nivel=aux

				der=False

	def imprimirarbol(self):
		self.imprimir(self.root)
