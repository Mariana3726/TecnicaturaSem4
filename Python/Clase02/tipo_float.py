# Profundizamos en el tipo float
a = 3.0
print(f'a: {a:.2f}')

# Constructor de tipo float: puede recibir enteros y de tipo string
a = float(10) #le pasamos un tipo entero
print(f'a: {a:.2f}')

a = float('10')
print(f'a: {a:.2f}')

# Notación exponencial (valores + o -)
a = 3e5
print(f'a: {a:.2f}')

a = 3e-5
print(f'a: {a:.5f}')

# Cualquier cálculo que incluye un float, todo cambia a float

a = 4.0 + 5
print(a)
print(type(a))


















