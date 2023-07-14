# Módulo para conexión y cargar inicial de los datos
import sqlite3
from sqlite3 import Error
"""
Aqui se cragarán los datos en la base de datos.
"""
def conexion_bbdd(archivo):

    """
Mediante sqlite3 creamos la conexion a la base de datos.
    """
    conn = None
    try:
        conn = sqlite3.connect(archivo)
        print(f"Versión de Sqlite3: {sqlite3.version}")
    except Error as error:
        print(f"Ha ocurrido un error al conectarse {error}")
        if conn:
            conn.close()
    return conn


def buscar_red_social(conexion,nom_red_social):
    """
Aquí realizamos la búsqeuda de una red social mediante su nombre
    """
    cursor = conexion.cursor()
    query ="SELECT id_red_social FROM red_social WHERE nom_red_social = '{}'".format(nom_red_social)
    cursor.execute(query)
    res = cursor.fetchone()
    if res is None:
        id = None
    else:
        if type(res) == int:
            id = res
        else:
            id = res[0]
    return id
def insertar_red_social(conexion, nom_red_social, url_red_social):
    """
Aqui introduciremos a la base de datos la red social dada
    """
    id_red_social  = buscar_red_social(conexion,nom_red_social)
    if id_red_social is None:
        query = "INSERT INTO red_social (nom_red_social, url_red_social) VALUES (?,?)"
        datos = (nom_red_social, url_red_social)
        insertar = conexion.cursor()
        insertar.execute(query,datos)
        conexion.commit()
        return insertar.lastrowid
    else:
        print("La red social ya existe...")
        return None



def buscar_usuario(conexion,nick_usuario):
    """
Aqui buscaremos si un usuario se encuentra en nuestra base de datos
    """
    cursor = conexion.cursor()
    query ='SELECT id_usuario FROM usuario WHERE nick_usuario = "{}"'.format(nick_usuario)
    cursor.execute(query)
    res = cursor.fetchone()
    if res is None:
        id = None
    else:
        if type(res) == int:
            id = res
        else:
            id = res[0]
    return id


def buscar_juego(conexion,tit_juego, plataforma):
    """
Aqui buscaremos si un juego ya se encuentra en nuestra base de datos
    """
    cursor = conexion.cursor()
    query ="SELECT id_juego FROM juegos WHERE tit_juego = '{}' AND plataforma = '{}'".format(tit_juego, plataforma)
    cursor.execute(query)
    res = cursor.fetchone()
    if res is None:
        id = None
    else:
        if type(res) == int:
            id = res
        else:
            id = res[0]
    return id

def insertar_usuario(conexion, nick_usuario, nom_usuario, email_usuario):
    """
Aqui insertaremos un usuario dado en nuestra base de datos
    """
    id_usuario  = buscar_usuario(conexion,nom_usuario)
    if id_usuario is None:
        query = "INSERT INTO usuario (nick_usuario, nom_usuario, email_usuario) VALUES (?,?,?)"
        datos = (nick_usuario, nom_usuario, email_usuario)
        insertar = conexion.cursor()
        insertar.execute(query,datos)
        conexion.commit()
        return insertar.lastrowid
    else:
        print("El usuario ya existe...")
        return None

def insertar_juego(conexion, tit_juego, plataforma, f_publicacion):
    """
Aqui insertaremos un juego dado en nuestra base de datos
    """
    id_juego  = buscar_juego(conexion,tit_juego, plataforma)
    if id_juego is None:
        query = "INSERT INTO juegos (tit_juego, plataforma, f_publicacion) VALUES (?,?,?)"
        datos = (tit_juego, plataforma, f_publicacion)
        insertar = conexion.cursor()
        insertar.execute(query,datos)
        conexion.commit()
        return insertar.lastrowid
    else:
        print("El usuario ya existe...")
        return None

def insertar_mensaje(conexion, f_mensaje, mensaje, id_juego, id_usuario, id_red_social):
    """
   Aqui insertaremos un mensaje dado en nuestra base de datos
    """
    query = "INSERT INTO mensaje (f_mensaje, text_mensaje,id_juego, id_usuario,id_red_social) VALUES (?,?,?,?,?)"
    datos = (f_mensaje,mensaje,id_juego, id_usuario,id_red_social)
    insertar = conexion.cursor()
    insertar.execute(query, datos)
    conexion.commit()
    return insertar.lastrowid

