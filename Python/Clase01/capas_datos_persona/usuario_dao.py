from capas_datos_persona.Usuario import Usuario
from capas_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log


class UsuarioDAO:
    '''
    DAO -> Data Access Object para la tabla de usuario
    CRUD -> Create -Read - Update - Delete
    '''

    # Sentencias SQL predefinidas para las operaciones CRUD

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    # Métodos de la clase
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:  # obtiene un cursor desde el pool de conexiones
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)  # ejecuta la consulta SELECT
            registros = cursor.fetchall()  # obtiene todos los registros de la consulta
            usuarios = []
            for registro in registros:
                # crea un objeto Usuario por cada fila obtenida
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)  # valores para la consulta
            cursor.execute(cls._INSERTAR, valores)  # ejecuta la sentencia
            return cursor.rowcount  # devuelve cuántas filas fueron afectadas

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)  # tupla con un solo valor
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount


if __name__ == '__main__':
    pass
# Eliminar usuario

# usuario = Usuario(id_usuario=4)
# usuario_eliminado = UsuarioDAO.eliminar(usuario)
# log.debug(f'Usuario eliminado: {usuario_eliminado}')


# Actualizar usuario

# usuario = Usuario(id_usuario=6, username='Jonatan', password='269')
# usuario_modificado = UsuarioDAO.actualizar(usuario)
# log.debug(f'Usuario modificado: {usuario_modificado}')


# Insertar usuario

# usuario = Usuario(username='Daniel', password='751')
# usuario_insertado = UsuarioDAO.insertar(usuario)
# log.debug(f'Usuario insertado: {usuario_insertado}')


# Listar o seleccionar usuarios

# usuarios = UsuarioDAO.seleccionar()
# for usuario in usuarios:
#     log.debug(usuario)
