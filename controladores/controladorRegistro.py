from bd import Obtener_Conexion

def RegistrarCliente(documento, nombre, movil, direccion, deuda, a_favor):
    conexion = Obtener_Conexion()
    with conexion.cursor() as cursor:
        cursor.execute ("INSERT INTO clientes(documento,nombre,movil,direccion,deuda, a_favor) VALUES (%s,%s,%s,%s,%s,%s) ",(documento,nombre,movil,direccion,deuda, a_favor))
    conexion.commit()
    conexion.close()
    