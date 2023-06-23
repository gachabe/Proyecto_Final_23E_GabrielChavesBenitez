# PROYECTO FINAL GABRIEL CHAVES BENITEZ; CURSO E23

from cargar_datos import cargar_datos_bbdd as bbdd
from procesar_mensajes import procesar_mensajes_metacritic as meta
conexion = bbdd.conexion_bbdd("bbdd/videojuegos.db")
"""
id_red_social = bbdd.buscar_red_social(conexion, "Playstore")
print("Red social: ",id_red_social)

id_red_social = bbdd.insertar_red_social(conexion,"Twitter","Twitter.com")
print("Rdo social  nueva: ", id_red_social)
"""

meta.cargar_comentario_metacritic(conexion,"The Legend of Zelda: Ocarina of Time","Nintendo64")