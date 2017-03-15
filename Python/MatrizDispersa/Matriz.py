#----------------------------------Area de Importaciones-----------------------------
import Listausuarios
LN=Listausuarios
import ListaDobleV
LDV=ListaDobleV
import ListaDobleH
LDH=ListaDobleH
import NodoMatriz
nm=NodoMatriz
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
