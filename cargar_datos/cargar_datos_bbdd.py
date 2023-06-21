# Módulo para conexión y cargar inicial de los datos


#TODO: Crear funcion buscar usuario -
#TODO: Crear funcion buscar juego
#TODO: Crear funcion insertar juego
#TODO: Crear funcion insertar usuario
#TODO: insertar comentario
import sqlite3
from sqlite3 import Error

def conexion_bbdd(archivo):
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
    cursor = conexion.cursor()
    query ="SELECT id_red_social FROM red_social WHERE nom_red_social = '{}'".format(nom_red_social)
    cursor.execute(query)
    id = cursor.fetchone()
    return id

def insertar_red_social(conexion, nom_red_social, url_red_social):
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



def buscar_usuario(conexion,nom_usuario):
    cursor = conexion.cursor()
    query ="SELECT id_usuario FROM usuario WHERE nom_usuario = '{}'".format(nom_usuario)
    cursor.execute(query)
    id = cursor.fetchone()
    return id


def buscar_juego(conexion,tit_juego):
    cursor = conexion.cursor()
    query ="SELECT id_juego FROM juegos WHERE tit_juego = '{}'".format(tit_juego)
    cursor.execute(query)
    id = cursor.fetchone()
    return id

def insertar_usuario(conexion, nick_usuario, nom_usuario, email_usuario):
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
    id_juego  = buscar_juego(conexion,tit_juego)
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
