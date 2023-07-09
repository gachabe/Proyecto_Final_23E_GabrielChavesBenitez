# PROYECTO FINAL GABRIEL CHAVES BENITEZ; CURSO E23
from tkinter import *
from cargar_datos import cargar_datos_bbdd as bbdd
from procesar_mensajes import procesar_mensajes_metacritic as meta
from procesar_mensajes import procesar_mensajes_playstore as play
from obtener_datos import consultar_datos as consulta
from GUI import pantalla_principal as pp
from GUI import mis_funciones as f
conexion = bbdd.conexion_bbdd("bbdd/videojuegos.db")
"""
id_red_social = bbdd.buscar_red_social(conexion, "Playstore")
print("Red social: ",id_red_social)

id_red_social = bbdd.insertar_red_social(conexion,"Twitter","Twitter.com")
print("Rdo social  nueva: ", id_red_social)
"""


#play.cargar_comentario_playstore(conexion)
#meta.cargar_videojuegos_metacritic(conexion)
#meta.cargar_comentario_metacritic(conexion,"The Legend of Zelda: Ocarina of Time","Nintendo64")
#consulta.consultar_comentarios_fecha(conexion, "app","2023-07-05","2023-07-06")
#meta.cargar_comentario_metacritic(conexion,"Final Fantasy IX","PlayStation")
#consulta.consultar_comentarios_fecha_media(conexion, "2023-07-05", "2023-07-06")
#consulta.consultar_comentarios_red_social_media(conexion, "2023-07-05", "2023-07-06")
#consulta.consultar_comentarios_cantidad(conexion)
#f.borrar_datos(conexion)
#f.carga_inicial(conexion)

ventana_principal = Tk()
calculadora = pp.Interfaz(ventana_principal,conexion)
ventana_principal.mainloop()