import pandas as pd
from datetime import datetime
from cargar_datos import cargar_datos_bbdd as bbdd
"""
Aqui creamos el módulo para cargar los comentarios y juegos desde metacritic, también usaremos el formato datetime y lo
pasaremos a date en el query. 
"""
def cargar_videojuegos_metacritic(conexion):
    """
 Aqui cargamos todos los juegos del CSV metacritic
    """
    df_juegos = pd.read_csv("datos/metacritic_game_info.csv", header=0,index_col = 0,
                            names = ['tit_juego', 'f_publicacion', 'Publisher', 'Genre',
                                     'plataforma', 'PMetascore', 'Avg', 'NoPlayers'])
    df_juegos = df_juegos.loc[:,["tit_juego","plataforma", "f_publicacion"]]
    df_juegos.to_sql(name="juegos", con=conexion, if_exists="append", index=False)


def cargar_comentario_metacritic(conexion, juego, plataforma):
    """
Aqui dado un juego y una plataforma se añadirá los comentarios de metacritic relacionado a ambos a nuestra base de datos
    """
    df_comentarios = pd.read_csv("datos/metacritic_game_user_comments.csv", header=0, index_col=0,
                                 names=['Title','Platform','Userscore','Comment', 'UserName'])
    df_comentarios =(df_comentarios.loc[(df_comentarios['Title'] == juego) & (df_comentarios['Platform'] == plataforma),
    ['Title','Platform','Comment','UserName']])
    id_red_social = bbdd.buscar_red_social(conexion,"Metacritic")
    id_juego = bbdd.buscar_juego(conexion,juego,plataforma)
    f_actual = datetime.today()
    if id_juego is None:
        id_juego = bbdd.insertar_juego(conexion, juego, plataforma, f_actual)

    for fila in df_comentarios.itertuples():
        id_usuario = bbdd.buscar_usuario(conexion, fila.UserName)
        if id_usuario is None:
            id_usuario = bbdd.insertar_usuario(conexion,fila.UserName, fila.UserName, "sin email")

        try:
            bbdd.insertar_mensaje(conexion, f_actual, fila.Comment, id_juego, id_usuario, id_red_social)
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")
            print(f"id juego: {id_juego}, id usuario: {id_usuario},red social: {id_red_social}, "
                  f"mensaje: {fila.Comment}") #PSeudo log, para facilitar la correcion de errores


