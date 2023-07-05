# PROYECTO FINAL GABRIEL CHAVES BENITEZ; CURSO E23

from cargar_datos import cargar_datos_bbdd as bbdd
from procesar_mensajes import procesar_mensajes_metacritic as meta
from procesar_mensajes import procesar_mensajes_playstore as play
from obtener_datos import consultar_datos as consulta
conexion = bbdd.conexion_bbdd("bbdd/videojuegos.db")
"""
id_red_social = bbdd.buscar_red_social(conexion, "Playstore")
print("Red social: ",id_red_social)

id_red_social = bbdd.insertar_red_social(conexion,"Twitter","Twitter.com")
print("Rdo social  nueva: ", id_red_social)
"""

#meta.cargar_comentario_metacritic(conexion,"The Legend of Zelda: Ocarina of Time","Nintendo64")
#play.cargar_comentario_playstore(conexion)
#consulta.consultar_comentarios_fecha(conexion)
#meta.cargar_videojuegos_metacritic(conexion)
#consulta.consultar_comentarios_fecha(conexion, "Zelda","2023-07-05","2023-07-05")
bbdd.insertar_mensaje(conexion, "2023-07-06", "prueba", 1, 1000, 1)
consulta.consultar_comentarios_fecha_media(conexion, "2023-07-05", "2023-07-06")