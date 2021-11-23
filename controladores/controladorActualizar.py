from pymysql.cursors import Cursor
from bd import Obtener_Conexion


def ActualizarNombre(documento,nombre):
    conexion = Obtener_Conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET nombre = %s WHERE documento = %s",(nombre, documento))
    conexion.commit()
    conexion.close()

def ActualizaMovil(documento,movil):
    conexion = Obtener_Conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET movil = %s WHERE documento = %s",(movil, documento))
    conexion.commit()
    conexion.close()
