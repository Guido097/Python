#Ahora veremos listas

from dataclasses import asdict


mi_lista = ['a','b','c']
print (type(mi_lista))

#Calculamos el largo de la lista

mi_lista = ['a','b','c']
resultado = len(mi_lista)
print (resultado)

#Tambien se puede extraer el valor de un elemento, con todas las propiedades de 'index'

mi_lista = ['a','b','c']
resultado = mi_lista[0]
print (resultado)

#Se pueden aplicar concatenaciones

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
resultado = mi_lista[0:]
print (mi_lista3)

#Pasamos al siguiente tema
