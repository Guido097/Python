#Para redondear se usa 'round' para eliminar la cantidad de decimales que quieras, indicando cuantos decimales quieres dejar

print(round(90/7))

#Otra forma
resultado = round(90/7)
print(resultado)

#Otra forma

resultado = 90/7
redondeo = round(resultado)

print(redondeo)

#Vamos con un ej distinto

valor = round(95.6666666666666,2)
print(valor)

#Vamos con una curiosidad

valor = round(95.6666666666666)
print(valor)
print(type(valor))

#Al ejecutar el round dentro de la variable se transforma el tipo de variable, fuera de la variable lo deja como 'float'

valor = 95.6666666666666
print(round(valor))
print(type(valor))