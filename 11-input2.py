pregunta = 'agrega un  numero y te diré si es par o impar \r\n'
pregunta += 'escribe "Cerrar" para salir de la aplicacion"\r\n'

preguntar = True

while preguntar:
    numero =  input(pregunta)
    
    if numero == 'cerrar':
        pregunta = False
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print (f'el numero {numero} es par')
        else:
            print (f'el numero {numero} es impar')
    