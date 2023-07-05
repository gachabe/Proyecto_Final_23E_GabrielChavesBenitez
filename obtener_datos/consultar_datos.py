import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


def consultar_comentarios_fecha(conexion, palabra_clave,f_inicio,f_fin):
    query = "SELECT nick_usuario" \
            " FROM usuario " \
            "WHERE id_usuario in " \
            "(SELECT id_usuario  FROM mensaje " \
            "WHERE text_mensaje like '%{}%' " \
            "AND f_mensaje >=  DATE('{}')" \
            "AND f_mensaje <= DATE('{}'))".format(palabra_clave,f_inicio,f_fin)

    df = pd.read_sql_query(query,conexion)
    print(df)

def consultar_comentarios_cantidad(conexion, palabra_clave):
    query = "SELECT usuario.nick_usuario, count(mensaje.text_mensaje) as cantidad" \
            "FROM mensaje " \
            "INNER JOIN  usuario ON usuario.id_usuario = mensaje.id_usuario" \
            "GROUP BY mensaje.id_usuario" \
            "HAVING text_mensaje like '%{}%' " \
            "ORDER  BY cantidad DESC ".format(palabra_clave)

    df = pd.read_sql_query(query,conexion)
    print(df)
def consultar_comentarios_fecha_media(conexion,f_inicio,f_fin):
    """
 Aqui contaremos cuantos mensajes hay en un intervalo de tiempo y daremos la media de mensajes por dia
    """
    query = "SELECT red_social.nom_red_social, mensaje.text_mensaje, mensaje.f_mensaje " \
            "FROM mensaje " \
            "INNER JOIN red_social ON red_social.id_red_social = mensaje.id_red_social " \
            "WHERE f_mensaje >=  DATE('{}') " \
            "AND f_mensaje <= DATE('{}') ".format(f_inicio, f_fin)
    df = pd.read_sql_query(query, conexion)
    df["f_mensaje"] = pd.to_datetime(df["f_mensaje"])
    df["dia"] = df["f_mensaje"].dt.day
    df = df.loc[:, ["nom_red_social", "f_mensaje"]]
    m_dia = df.groupby(["nom_red_social", "f_mensaje"])["f_mensaje"].count().reset_index(name='Mensajes')
    print(m_dia)



