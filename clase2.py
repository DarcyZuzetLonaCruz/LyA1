def clase2():
    lista=input("escribe un lenguaje")#input es para que el usuario ingrese un lenguaje
    
    lista2=[]#imprime
    for i in (lista): #es cada uno de los valores de la lista
        m=i #toma el primer valor
        for x in (m): #primer valor 
            if x not in lista2:#not in separa los valores de el primer valor 
                lista2.append(x)#guarda sino esta en lal ista
                
    print (lista2)            
   
from time import time
start =time()
clase2()
end=time()-start
print(end)   
        