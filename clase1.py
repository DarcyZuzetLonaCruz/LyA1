import random
#from turtledemo.penrose import star
#from _tracemalloc import start
def clase1():
    alfabeto=input("ingresa alfabeto")
    n=5
    m=0
    letra=""
    lista=[]
    
    while  m<=n:#checa que la cantidad de letras sea menor
        for x in range (0,len(alfabeto)): #avanza cada una de las letras del alfabeto
          
            letras=random.randint(1,5) #una letra aleatoria del alfabeto 
            letra=letra.join(random.choice(alfabeto)for _ in range(letras))#pone cada una de las letras en cada vuelta
        
            lista.append(letra)#append guarda
            letra="" #no guarda las pasadas
            m=m+1  
    
    print (lista)

from time import time
start =time()
clase1()
end=time()-start
print(end)