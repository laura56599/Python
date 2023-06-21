numero = 0

while numero <= 10:
    print(numero)
    numero += 1 # incrmento para evitar loop infinito

#if dentro del while    

while numero <= 10:
 
    if numero == 5:
        print('CINCOOO')
        break
    else:
           print(numero)
    numero += 1 