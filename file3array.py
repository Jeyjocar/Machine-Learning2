"""13-05-2023
Array con NUMPY
Jeyfrey Calero"""

import numpy as np

new_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(new_array[1:6]) #imprime del 2 al 6
print(new_array[4:10]) #imprime del 5 al 10
print(new_array[-4:-3]) # imprime del 7 al 8
print(new_array[1:10:2]) #imprime pares [1::2] 
print(new_array[0:9:2]) #imprime impares [::2]
