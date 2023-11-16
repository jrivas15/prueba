from mysql import connector


config ={
    'user': 'guest',
    'password': '66776913',
    'host': '127.0.0.1',
    'database': 'alumnos_db'
}


def crear_conexion():
    conexion = None
    try:
        conexion = connector.connect(**config)
        print('Conexion exitosa!')
        return conexion
    except connector.Error as error:
        print(f"Error conectando: {error.msg}")
        return None