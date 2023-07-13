# PROYECTO FINAL GABRIEL CHAVES BENITEZ; CURSO E23
from tkinter import Tk
from cargar_datos import cargar_datos_bbdd as bbdd
from GUI import pantalla_principal as pp


conexion = bbdd.conexion_bbdd("bbdd/videojuegos.db")
if __name__ == "__main__":
    ventana_principal = Tk()
    calculadora = pp.Interfaz(ventana_principal,conexion)
    ventana_principal.mainloop()