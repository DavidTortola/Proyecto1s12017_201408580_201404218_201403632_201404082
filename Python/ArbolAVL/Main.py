import Arbol
ar=Arbol
arbol=ar.AVL()

arbol.insertar(1)
arbol.insertar(2)
arbol.insertar(3)

arbol.impreArbol(arbol.getRoot(), None)