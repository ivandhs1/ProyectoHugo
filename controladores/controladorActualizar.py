
from bd import Obtener_Conexion


def ActualizarDireccion(documento,direccion):
    conexion = Obtener_Conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET direccion = %s WHERE documento = %s",(direccion, documento))
    conexion.commit()
    conexion.close()

def ActualizaMovil(documento,movil):
    conexion = Obtener_Conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET movil = %s WHERE documento = %s",(movil, documento))
    conexion.commit()
    conexion.close()
