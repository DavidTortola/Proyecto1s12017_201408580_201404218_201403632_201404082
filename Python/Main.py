from MatrizDispersa import Matriz
mm = Matriz
matriz1 = mm.Matriz()

from ArbolAVL import Arbol
AVL= Arbol


from ArbolAVL import Activo
ac= Activo

from MatrizDispersa import GeneradorID

GI = GeneradorID




from MatrizDispersa import Usuario
us = Usuario

from flask import Flask, request, Response
app = Flask("Proyecto1")






@app.route('/Matriz', methods = ['POST']) 
def usuario2():

	if str(request.form['tipo'])=="login":
		arreglo = str(request.form['informacion']).split("$")

		aux = matriz1.buscar(arreglo[0],arreglo[3],arreglo[2])

		if aux!= None:
			
			return aux.getNombre()+","+aux.getUsuario()+","+aux.getContrasena()+ ","+ aux.getX()+ ","+aux.getY()

		else:
			return "false"

	elif str(request.form['tipo'])=="registrar":

		arreglo = str(request.form['informacion']).split("$")

		aux = matriz1.buscar(arreglo[0],arreglo[3],arreglo[4])

		if aux!= None:

			return "Existe el Usuario"
		else:
			usuario=us.Usuario()
			usuario.setUsuario(arreglo[0])
			usuario.setContrasena(arreglo[1])
			usuario.setNombre(arreglo[2])
			usuario.setX(arreglo[3])
			usuario.setY(arreglo[4])
			arbol=AVL.AVL()
			usuario.setArbol(arbol)

			matriz1.agregar(usuario.getY(),usuario.getX(),usuario)

			matriz1.Graficar()

		return "Agregado"

	elif str(request.form['tipo'])=="registrarActivo":

		arreglo = str(request.form['informacion']).split("$")

		generador = GI.GeneradorID()


		activo = ac.Activo()

		identificador =str(generador.generarID(15))

		activo.setId(identificador)

		activo.setUsuario(arreglo[0])

		activo.setNombre(arreglo[1])

		activo.setDescripcion(arreglo[2])

		usuario = matriz1.buscar(arreglo[0],arreglo[3],arreglo[4])

		arbol= usuario.getArbol()

		arbol.insertar(activo)

		usuario.setArbol(arbol)

		activo.setUsuario(usuario)

		arbol.impreArbol(arbol.getRoot(), None)

		return "Identificador de Activo: "+ identificador

	elif str(request.form['tipo'])=="generarid":

		generador = GI.GeneradorID()

		identificador =str(generador.generarID(15))

		return identificador

	elif str(request.form['tipo'])=="eliminarUsuario":

		arreglo = str(request.form['informacion']).split("$")
		
		matriz1.eliminar(arreglo[2],arreglo[1],arreglo[0])

	elif str(request.form['tipo'])=="obtenerdatos":

		usuario = matriz1.buscar(str(request.form['usuario']),str(request.form['empresa']),str(request.form['departamento']))
		arbol= usuario.getArbol()
		valores = arbol.obtenerDatos()

		return valores
	elif str(request.form['tipo'])=="eliminaractivo":
		usuario = matriz1.buscar(str(request.form['usuario']),str(request.form['empresa']),str(request.form['departamento']))
		arbol= usuario.getArbol()
		valores = arbol.eliminar(str(request.form['id']))

	elif str(request.form['tipo'])=="modificaractivo":

		arreglo = str(request.form['informacion']).split("$")

		usuario = matriz1.buscar(arreglo[0],arreglo[4],arreglo[5])

		arbol= usuario.getArbol()

		aux = arbol.buscar(arreglo[1],,arbol.getRoot(),None)

		aux.setNombre(arreglo[2])
		aux.setDescripcion(arreglo[3])
		
		arbol.impreArbol(arbol.getRoot(), None)

		return "Activo Modificado: "+ identificador


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')


'''




usuario2=us.Usuario()

usuario2.setNombre("Andree")
usuario2.setUsuario("bobo")
usuario2.setContrasena("1234")

arbol.insertar("ab")
arbol.insertar("ac")
arbol.insertar("ad")

usuario2.setArbol(arbol)



matriz1.agregar("aaa","empresa1",usuario)
matriz1.agregar("aaa","empresa1",usuario2)

usuario3=us.Usuario()
usuario3.setNombre("mario")
usuario3.setUsuario("juancho")
usuario3.setContrasena("popo")
usuario3.setArbol(arbol)

matriz1.agregar("bbb","empresa3",usuario3)

user=matriz1.buscar("fjakls")
if user != None:

	print "Nombre: "+user.getNombre()+" \nUsuario: "+user.getUsuario()+" \nContrasena: "+user.getContrasena()
	arbol2 = user.getArbol()
	arbol2.impreArbol(arbol2.getRoot(), None)
else:
	print "No se encontro ninguno"
matriz1.Graficar()
'''

