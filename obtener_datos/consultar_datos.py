import pandas as pd
def consultar_comentarios_fecha(conexion, palabra_clave,f_inicio,f_fin):
    query = "SELECT * FROM mensaje WHERE text_mensaje like"
    df = pd.read_sql_query(query,conexion)
    print(df)