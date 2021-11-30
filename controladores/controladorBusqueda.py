from bd import Obtener_Conexion

def BuscarCliente(documento):
    conexion = Obtener_Conexion()
    
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * from clientes where documento = %s",(documento))
        cliente = cursor.fetchall()
    conexion.close()
    return cliente

def BuscarCliente2(documento):
    conexion = Obtener_Conexion()
    
    with conexion.cursor() as cursor:
        cursor.execute("SELECT direccion, movil from clientes where documento = %s",(documento))
        cliente = cursor.fetchone()
    conexion.close()
    return cliente
    