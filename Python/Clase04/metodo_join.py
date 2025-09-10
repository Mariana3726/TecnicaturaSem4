

#help(str.join)

tupla_str = ('Hola', 'mundo', 'tecnicatura')
mensaje = ' '.join(tupla_str)
print(f'Mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(f'Mensaje: {mensaje}')

cadena = 'Holamundo'
mensaje = '. '.join(cadena)
print(f'Mensaje: {mensaje}')

diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': '18'}
llaves = '-'.join(diccionario)
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves},'
      f'Type: {type(llaves)}')
print(f'Valores: {valores}, Type: {type(valores)}')