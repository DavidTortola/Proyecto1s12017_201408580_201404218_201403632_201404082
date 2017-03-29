class Activo(object):
	def __init__(self):
		self.id=None
		self.nombre= None
		self.descripcion = None
		self.usuario=None
		self.empresa=None
		self.departamento=None

	def setId(self,ide):
		self.id=ide
	def setNombre(self,nombre):
		self.nombre=nombre
	def setDescripcion(self,descripcion):
		self.descripcion=descripcion
	def setEmpresa(self,empresa):
		self.empresa=empresa
	def setDepartamento(self,departamento):
		self.departamento=departamento
	def setUsuario(self,usuario):
		self.usuario=usuario


	def getEmpresa(self):
		return self.empresa
	def getDepartamento(self):
		return self.departamento
	def getId(self):
		return self.id
	def getNombre(self):
		return self.nombre
	def getDescripcion(self):
		return self.descripcion
	def getUsuario(self):
		return self.usuario
	