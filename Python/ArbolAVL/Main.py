from parent import Arbol
ar=Arbol
arbol=ar.AVL()

arbol.insertar("ab")
arbol.insertar("ac")
arbol.insertar("ad")
arbol.insertar("aa")
arbol.insertar("af")
arbol.insertar("ae")

arbol.impreArbol(arbol.getRoot(), None)