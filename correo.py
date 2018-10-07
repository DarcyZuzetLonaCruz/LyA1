def correo():   
    import re
correo='nombre@dominio.ext'
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
        print "Correo correcto"
else:
    print "Correo incorrecto"

rom time import time
    start =time()
    correo()
    end=time()-start
    print(end)