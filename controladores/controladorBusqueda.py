from bd import Obtener_Conexion

def BuscarCliente(documento):
    conexion = Obtener_Conexion()
    
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * from clientes where documento = %s",(documento))
        cliente = cursor.fetchall()
    conexion.close()
    return cliente
    