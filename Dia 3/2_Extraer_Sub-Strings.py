#Esta funcion nos va a permitir extraer partes de texto con la funcion slicing

texto = 'ABCDEFGHIJKLM'
fragmento = texto[2]
print(fragmento)

#Extraemos Desde-Hasta

texto = 'ABCDEFGHIJKLM'
fragmento = texto[2:5]
print(fragmento)

#Siguiendo, extrayendo hasta..

texto = 'ABCDEFGHIJKLM'
fragmento = texto[:5]
print(fragmento)

#Ahora extraemos desde-hasta en intervalos

texto = 'ABCDEFGHIJKLM'
fragmento = texto[2:10:2]
print(fragmento)

#Desde el primero al ultimo en intervalos de 3

texto = 'ABCDEFGHIJKLM'
fragmento = texto[::3]
print(fragmento)

#Lo mismo pero en inverso

texto = 'ABCDEFGHIJKLM'
fragmento = texto[::-1]
print(fragmento)