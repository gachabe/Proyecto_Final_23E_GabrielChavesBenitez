# PROYECTO FINAL GABRIEL CHAVES BENITEZ; CURSO E23

from cargar_datos import cargar_datos_bbdd as bbdd

conexion = bbdd.conexion_bbdd("bbdd/videojuegos.db")

id_red_social = bbdd.buscar_red_social(conexion, "Playstore")
print("Red social: ",id_red_social)

id_red_social = bbdd.insertar_red_social(conexion,"Twitter","Twitter.com")
print("Rdo social  nueva: ", id_red_social)