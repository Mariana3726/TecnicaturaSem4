class Usuario:
    # Constructor de la clase, se ejecuta al crear un objeto
    def __init__(self, id_usuario=None, username=None, password=None):
        # Atributos de la clase. Se inicializan con los valores recibidos
        self.id_usuario = id_usuario
        self._username = username
        self._password = password

    # Método que define cómo se muestra el objeto al convertirlo en string
    def __str__(self):
        return f'Usuario: {self.id_usuario} {self._username} {self._password}'

    #métodos get y set
    @property
    def id_usuario(self):
        return self._id_usuario # devuelve el atributo privado interno

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password