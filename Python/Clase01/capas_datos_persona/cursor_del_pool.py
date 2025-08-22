from logger_base import log #importamos para registrar mensajes en consola o archivo
from conexion import Conexion #importamos la clase que maneja las conexiones a la base de datos


class CursorDelPool: #definimos la clase que nos permite usar with para manejar automátic la conexión y el cursor
    def __init__(self):
        #inicializamos la conexión y el cursor como None
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        #este método se ejecuta automatic al entrar al bloque with
        log.debug('Inicio del método with y __enter__')
        #conexión del pool
        self._conexion = Conexion.obtenerConexion()
        #creamos un cursor a partir de esa conexión (para ejecutar sentencias SQL)
        self._cursor = self._conexion.cursor()
        return self._cursor #devolvemos el cursor para poder usarlo dentro del bloque with

    def __exit__(self, tipo_exception, valor_exception, detalle_exception):
        log.debug('Se ejecuta el método exit')
        if valor_exception:
            self._conexion.rollback()
            log.debug(f'Ocurrio una excepción: {valor_exception}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor: #renombramos al cursor
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())



















