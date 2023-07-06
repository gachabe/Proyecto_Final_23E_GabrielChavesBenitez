import pandas as pd
import matplotlib.pyplot as plt
#TODO apartado 1
#TODO apartado 2
#TODO apartado 4

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



def consultar_comentarios_red_social_media(conexion,f_inicio,f_fin):
    query = "SELECT red_social.nom_red_social, mensaje.text_mensaje, mensaje.f_mensaje " \
            "FROM mensaje " \
            "INNER JOIN red_social ON red_social.id_red_social = mensaje.id_red_social " \
            "WHERE f_mensaje >=  DATE('{}') " \
            "AND f_mensaje <= DATE('{}') ".format(f_inicio, f_fin)
    df = pd.read_sql_query(query, conexion)
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
    plt.title(f'Media de mensajes por Red Social entre: {f_inicio} - {f_fin}')
    plt.show()



