#Creando una lista (se pueden modificar)
lista =['tilin', 'pepe', True, 1.79]

#Creando una tupla (no se pueden modificar)
tupla = ('tilin', 'pepe', True, 1.79)

#tupla[3]= 1.80 #ERROR (no puedo cambiar el valor del [3] en tupla)
#print(tupla[3]) 

lista[0] = 'fermin' #Si puedo cambiar el valor de [0] en lista
print (lista[0])

#Creando un conjunto (set) (no se puede acceder a un conjunto por indice, no almacena datos duplicados)
conjunto = {'tilin', 'pepe', True, 1.79}
print(conjunto)

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {'nombre': 'tilin', 'edad': 5, 'es_mascota': True}
print(diccionario['edad'])