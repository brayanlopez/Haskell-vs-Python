import math

def sumar(lista):
	a=0
	for x in range (0,(len(lista))):
		a += lista[x]
	return a

def invertir(lista):
        i=len(lista)-1
        for x in range (0,int(len(lista)/2)):
                temp = lista[x]
                lista[x]=lista[i]
                lista[i]= temp
                i-=1
	
def igualLista(lista1,lista2):
        a=True
        if (len(lista1)==len(lista2)):
                for x in range(0,len(lista1)):
                        if (lista1[x]!=lista2[x]):
                                a=False
                                break
                return a
        else:
                return False

def lista_ordenada(lista):
        a = True
        for x in range (1,len(lista)):
                if (lista[x]<lista[x-1]):
                        a=False
        return a

def mostrar_ubicacion(lista,pos):
	return lista[pos]

def mayor(lista):
        a=0
        for x in range(0,len(lista)):
                if(lista[x]>a):
                        a=lista[x]
        return a

def contarpares(lista):
        a=0
        for x in range (0,len(lista)):
                if(lista[x]%2==0):
                        a+=1;
        return a

        
def cuadrados(lista):
        listaApoyo=lista
        for x in listaApoyo:
                listaApoyo[x-1]*=listaApoyo[x-1]
        return listaApoyo

def esPrimo(num):
        a=True
        for x in range (2,num-1):
                if (num%x==0):
                        a=False
        return a
def primos (n):
        lista=[]
        for x in range(1,n+1):
                if (esPrimo(x)):
                        lista.append(x)
        return lista


print ("Funciones")

lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[1,2,3,4,5,6,7,8,9,10]

print (mayor(lista1))
