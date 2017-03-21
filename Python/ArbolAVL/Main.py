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
arbol.insertar(0)
arbol.eliminar(2)
print " . "
print "----" +str((arbol.buscar(4,arbol.getRoot(),None).getAltura()))
arbol.impreArbol(arbol.getRoot(), None)