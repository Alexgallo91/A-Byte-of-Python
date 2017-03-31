'''
Created on 27/03/2017

@author: Abraham Araujo Moreno
'''

age = 24
name = "Abraham"

print("Mi nombre es {} y tengo {} anios".format(name,age))

#decimal (.) precision of 3 for float "0.333"
print("{0:.3f}".format(1.0/3))

print("{0:_^11}".format("hello"))

print("{name} wrote {book}".format(name="Abraham", book="A byte of python"))

#imprimir sin salto de linea

print('a', end="")
print("b", end="")
print("\nsalto de linea\n",end="\n otro salto")

print("1", end=" ")
print("2", end=" \n")

#string con " y /

print("Hola soy un \\ \"salvaje\"")

print("soy un string \
continuo")

#ejemplo de un raw string, para expresiones regulares
mensaje = r"raw string\\\\"

print(mensaje)







