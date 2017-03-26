import Arbol
ar=Arbol
arbol=ar.AVL()

arbol.insertar(1)
arbol.insertar(2)
arbol.insertar(3)
arbol.insertar(4)
arbol.insertar(5)
arbol.insertar(6)
arbol.insertar(7)
arbol.insertar(8)
arbol.insertar(12)

arbol.eliminar(2)
arbol.eliminar(3)
arbol.eliminar(4)
arbol.eliminar(8)
arbol.eliminar(1)
arbol.eliminar(5)
arbol.eliminar(7)
arbol.eliminar(12)
arbol.impreArbol(arbol.getRoot(), None)