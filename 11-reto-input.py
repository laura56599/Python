calificacion = 0

nombre = input('cual es tu nombre: \r\n')

print ( f'Hola {nombre}')

#pregunta 1

p1 = input('Primera pregunta: ¿en que año terminó la primera guerra mundial?')

p1= int(p1)

if p1 == 1918:
     print('Es correcto, eres muy pilo!')
     calificacion = calificacion + 1
     
else:
     print('Nel, pailander!')
     
     
# pregunta 2
p2 = input ('Segunda pregunta: ¿cual era el nombre del lider la propaganda NAZI en la WWII?')

p2 = (p1)

if p2 == 'Joseph Goebbels':
    print ('Es correcto, eres muy pilo!')
    
    calificacion = calificacion + 1
    
else:
     print('Nel, pailander!')
     
     calificacion -1
     

# Pregunta 3
p3 = input ('¿Cual era el nombre de la bomba atómica?')

p3 = (p3)

if p3 == 'Little Boy':
    print ('Es correcto, eres muy pilo!')
    
    calificacion = calificacion + 1
    
else:
     print('Nel, pailander!')
     
     calificacion -1
     
if calificacion >= 3:
    print (f'Felicidades {nombre}, Tu calificacion es {calificacion}')
elif  calificacion == 2:
    print (f'no esta mal, {nombre}, Tu calificacion es {calificacion}')
else:
    print (f'jajajjaajajaj Pailander!, Tu calificacion es {calificacion}')
    
