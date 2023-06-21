# revisar si una condicion es mayor a
balance = 500
if balance > 501:
    print('puedes pagar')
else:
    print('no tienes saldo')
    
#likes
likes = 200
if likes >= 200:
    print('Excelente, 200 likes')
else:
    print('Casi llegas a los 200')

#if con texto
lenguaje =  'python'

if lenguaje =='python':
    print('Excelente decisión')

#evaluar un boolean
usuario_autenticado = True

if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')
  
  
#Evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Javascrip']

if 'PHP' in lenguajes:
    print('PHP Si existe')
else:
    print('PHP No esta en la lista')


#if anidados
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
        print('Debes iniciar sesión')
