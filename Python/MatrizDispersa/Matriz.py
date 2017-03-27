#----------------------------------Area de Importaciones-----------------------------
import Listausuarios
LN=Listausuarios
import ListaDobleV
LDV=ListaDobleV
import ListaDobleH
LDH=ListaDobleH
import NodoMatriz
nm=NodoMatriz
import subprocess
#------------------------------------------------------------------------------------

class Matriz(object):
	def __init__(self):
		self.ListaVertical=None
		self.ListaHorizontal = None
		self.ListaUsuarios= None
		self.tamano = 0

	#Metodo para insertar
	def agregar(self,departamento,empresa,valor):
		if self.tamano ==0:
			self.ListaVertical=LDV.ListaDobleV()
			self.ListaHorizontal=LDH.ListaDobleH()

			ListaUsuarios=LN.Nombres()

			ListaUsuarios.insertar(valor)

			Nodo=nm.NodoMatriz(ListaUsuarios,departamento,empresa)

			self.ListaHorizontal.agregar(empresa)
			self.ListaVertical.agregar(departamento)

			AuxiliarVertical=self.ListaVertical.buscar(departamento)
			AuxiliarHorizontal=self.ListaHorizontal.buscar(empresa)


			AuxiliarVertical.setDerecha(Nodo)
			AuxiliarHorizontal.setAbajo(Nodo)

			Nodo.setArriba(AuxiliarHorizontal)
			Nodo.setIzquierda(AuxiliarVertical)

			self.tamano=self.tamano+1

		elif self.tamano>0:

			if self.ListaVertical.buscar(departamento)!=None and self.ListaHorizontal.buscar(empresa)!=None:
				self.Existen(departamento,empresa,valor)

			elif self.ListaHorizontal.buscar(empresa)==None and self.ListaVertical.buscar(departamento)!=None:
				self.ExisteVertical(departamento,empresa,valor)

			elif self.ListaHorizontal.buscar(empresa)!=None and self.ListaVertical.buscar(departamento)==None:
				self.ExisteHorizontal(departamento,empresa,valor)				

			elif self.ListaHorizontal.buscar(empresa)==None and self.ListaVertical.buscar(departamento)==None:
				self.NoExisten(departamento,empresa,valor)
				
			self.tamano=self.tamano+1




	#Metodo para insertar cuando existen ambas cabeceras
	def Existen(self,departamento,empresa,valor):

		if self.Comparar(departamento,empresa)==True:

			NodoAuxiliarHorizontal= self.ListaHorizontal.buscar(empresa)
			NodoAux =NodoAuxiliarHorizontal

			while NodoAux!=None:

				if NodoAux.getY()==departamento:
					NodoAuxiliarHorizontal=NodoAux
					NodoAux=NodoAux.getAbajo()
				else:
					NodoAux=NodoAux.getAbajo()
			ListaUsuarios=NodoAuxiliarHorizontal.getValor()
			ListaUsuarios.insertar(valor)


		else:
			NodoAuxiliarHorizontal= self.ListaHorizontal.buscar(empresa)
			NodoAux = NodoAuxiliarHorizontal.getAbajo()

			ListaUsuarios=LN.Nombres()
			ListaUsuarios.insertar(valor)


			Nodo=nm.NodoMatriz(ListaUsuarios,departamento,empresa)
			letrainsertar=departamento[:1]
			letrainsertar=ord(letrainsertar)

			agregado = False
			while NodoAux !=None:

				letracomparar= NodoAux.getY()[:1]
				letracomparar=ord(letracomparar)
				if letrainsertar>letracomparar:
					NodoAux=NodoAux.getAbajo()
				else:
					Nodo.setAbajo(NodoAux)
					Nodo.setArriba(NodoAux.getArriba())
					NodoAux.getArriba().setAbajo(Nodo)
					NodoAux.setArriba(Nodo)
					agregado=True
					break
			if agregado==False:
				NodoAux= NodoAuxiliarHorizontal.getAbajo()
				while NodoAux.getAbajo()!=None:
					NodoAux=NodoAux.getAbajo()

				Nodo.setArriba(NodoAux)
				NodoAux.setAbajo(Nodo)

			NodoAuxiliarVertical= self.ListaVertical.buscar(departamento)
			NodoAux2= NodoAuxiliarVertical.getDerecha()

			letrainsertar=empresa[:1]
			letrainsertar=ord(letrainsertar)

			agregado=False
			while NodoAux2!=None:
				letracomparar=NodoAux2.getX()[:1]
				letracomparar=ord(letracomparar)

				if letrainsertar>letracomparar:
					NodoAux2=NodoAux2.getDerecha()
				else:
					Nodo.setDerecha(NodoAux2)
					Nodo.setIzquierda(NodoAux2.getIzquierda())
					NodoAux2.getIzquierda().setDerecha(Nodo)
					NodoAux2.setIzquierda(Nodo)
					agregado=True
					break 
			if agregado ==False:
				NodoAux2=NodoAuxiliarVertical.getDerecha()
				while NodoAux2.getDerecha()!=None:
					NodoAux2=NodoAux2.getDerecha()
					Nodo.setIzquierda(NodoAux2)
				NodoAux2.setDerecha(Nodo)

	#Metodo para instertar cuando existe la cabecera horizontal
	def ExisteHorizontal(self,departamento,empresa,valor):
		self.ListaVertical.agregar(departamento)

		NodoAuxiliarHorizontal=self.ListaHorizontal.buscar(empresa)
		NodoAux=NodoAuxiliarHorizontal.getAbajo()

		ListaUsuarios=LN.Nombres()
		ListaUsuarios.insertar(valor)

		Nodo=nm.NodoMatriz(ListaUsuarios,departamento,empresa)

		letrainsertar=departamento[:1]
		letrainsertar=ord(letrainsertar)
		agregado = False
		while NodoAux !=None:

			letracomparar= NodoAux.getY()[:1]
			letracomparar=ord(letracomparar)

			if letrainsertar>letracomparar:
				NodoAux=NodoAux.getAbajo()
			else:
				Nodo.setAbajo(NodoAux)
				Nodo.setArriba(NodoAux.getArriba())
				NodoAux.getArriba().setAbajo(Nodo)
				NodoAux.setArriba(Nodo)
				agregado=True
				break
		if agregado==False:
			NodoAux= NodoAuxiliarHorizontal.getAbajo()
			while NodoAux.getAbajo()!=None:
				NodoAux=NodoAux.getAbajo()
				Nodo.setArriba(NodoAux)
				NodoAux.setAbajo(Nodo)

		AuxiliarVertical=self.ListaVertical.buscar(departamento)
		AuxiliarVertical.setDerecha(Nodo)

		Nodo.setIzquierda(AuxiliarVertical)

	#Metodo para insertar cuando existe la cabecera vertical
	def ExisteVertical(self,departamento,empresa,valor):

		self.ListaHorizontal.agregar(empresa)

		NodoAuxiliarVertical= self.ListaVertical.buscar(departamento)
		ListaUsuarios=LN.Nombres()

		ListaUsuarios.insertar(valor)

		Nodo=nm.NodoMatriz(ListaUsuarios,departamento,empresa)
		NodoAux2= NodoAuxiliarVertical.getDerecha()

		letrainsertar=empresa[:1]
		letrainsertar=ord(letrainsertar)
		agregado=False

		while NodoAux2!=None:
			letracomparar=NodoAux2.getX()[:1]
			letracomparar=ord(letracomparar)

			if letrainsertar>letracomparar:
				NodoAux2=NodoAux2.getDerecha()
			else:
				Nodo.setDerecha(NodoAux2)
				Nodo.setIzquierda(NodoAux2.getIzquierda())
				NodoAux2.getIzquierda().setDerecha(Nodo)
				NodoAux2.setIzquierda(Nodo)
				agregado=True
				break 

		if agregado ==False:
			NodoAux2=NodoAuxiliarVertical.getDerecha()
			while NodoAux2.getDerecha()!=None:
				NodoAux2=NodoAux2.getDerecha()
			Nodo.setIzquierda(NodoAux2)
			NodoAux2.setDerecha(Nodo)

		AuxiliarHorizontal=self.ListaHorizontal.buscar(empresa)				
		AuxiliarHorizontal.setAbajo(Nodo)

		Nodo.setArriba(AuxiliarHorizontal)

	#Metodo para insertar cuando no existe ninguna cabecera
	def NoExisten(self,departamento,empresa,valor):
		self.ListaHorizontal.agregar(empresa)
		self.ListaVertical.agregar(departamento)
		AuxiliarVertical=self.ListaVertical.buscar(departamento)
		AuxiliarHorizontal=self.ListaHorizontal.buscar(empresa)

		ListaUsuarios=LN.Nombres()
		ListaUsuarios.insertar(valor)

		Nodo=nm.NodoMatriz(ListaUsuarios,departamento,empresa)

		AuxiliarVertical.setDerecha(Nodo)
		AuxiliarHorizontal.setAbajo(Nodo)

		Nodo.setArriba(AuxiliarHorizontal)
		Nodo.setIzquierda(AuxiliarVertical)

	#Metodo para comparar
	def Comparar(self, departamento, empresa):
		NodoAux = self.ListaHorizontal.buscar(empresa)
		while NodoAux != None:
			if NodoAux.getY() == departamento:
				return True
			else:
				NodoAux = NodoAux.getAbajo()
		return False

	def Graficar(self):
		#Creamos un archivo con nombre matriz
		f=open("Graficas\Matriz.txt","w")
		#Escribimos sobre el archivo el inicio de sentencia 
		f.write("digraph Matriz{ bgcolor=gray \n")
		f.write("node [fontcolor=\"white\", height=0.5, color=\"white\"]\n")
		f.write("[shape=tripleoctagon, style=filled, color=blue]")
		f.write("rankdir=LR \n")
		f.write("edge  [color=\"black\", dir=fordware]\n")
		#instanciamos derecha como primer nodo de la cabecera horizontal

		derecha = self.ListaHorizontal.getInicio()
		Actual = derecha
		contador=1
		#Agregamos el apuntador principal
		f.write("inicial[style =\"filled\"; label=\"inicial\";pos= \"0,0!\"] \n")

		'''--------------------------------Obtener Horizontales ----------------------------'''
		while derecha!=None:
			f.write("\""+Actual.getValor()+"\""+"[style =\"filled\"; label=\""+Actual.getValor()+"\";pos= \""+str(contador)+",0!\"]\n")
			contador=contador+1

			derecha=derecha.getDerecha()
			Actual=derecha

		'''--------------------------------Obtener Verticales ----------------------------'''
		contador= 1
		abajo = self.ListaVertical.getInicio()
		Actual=abajo

		while abajo!= None:
			f.write(Actual.getValor()+"[style =\"filled\"; label="+Actual.getValor()+";pos= \"0,"+str(contador)+"!\"]\n")
			contador=contador+1

			abajo=abajo.getAbajo()
			Actual=abajo

		'''--------------------------------Obtener Valores ----------------------------'''

		derecha= self.ListaHorizontal.getInicio()
		Actual=derecha

		while derecha!=None:
			abajo=self.ListaVertical.getInicio()
			while abajo!= None:

				if Actual.getAbajo()!=None:
					Actual=Actual.getAbajo()
					user = Actual.getValor().getPrimero().getValor()
					f.write(user.getUsuario()+"[shape=doubleoctagon,style =\"filled\"; label="+user.getUsuario()+";pos= \""+str(self.posX(Actual.getX()))+","+str(self.posY(Actual.getY()))+"!\"]\n")
					self.imprimirPrimeros(Actual.getValor(),f,Actual.getY(),Actual.getX())
				
				abajo=abajo.getAbajo()
			derecha=derecha.getDerecha()
			Actual=derecha
		'''--------------------------------Enlazar Horizontal -> ----------------------------'''
		derecha=self.ListaHorizontal.getInicio()
		abajo = self.ListaVertical.getInicio()
		f.write("\n inicial->"+"\""+derecha.getValor()+"\""+"->inicial->"+abajo.getValor()+"->inicial;\n")
		first=True
		Actual=derecha
		while derecha!=None:

			if first==True:
				f.write(str("\""+Actual.getValor())+"\"")
				first=False
			else:
				f.write("->"+"\""+Actual.getValor()+"\"")

			contador=contador+1
			derecha=derecha.getDerecha()
			Actual=derecha
		f.write(";")

		'''--------------------------------Enlazar Horizontal <- ----------------------------'''
		izquierda=self.ListaHorizontal.getFin()

		last=True
		Actual=izquierda

		while izquierda!=None:
			
			if last==True:
				f.write(str("\""+Actual.getValor())+"\"")
				last=False
				
			else:
				f.write("->"+"\""+Actual.getValor()+"\"")

			izquierda=izquierda.getIzquierda()
			Actual=izquierda

		f.write(";\n")

		'''--------------------------------Enlazar Vertical abajo ----------------------------'''
		first=True
		Actual=abajo
		while abajo!=None:
			if first==True:
				f.write(str(Actual.getValor()))
				first=False
			else:
				f.write("->"+Actual.getValor())
			abajo=abajo.getAbajo()
			Actual=abajo
		f.write(";\n")

		'''--------------------------------Enlazar Vertical arriba ----------------------------'''

		last=True
		arriba = self.ListaVertical.getFin()
		Actual=arriba
		while arriba!=None:
			if last == True:
				f.write(str(Actual.getValor()))
				last=False
			else:
				f.write("->"+Actual.getValor())
			arriba=arriba.getArriba()
			Actual=arriba

		f.write(";\n")

		'''--------------------------------Enlazar Valores hacia derecha----------------------------'''

		#instanciamos para estar en la primera posicion de los dominios 
		derecha=self.ListaHorizontal.getInicio()
		#nodo auxiliar el cual recorrera de derecha hacia abajo
		Actual=derecha
		while derecha!= None:
			#instanciamos el primero nodo de letras 
			abajo= self.ListaVertical.getInicio()
			#escribimos en el archivo el primer valor
			f.write("\""+derecha.getValor()+"\"")

			while abajo!=None:
				#ponemos una condicion si actual diferente de nulo recorrera hacia abajo 
				if Actual.getAbajo()!=None:
					#derecha, luego hacia abajo
					Actual=Actual.getAbajo()
					#enlazar el valor en el archivo del valor actual con el de abajo 
					f.write("->"+Actual.getValor().getPrimero().getValor().getUsuario())
				#cambiar de nodo hacia el siguiente 
				abajo=abajo.getAbajo()
			#separacion de nombres con ;
			f.write(";\n")
			#recorremos la posicion del nodo hacia la derecha 
			derecha=derecha.getDerecha()
			#el nodo auxiliar es igual al de la siguiente posicion 
			Actual=derecha

		f.write("\n\n\n")

		'''--------------------------------Enlazar Valores hacia abajo----------------------------'''
		
		abajo=self.ListaVertical.getInicio()
		Actual=abajo
		while abajo!=None:
			derecha=self.ListaHorizontal.getInicio()
			f.write(abajo.getValor())
			while derecha!=None:
				if Actual.getDerecha()!=None:
					Actual=Actual.getDerecha()
					f.write("->"+Actual.getValor().getPrimero().getValor().getUsuario())
				derecha=derecha.getDerecha()
			f.write(";\n")
			abajo=abajo.getAbajo()
			Actual=abajo


		f.write("\n\n\n")
		
		derecha=self.ListaHorizontal.getInicio()
		Actual=derecha

		while derecha!=None:

			while Actual.getAbajo()!=None:
				Actual=Actual.getAbajo()
			while Actual.getArriba()!=None:
				f.write(Actual.getValor().getPrimero().getValor().getUsuario()+"->")
				Actual=Actual.getArriba()
			
			f.write( "\""+derecha.getValor()+"\"")
			f.write(";\n")
			derecha=derecha.getDerecha()
			Actual=derecha

		abajo=self.ListaVertical.getInicio()
		Actual=abajo

		while abajo!=None:
			
			while Actual.getDerecha()!=None:
				Actual=Actual.getDerecha()
			while Actual.getIzquierda()!=None:
				f.write(Actual.getValor().getPrimero().getValor().getUsuario()+"->")
				Actual=Actual.getIzquierda()
			
			f.write(abajo.getValor())
			f.write(";\n")
			abajo=abajo.getAbajo()
			Actual=abajo






		f.write("}")
		subprocess.Popen("fdp -Tpng Graficas\Matriz.txt -o Graficas\Matriz.png")
	

	def posX(self,nodo):
		x=1
		derecha=self.ListaHorizontal.getInicio()

		while derecha!=None:
			if derecha.getValor()==nodo:
				return x 
			else:
				x=x+1
				derecha=derecha.getDerecha()
	#Metodo para obtener el valor en y en la matriz
	def posY(self,nodo):
		y=1
		abajo= self.ListaVertical.getInicio()
		while abajo!=None:
			if abajo.getValor()==nodo:
				return y
			else:
				y=y+1
				abajo=abajo.getAbajo()

	#Metodo para graficar los nombres de la lista del nodo digase el hijo 
	def imprimirPrimeros(self,lista,f,Y,x):
		#Creamos un archivo con nombre matriz
		f=f
		cont2=self.posX(x)
		contador=self.posY(Y)
		if lista.getTamano()>1:
			auxiliar= lista.getPrimero()
			while auxiliar.getSiguiente()!=None :
				contador=contador+0.05
				cont2=cont2+0.05
				auxiliar=auxiliar.getSiguiente()
				aux=auxiliar
				f.write("\""+auxiliar.getValor().getUsuario()+"\""+"[shape=octagon, style =\"filled\"; label=\""+auxiliar.getValor().getUsuario()+"\";pos= \""+str(cont2)+","+str(contador)+"!\"]\n")
				
				#print auxiliar.getValor()
			f.write(";\n")

			auxiliar= lista.getPrimero()
			f.write(auxiliar.getValor().getUsuario())
			while auxiliar.getSiguiente()!=None :
				auxiliar=auxiliar.getSiguiente()
				aux=auxiliar

				f.write("->"+auxiliar.getValor().getUsuario())
				#print auxiliar.getValor()
			f.write(";\n")
			f.write(lista.getUltimo().getValor().getUsuario()+"")
			auxiliar= lista.getUltimo()

			while auxiliar.getAnterior()!=None :
				auxiliar=auxiliar.getAnterior()
				f.write("->"+auxiliar.getValor().getUsuario())
				#print auxiliar.getValor()
			f.write(";\n")

	def buscar(self,nombreusuario,empresa,departamento):
		if self.tamano==0:
			return None
		else:
			derecha = self.ListaHorizontal.getInicio()

			Actual=derecha

			while derecha!= None:

				abajo = self.ListaVertical.getInicio()

				while abajo!= None:

					if Actual.getAbajo()!= None:

						Actual = Actual.getAbajo()

						Auxiliar=Actual.getValor().getPrimero()

						while Auxiliar!=None:

							if nombreusuario== Auxiliar.getValor().getUsuario() and abajo.getValor()==departamento and derecha.getValor() == empresa:
							
								return Auxiliar.getValor()
							else:

								Auxiliar=Auxiliar.getSiguiente()


					abajo = abajo.getAbajo()

				derecha=derecha.getDerecha()

				Actual=derecha

		return None

	def eliminar(self,departamento,empresa,valor):
		AuxiliarVertical= self.ListaVertical.buscar(departamento)

		AuxiliarHorizontal = self.ListaHorizontal.buscar(empresa)

		if AuxiliarVertical!= None and AuxiliarHorizontal!= None:

			Auxiliar = AuxiliarHorizontal

			while Auxiliar.getAbajo()!= None:

				Auxiliar = Auxiliar.getAbajo()

				if Auxiliar.getY() == departamento:

					lista = Auxiliar.getValor()

					lista.eliminar(valor)

					if lista.getPrimero()==None:

						if self.X(empresa) != 1:

							if Auxiliar.getAbajo() != None:

								Auxiliar.getArriba().setAbajo(Auxiliar.getAbajo())
								
								Auxiliar.getAbajo().setArriba(Auxiliar.getArriba())
							
							elif Auxiliar.getAbajo() == None:
								
								Auxiliar.getArriba().setAbajo(None)
						else:

							self.ListaHorizontal.eliminar(empresa)

						if self.Y(departamento)!= 1:
							
							if Auxiliar.getDerecha()!= None:
								
								Auxiliar.getIzquierda().setDerecha(Auxiliar.getDerecha())
								
								Auxiliar.getDerecha().setIzquierda(Auxiliarl.getIzquierda())
							
							elif Auxiliar.getDerecha()==None:
								
								Auxiliar.getIzquierda().setDerecha(None)
						
						else:
							
							self.ListaVertical.eliminar(departamento)
					
					return True

			return False

	def X(self,nodo):
		contador= 0

		derecha= self.ListaHorizontal.getPrimero()

		Actual=derecha

		while derecha!= None:

			if derecha.getValor()==nodo:

				abajo=self.ListaVertical.getPrimero()

				while abajo!= None and Actual.getAbajo()!= None:

					if Actual.getAbajo()!= None:

						Actual=Actual.getAbajo()

					contador=contador+1

					abajo=abajo.getAbajo()

				break

			else:

				derecha= derecha.getDerecha()

				Actual= derecha

		return contador

	def Y(self, nodo):
		contador= 0 

		abajo = self.ListaVertical.getPrimero()

		actual=abajo

		while abajo!= None:

			if abajo.getValor() == nodo:

				derecha= self.ListaVertical.getPrimero()

				while derecha!= None and Actual.getDerecha()!= None:

					if Actual.getDerecha()!= None:

						Actual= Actual.getDerecha()

					contador= contador+1

				derecha = derecha.getDerecha()

				break

			else:

				abajo = abajo.getAbajo()

				Actual= abajo

		return contador

