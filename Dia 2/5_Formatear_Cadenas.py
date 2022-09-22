# Hay 2 formas de formaatear cadenas, la 1era opcion es la funcion format, pero es dificil para el ojo humano seguir esta linea de codigo. La segunda forma de hacerlo es con cadenas literales.

#Creamos 2 variables

x = 10
y = 5

print('Mis numeros son ' + str(x) + ' y ' + str(y))

#usando la primera forma...

print('Mis numeros son {} y {}'.format(x,y))

#Otro ejemplo, esta vez haciendo una operacion

print('La suma de {} y {} es igual a {}'.format(x,y,x+y))

#Usando la segunda forma...

color = 'Rojo'
matricula = 62431

print(f'El auto es {color} y su matricula es {matricula}')
