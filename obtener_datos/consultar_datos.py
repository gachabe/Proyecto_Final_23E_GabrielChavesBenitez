import pandas as pd
import matplotlib.pyplot as plt
"""
Aqui realizaremos las consultas que después mostraremos con nuestra interfaz
"""
def consultar_comentarios_fecha(conexion, palabra_clave,f_inicio,f_fin): #apartado a)
    """
Dadas una palabra clave, una fecha inicial y una fecha inicial, ambas daadas en formato datetime, devolveremos
un DataFrame que contendrá los usuarios que, en ese rango hayan hablado de ese tema.
    """
    query = "SELECT nick_usuario" \
            " FROM usuario " \
            "WHERE id_usuario in " \
            "(SELECT id_usuario  FROM mensaje " \
            "WHERE text_mensaje like '%{}%' " \
            "AND DATE(f_mensaje) >=  DATE('{}')" \
            "AND DATE(f_mensaje) <= DATE('{}'))".format(palabra_clave,f_inicio,f_fin)

    df = pd.read_sql_query(query, conexion)
    if not df.empty:
        print(df)
        return df
    else:
        print("Hubo un error en la búsqueda")
        return None


def consultar_comentarios_cantidad(conexion): #apartado b
    """
Aqui mostraremos todos los usuarios que hayan comentado, ordenados de mayor número de comentarios a menos
    """
    query = "SELECT usuario.nick_usuario, count(mensaje.text_mensaje) as cantidad " \
            "FROM mensaje " \
            "INNER JOIN usuario ON usuario.id_usuario = mensaje.id_usuario " \
            "GROUP BY mensaje.id_usuario " \
            "ORDER BY cantidad DESC"

    df = pd.read_sql_query(query,conexion)
    print(df)
    return df


def consultar_comentarios_fecha_media(conexion,f_inicio,f_fin):
    """
 Aqui contaremos cuantos mensajes hay en un intervalo de tiempo y daremos la media de mensajes por dia
    """
    query = "SELECT red_social.nom_red_social, mensaje.text_mensaje, mensaje.f_mensaje " \
            "FROM mensaje " \
            "INNER JOIN red_social ON red_social.id_red_social = mensaje.id_red_social " \
            "WHERE DATE(f_mensaje) >=  DATE('{}') " \
            "AND DATE(f_mensaje) <= DATE('{}') ".format(f_inicio, f_fin)
    df = pd.read_sql_query(query, conexion)
    if not df.empty:
        df["f_mensaje"] = pd.to_datetime(df["f_mensaje"])
        df["dia"] = df["f_mensaje"].dt.date
        df = df.loc[:, ["nom_red_social", "dia"]]
        m_dia = df.groupby(["nom_red_social", "dia"])["dia"].count().reset_index(name='Mensajes')
        total_mensajes = m_dia["Mensajes"].sum()
        m_dia['media_mensajes'] = m_dia['Mensajes']/total_mensajes
        print(m_dia)
        m_dia.plot(x='dia', y="media_mensajes", kind='bar', figsize=(12, 8))
        plt.xticks(rotation=30)
        plt.xlabel('Días')
        plt.ylabel('Porcentaje')
        plt.title('Tanto por uno, de mensajes por día')
        plt.show()
        return m_dia

    else:
        return("Error: No hubo coincidencia con tu búsqueda")



def consultar_comentarios_red_social_media(conexion,f_inicio,f_fin): #apartado c)
    """
Aqui contaremos los mensajes escritos en un intervalo específico y daremos el porcentaje de mensajes correspondientes
a cada red social
    """
    query = "SELECT red_social.nom_red_social, mensaje.text_mensaje, mensaje.f_mensaje " \
            "FROM mensaje " \
            "INNER JOIN red_social ON red_social.id_red_social = mensaje.id_red_social " \
            "WHERE DATE(f_mensaje) >=  DATE('{}') " \
            "AND DATE(f_mensaje) <= DATE('{}') ".format(f_inicio, f_fin)
    df = pd.read_sql_query(query, conexion)
    if not df.empty:
        df["f_mensaje"] = pd.to_datetime(df["f_mensaje"])
        df["dia"] = df["f_mensaje"].dt.date
        df = df.loc[:, ["nom_red_social", "dia"]]
        m_red_social = df.groupby(["nom_red_social"])["nom_red_social"].count().reset_index(name='Mensajes')
        total_mensajes = m_red_social["Mensajes"].sum()
        m_red_social['media_mensajes'] = m_red_social['Mensajes'] / total_mensajes
        print(m_red_social)
        m_red_social.plot(x='nom_red_social', y="media_mensajes", kind='bar', figsize=(12, 8))
        plt.xticks(rotation=30)
        plt.xlabel('Red Social')
        plt.ylabel('Media')
        plt.title(f'Relación de mensajes por Red Social: {f_inicio} - {f_fin}')
        plt.show()

    else:
        return("Error: No hubo coincidencia con tu búsqueda")



def consultar_tema_red_social(conexion,*args):
    """
Aqui dado un conjunto de palabras, el cual no sabemos la cantidad, daremos los comentarios en los que
ese conjunto de palabras aparecen. Para ellos crearemos un for que añade al query principal otro query para
añadir palabras a la búsqueda.
    """
    if len(args) > 1:
        query1 = "SELECT red_social.nom_red_social FROM mensaje INNER JOIN red_social" \
                 " ON red_social.id_red_social = mensaje.id_red_social "\
                    "WHERE text_mensaje like '%{}%'".format(args[0][0])
        query2 = ""
        for i in range(len(args)):
            query2 += " AND text_mensaje like '%{}%'".format(args[0][i+1])
        query = query1+query2
    else:
        query = "SELECT red_social.nom_red_social FROM mensaje INNER JOIN red_social" \
                " ON red_social.id_red_social = mensaje.id_red_social "\
                    "WHERE text_mensaje like '%{}%'".format(args[0][0])
    print(query)
    df = pd.read_sql_query(query, conexion)
    if not df.empty:
        df = df.loc[:, ["nom_red_social"]]
        red_social_tema = df.groupby(["nom_red_social"])["nom_red_social"].count().reset_index(name='Numero_mensajes')
        print(red_social_tema)
        return(red_social_tema)
    else:
        print("Hubo un error inesperado")
        return None