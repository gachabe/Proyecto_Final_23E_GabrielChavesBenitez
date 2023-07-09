from datetime import date
import json
from cargar_datos import cargar_datos_bbdd as bbdd

def cargar_comentario_playstore(conexion):
    with open("datos/PlayStoreGameAppInfoReview.json")as file:
        json_data = json.load(file)
    f_actual = date.today()
    id_red_social = bbdd.buscar_red_social(conexion, "Playstore")
    juegos = ["com.redantz.game.za3p","com.imcrazy.ds2"]
    for juego in juegos:
        tit_juego = json_data[juego]["appInfo"]["title"]
        f_publicacion = json_data[juego]["appInfo"]["released"][-4:]
        id_juego = bbdd.buscar_juego(conexion,tit_juego,"Mobile")
        if id_juego is None:
            id_juego = bbdd.insertar_juego(conexion, tit_juego, "Mobile", f_publicacion)

        for i in range(5):
            nick_usuario = json_data[juego]["reviews"][i]["userName"]
            id_usuario = bbdd.buscar_usuario(conexion, nick_usuario)
            if id_usuario is None:
                id_usuario = bbdd.insertar_usuario(conexion,nick_usuario,nick_usuario,"sin email")
            mensaje = json_data[juego]["reviews"][i]["content"]
            try:
                bbdd.insertar_mensaje(conexion,f_actual,mensaje,id_juego,id_usuario,id_red_social)
            except Exception as error:
                print(f"Ha ocurrido un error: {error}")
                print(f"id juego: {id_juego}, id usuario: {id_usuario},red social: {id_red_social}, mensaje: {mensaje}")