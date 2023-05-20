"""13-05-2023
Array con NUMPY
Jeyfrey Calero"""


import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

pares = a[a % 2 == 0]

print(f"Estos son los números pares: {pares}")

def calculate(mi_array):
    resultado = np.zeros(len(mi_array))

    for i in range(len(mi_array)):
        resultado[i] = mi_array[i]**2
    return resultado

mi_array = np.array([1, 2, 3, 4, 5, 6])
                    
cuadrado = calculate(mi_array)
print(f"array_inicial {mi_array}")

print(f"array_inicial {cuadrado}")



