nombre = input('cual es tu nombre: \r\n')

print ( f'Hola {nombre}')

#leer datos que serán numeros

edad = input('cual es tu edad?')

edad = int(edad)

if edad >= 18:
     print('ya puedes votar')
                 
else:
     print('aun no puedes votar')
     

#Mezclarlo con operaqdores

numero =  input('agrega un  numero y te diré si es par o non \r\n')

numero = int(numero)

if numero % 2 == 0:
    print (f'el numero {numero} es par')
else:
    print (f'el numero {numero} es impar')
    
    
    