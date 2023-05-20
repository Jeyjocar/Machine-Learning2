"""13-05-2023
Array con NUMPY
Jeyfrey Calero"""


import numpy as np 



mi_Array = np.array([1,2,3,4,5])
mi_Array2 = mi_Array.view()

print(f"array 1: {mi_Array}")
print(f"array 2: {mi_Array2}")
print()

mi_Array[0]=10 # de esta manera modificamos un indice de nuestro array 
print()
print(f"array 1: {mi_Array}")
print(f"array 2: {mi_Array2}")

Mi_Array3 = np.array([6,7,8,9,10])
Mi_Array4 = Mi_Array3.copy()
print()
print('COPIADO')
print()
print(f"array 1: {Mi_Array3}")
print(f"array 2: {Mi_Array4}")

Mi_Array3[1]=45

print()
print(f"array 1: {Mi_Array3}")
print(f"array 2: {Mi_Array4}")
