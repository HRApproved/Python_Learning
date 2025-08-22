#Definiendo una variable
nombre = 'Pedro'

#Concatenar con f-strings'
bienvenida = f'Hola {nombre} Como estas?'

#Concatenar con +
bienvenida = 'Hola ' + nombre + ' Como estas?'

#Operadores de pertenencia 'in / not in'
print( 'Juan' not in bienvenida) #true
print( 'Pedro' not in bienvenida) #false
print('Pedro' in bienvenida) #true