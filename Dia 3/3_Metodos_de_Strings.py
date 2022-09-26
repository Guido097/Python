#Vamos a ver: upper, lower, split, join, find y replace.

#Upper

texto = 'Este es el texto de prueba'
resultado = texto.upper()
print(resultado)

texto = 'Este es el texto de prueba'
resultado = texto[2].upper()
print(resultado)

#Lower

texto = 'Este es el texto de prueba'
resultado = texto.lower()
print(resultado)

#Split

texto = 'Este es el texto de prueba'
resultado = texto.split()
print(resultado)

texto = 'Este es el texto de prueba'
resultado = texto.split('t')
print(resultado)

#Join

a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
e = ' '.join([a,b,c,d])
print(e)

#Find

texto = 'Este es el texto de prueba'
resultado = texto.find('d')
print(resultado)

#Replace

texto = 'Este es el texto de prueba'
resultado = texto.replace('prueba','Guid097')
print(resultado)

texto = 'Este es el texto de prueba'
resultado = texto.replace('s','T')
print(resultado)