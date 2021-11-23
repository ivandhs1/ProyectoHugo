from bd import Obtener_Conexion

def RegistrarCliente(documento, nombre, movil, saldo):
    conexion = Obtener_Conexion()
    with conexion.cursor() as cursor:
        cursor.execute ("INSERT INTO clientes(documento,nombre,movil,saldo) VALUES (%s,%s,%s,%s) ",(documento,nombre,movil,saldo))
    conexion.commit()
    conexion.close()
    