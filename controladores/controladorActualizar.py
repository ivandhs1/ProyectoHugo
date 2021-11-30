
from bd import Obtener_Conexion


def actualizarCliente(documento,movil,direccion):
    conexion = Obtener_Conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET direccion = %s, movil = %s WHERE documento = %s",(direccion, movil, documento))
    conexion.commit()
    conexion.close()
