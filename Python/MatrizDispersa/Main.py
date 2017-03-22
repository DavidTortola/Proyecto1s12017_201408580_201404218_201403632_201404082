import Matriz 
ma = Matriz
matriz = ma.Matriz()
import Usuario
us = Usuario

usuario = us.Usuario()

usuario.setNombre("Andree")
usuario.setContrasena(1234)
usuario.setUsuario("AndreeAvalos")
usuario.setX("MARIONO")
usuario.setY("Ventas")

matriz.agregar(usuario.getY(),usuario.getX(),usuario)

matriz.agregar(usuario.getY(),usuario.getX(),usuario)

matriz.Graficar()

aux = matriz.buscar(usuario.getUsuario(),usuario.getX(),usuario.getY())
