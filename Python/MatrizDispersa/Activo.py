class Activo(objetc):
	def __init__(self):
		self.id=None
		self.nombre= None
		self.descripcion = None

	def setId(self, id):
		self.id=id
	def setNombre(self,nombre):
		self.nombre=nombre
	def setDescripcion(self,descripcion):
		self.descripcion=descripcion

	def getId(self):
		return self.id
	def getNombre(self):
		return self.nombre
	def getDescripcion(self):
		return self.descripcion
	