import NodoUsuarios
nu=NodoUsuarios



class Nombres(object):
	def __init__(self):
		self.primero=None
		self.ultimo=None
		self.tamano = 0
		


	def vacio(self):
		if self.tamano==0:
			return True
		else: 
			return False

	def insertar(self,insertar):
		nuevo=nu.NodoUsuarios(insertar)
		
		if self.vacio()==True:
			self.primero=nuevo
			self.ultimo= nuevo
			
		else:

			 letraInsertar = insertar[:1]
			 letraInsertar= ord(letraInsertar)

			 agregado=False	
			 Auxiliar= self.primero

			 while Auxiliar!= None:
			 	letracomparar = Auxiliar.getValor()[:1]
			 	letracomparar=ord(letracomparar)

			 	if letraInsertar>letracomparar:
			 		Auxiliar=Auxiliar.getSiguiente()
			 	else:
			 		if Auxiliar==self.primero:
			 			nuevo.setSiguiente(Auxiliar)
			 			Auxiliar.setAnterior(nuevo)
			 			self.primero=nuevo
			 			agregado=True
			 			break
			 		else:

			 			nuevo.setAnterior(Auxiliar.getAnterior())
			 			Auxiliar.getAnterior().setSiguiente(nuevo)

			 			nuevo.setSiguiente(Auxiliar)
			 			Auxiliar.setAnterior(nuevo)
			 			agregado=True
			 			break
			 if agregado==False:
			 	self.ultimo.setSiguiente(nuevo)
			 	nuevo.setAnterior(self.ultimo)
				self.ultimo=nuevo

		self.tamano=self.tamano+1
		
	def getTamano(self):
		return self.tamano

	def buscar(self,valor):
		if self.vacio()==False:
			aux=self.primero
			while aux!=None:
				if aux.getValor()==valor:
					return aux
				aux = aux.getSiguiente()
		else:
			return None

	def getPrimero(self):
		return self.primero

	def setPrimero(self,primero):
		self.primero=primero

	def getUltimo(self):
		return self.ultimo

	def setUltmio(self,ultimo):
		return self.ultimo
	def eliminar(self,dato):
		if self.vacio()==False:
			nodoaux = self.primero

			while nodoaux!=None:
				if nodoaux.getValor()==dato:
					if nodoaux==self.primero:
						if nodoaux.getSiguiente()!=None:
							self.primero=nodoaux.getSiguiente()
							nodoaux=nodoaux.getSiguiente().setAnterior(None)
							self.tamano=self.tamano-1
							
						else:
							self.primero=(None)
							self.ultimo=(None)
							self.tamano=0

						break
					elif nodoaux== self.getUltimo():
						if nodoaux.getAnterior()!=None:
						 	self.ultimo=nodoaux.getAnterior()
						 	nodoaux=nodoaux.getAnterior().setSiguiente(None)
						 	self.tamano=self.tamano -1 
						else:
							self.primero=(None)
							self.ultimo=(None)
							self.tamano=0
							
						break
					else:
						nodoaux.getAnterior().setSiguiente(nodoaux.getSiguiente())
						nodoaux.getSiguiente().setAnterior(nodoaux.getAnterior())
						self.tamano=self.tamano-1

						break
				else:
					nodoaux=nodoaux.getSiguiente()