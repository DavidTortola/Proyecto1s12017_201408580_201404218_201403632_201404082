
from MatrizDispersa import Matriz
mm = Matriz
matriz1 = mm.Matriz()

from ArbolAVL import Arbol
AVL= Arbol
arbol=AVL.AVL()

from MatrizDispersa import Usuario
us = Usuario
usuario=us.Usuario()

usuario.setNombre("Andree")
usuario.setUsuario("AndreeAvalos")
usuario.setContrasena("1234")

arbol.insertar("ab")
arbol.insertar("ac")
arbol.insertar("ad")

usuario.setArbol(arbol)


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

matriz1.Graficar()


