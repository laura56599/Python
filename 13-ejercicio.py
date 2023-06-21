playlist = {} #Diccionario vacío
playlist['canciones'] = [] #lista vacia de caciones

#Funcion principal
def app():
    
    #agregar playlist
    
    agregar_playlist = True
    while agregar_playlist:
            nombre_playlist = input('¿Como desea nombrar la playlist?\r\n')
            if nombre_playlist:
                playlist['nombre'] = nombre_playlist
    
                #ya  tenemos un nombre, desactivar el true
                agregar_playlist = False
                
                #manda a llamar la funcion de agregar canciones
                agregar_canciones()
                
                print (playlist)
                
def agregar_canciones():
    #bandera para agregr cancione s
    agregar_cancion = True
    
    while agregar_cancion:
        #preguntar al usuario que cancion desea agregar
        nombre_playlist =  playlist['nombre']        
        pregunta = f'\r\n agrega canciones para la playlist{nombre_playlist}: \r\n'
        pregunta =  'Escribe "X" para dejar de agregar canciones \r\n'
        
        cancion = input(pregunta)
        if cancion == 'X':
            #dejar de agregra canciones
            agregar_cancion = False
            #mostrar resumen de la playlist
            mostrar_resumen()
            
        else:
            #agregar canciones a la playlist
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'playlist: {nombre_playlist}\r\n')
    print('canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)
        
app()
    
    