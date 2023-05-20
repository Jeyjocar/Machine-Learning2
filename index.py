"""13-05-2023
Array con NUMPY
Jeyfrey Calero"""



import numpy as np 

myArray = np.array([1,2,3,4,5])
print(myArray)
print("*"*30)

myArrayBi = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(myArrayBi)
print("*"*30)

print (myArray[1])
print(myArrayBi[0,4])

print("*"*30)

prueba_1 = np.array([1,2,3])
prueba_2 = np.array([4,5,6])

print("*"*30 +' '+  'suma' +' '+ "*"*30) 
print(prueba_1 + prueba_2)
print("*"*30 +' '+  'multiplicar' + ' '+ "*"*30)
print(prueba_1 * prueba_2)

print("*"*30 +' '+  'numero menor' + ' '+ "*"*30)

print(np.min(prueba_1))

print("*"*30 +' '+  'número mayor' + ' '+ "*"*30)

print(np.max(prueba_1))

print("*"*30 +' '+  'número promedio' + ' '+ "*"*30)

print(np.mean(prueba_1))

print("*"*30 +' '+  'raíz cuadrada' + ' '+ "*"*30)

print(np.sqrt(prueba_1))

print("*"*30 +' '+  'Seno' + ' '+ "*"*30)

print(np.sin(prueba_1))

print("*"*30 +' '+  'Coseno' + ' '+ "*"*30)

print(np.cos(prueba_1))

print("*"*30 +' '+  'ceros' + ' '+ "*"*30)

resultado = np.zeros_like(prueba_1)

print(resultado)