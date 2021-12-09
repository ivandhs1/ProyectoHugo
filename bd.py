import pymysql

def Obtener_Conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='Sena1234',
                                db='bd_proyectohugo')
