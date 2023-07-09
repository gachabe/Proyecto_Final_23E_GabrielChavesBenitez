#Aqui definiremos las funcionalidades de la GUI

from procesar_mensajes import procesar_mensajes_metacritic as meta
from procesar_mensajes import procesar_mensajes_playstore as play

def carga_inicial(conexion):
    """
    Aqui cargaremos una serie de comentarios y juegos preseleccionados

    """
    try:
        play.cargar_comentario_playstore(conexion)
        meta.cargar_videojuegos_metacritic(conexion)
        meta.cargar_comentario_metacritic(conexion, "The Legend of Zelda: Ocarina of Time", "Nintendo64")
        meta.cargar_comentario_metacritic(conexion, "Final Fantasy IX", "PlayStation")
        meta.cargar_comentario_metacritic(conexion, "God of War", "PlayStation2")
        conexion.commit()
        return "Juegos cargados correctamente"
    except Exception as e:
        print("Hubo un error imprevisto:", str(e))

def borrar_datos(conexion):
    """
    Aqui se elimnarán los datos de comentarios, juegos y usuarios para poder hacer pruebas, se dejará la implementación
    en el resultado final para una evaluación más sencilla
    """
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM mensaje"
        cursor.execute(query)
        query = "DELETE FROM usuario"
        cursor.execute(query)
        query = "DELETE FROM juegos"
        cursor.execute(query)
        conexion.commit()
        return "Datos limpiados correctamente"
    except Exception as e:
        print("Hubo un error imprevisto:", str(e))
