import math
from decimal import Decimal

# NaN (Not a Number)
a = float('NaN')
print(f'a: {a}')

# Módulo math
a = float('nan')
print(f'Es de tipo NaN?: {math.isnan(a)}') #Va a imprimir true

# Módulo decimal
a = Decimal('2.0')
print(f'Es de tipo NaN?: {math.isnan(a)}')