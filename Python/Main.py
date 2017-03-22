from MatrizDispersa import Matriz
mm = Matriz
matriz1 = mm.Matriz()

from ArbolAVL import Arbol
AVL= Arbol


from ArbolAVL import Activo
ac= Activo

from MatrizDispersa import GeneradorID
gid = GeneradorID


from MatrizDispersa import Usuario
us = Usuario

from flask import Flask, request, Response
app = Flask("Proyecto1")






@app.route('/Matriz', methods = ['POST']) 
def usuario2():

	if str(request.form['tipo'])=="buscar":
		arreglo = str(request.form['informacion']).split("$")

		aux = matriz1.buscar(arreglo[0],arreglo[3],arreglo[2])


		return "Nombre: "+aux.getNombre()+" Usuario: "+aux.getUsuario()+" Contrasena: "+aux.getContrasena()+ " Empresa: "+ aux.getX()+ " Departamento: "+aux.getY()

	elif str(request.form['tipo'])=="registrar":

		arreglo = str(request.form['informacion']).split("$")
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

		generadorid = gid.GeneradorID()

		activo = ac.Activo()

		activo.setId(generadorid.obtenerID(15))

		activo.setUsuario(arreglo[0])

		activo.setNombre(arreglo[1])

		activo.setDescripcion(arreglo[2])

		usuario = matriz1.buscar(arreglo[0],arreglo[3],arreglo[4])

		arbol= usuario.getArbol()

		arbol.insertar(activo)

		usuario.setArbol(arbol)

		activo.setUsuario(usuario)

		







		return "Agregado"






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

