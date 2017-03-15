class Usuario(object):
	def __init__(self):
		self.Nombre=None
		self.Usuario=None
		self.Contrasena=None
		self.Arbol=None
		

	def setNombre(self,nombre):
		self.Nombre=nombre
	def setUsuario(self,usuario):
		self.Usuario=usuario
	def setContrasena(self,contrasena):
		self.Contrasena=contrasena
	def setArbol(self,arbol):
		self.Arbol=arbol


	def getNombre():
		return self.Nombre
	def getUsuario():
		return self.Usuario
	def getContrasena():
		return self.Contrasena
	def getArbol():
		return self.Arbol

