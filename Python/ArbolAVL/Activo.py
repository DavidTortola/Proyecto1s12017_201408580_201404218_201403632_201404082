
class Activo(object):

	def __init__(self):
		self.identificador=None
		self.nombre=None
		self.descripcion=None

	def setId(self,identificador):
		self.identificador=identificador
	def setNombre(self,nombre):
		self.nombre=nombre
	def setDescripcion(self,descripcion):
		self.descripcion=descripcion
		

	def getId(self):
		return self.identificador
	def getNombre(self):
		return self.nombre
	def getDescripcion(self):
		return self.descripcion