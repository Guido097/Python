num1 = 20
num2 = 30.5

print(type(num1))
print(type(num2))

#Haciendo la siguiente operacion generamos el cambio de integer a un float
#Conversion implicita, la cual la genera automaticamente python

num1 = num1 + num2


print(type(num1))
print(type(num2))

#Pasamos a las conversiones explicitas
#transformamos el num1(float) en num2(integer)

num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))

#Ejemplo

edad = input('Dime tu edad: ')
print(type(edad))

edad = int(edad)
print(type(edad))

nueva_edad = 1 + edad
print(nueva_edad)
