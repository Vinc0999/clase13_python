import random #libreria para llamar y crear numeros randoms

numeros=[]#coleccion vacia

for i in range(10):#ciclo para repetir 100 veces la iteracion
    numeros.append(random.randint(1,100))#guardamos en la lista el numero

numero=random.randint(1,100)#rango para el numero

print(numeros)#visualizamos lista

#contador de numeros pares
contador=0
for i in range(len(numeros)):
    if numeros[i]%2==0:
        contador+=1
print(f"cantidad de numeros pares : {contador}")