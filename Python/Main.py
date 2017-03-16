
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



matriz1.agregar("aaa","empresa1",usuario)


