#Vamos a ver las propiedades de las strings

#Son inmutables, se pueden transformar y demas pero siempre nos remitiremos a la string original
#Concatenables, usando el signo '+'
#Multiplicables, usando el signo '*'
#Multilineales, usando "\n" o tres comillas al inicio y al final
#Verificar si contiene, resultando un verdadero o falso
#Calcular longitud con la funcion lenght

#Empezamos, son inmutables

nombre = "Carina"
nombre[0] = 'K'
print(nombre)

#Concatenables

n1 = 'Kari'
n2 = 'na'
print(n1 + n2)

#Multiplicables

n1 = 'Kari'
n2 = 'na'
print(n1 * 10)

#Multilineales

poema = """Mil peque;os peces blancos
como si hirviera
el color del agua"""
print(poema)

#Se puede consultar si existe x en el string

poema = """Mil peque;os peces blancos
como si hirviera
el color del agua"""
print('agua' in poema)

poema = """Mil peque;os peces blancos
como si hirviera
el color del agua"""
print('sol' not in poema)

poema = """Mil peque;os peces blancos
como si hirviera
el color del agua"""
print('agua' not in poema)

