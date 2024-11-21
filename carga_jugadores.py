# carga_datos.py
jugadores = [] 
def ingresar_jugadores():
    while True:
        try:
            posicion_cancha = str(input("Ingrese la posicion en cancha: ")) #Ingrese posicion (1/2/3/5/7/9/10)
            nombre_apellido = str(input("Ingrese nombre y apellido del jugador: ")) #Ingresar el nombre del jugador
            nivel_jugador = str(input("Ingrese nivel del jugador (regular/medio/bueno): ")).upper() #Indicar nivel calidad
            edad_jugador = int(input("Ingrese la edad del jugador: ")) #Ingresar la edad en número
            velocidad_jugador = str(input("Indique la velocidad promedio (L, M, R): ")).upper() #Indica velocidad promedio
            #Guardamos los datos en un diccionario para cada paciente
            jugador = {
                "posicion_cancha": posicion_cancha,
                "nombre_apellido": nombre_apellido, 
                "nivel_jugador": nivel_jugador, 
                "edad": edad_jugador, 
                "velocidad": velocidad_jugador
                }
            jugadores.append(jugador) #Agregamos el diccionario generado a la lista
            #Ver si se quiere agregar a otro jugador
            continuar = input("¿Desea agregar a otro jugador? (S/N): ").lower() 
            if continuar !='s':
                break
        except ValueError:
            print("Error en la carga de datos. Ingreselos nuevamente")