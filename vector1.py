import numpy
arreglo = numpy.random.randint(0,10,size=10)
aux = 0
for i in range(len(arreglo)):
    if i == 0:
        aux = arreglo[i]
    else:
        if aux < arreglo[i]:
            aux = arreglo[i]
            posicion = i
print(arreglo)
print("El valor más alto es:",aux,"y esta en la posicion", posicion)