from bd import Obtener_Conexion

def listando():
    conexion = Obtener_Conexion()
    clientes=None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT documento, nombre, movil, direccion, deuda, aFavor FROM clientes")
        clientes=cursor.fetchall()
    conexion.close()
    return clientes
    
