#Proyecto para ayudar en un  negocio a que los vendedores sepan cuales van a ser sus comisiones.
#Se plantea que cada vendedor recibe como comision el 13% de las ventas realizadas.

vendedor = input('Ingrese el nombre del vendedor a cargo: ')
venta = float(input('Ingrese el monto de la venta: '))

comision = venta*13/100

print(f'La comision de {vendedor} equivale a ${round(comision,2)}')