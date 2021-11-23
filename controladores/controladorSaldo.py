from bd import Obtener_Conexion
def CambiarDeuda(documento, saldo):
    conexion = Obtener_Conexion()

    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET saldo = %s WHERE documento = %s", (saldo, documento))
    conexion.commit()
    conexion.close()
