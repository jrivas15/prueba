from mysql import connector


config ={
    'user': 'root',
    'password': '455555',
    'host': 'localhost',
    'database': 'pos_db'
}


def crear_conexion():
    conexion = None
    try:
        conexion = connector.connect(**config)
        return conexion
    except connector.Error as error:
        print(f"Error conectando: {error.msg}")
        pass