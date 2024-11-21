# clasificacion_jugadores.py
#from carga_jugadores import jugadores
# Carga inicial de los jugadores desde el archivo
jugadores = []

def contar_velocidad():
    velocidad_L = len([p for p in jugadores  if p['velocidad'] == 'L'])
    velocidad_M = len([p for p in jugadores if p['velocidad'] == 'M'])
    velocidad_R = len([p for p in jugadores if p['velocidad'] == 'R'])
    return velocidad_L, velocidad_M, velocidad_R

def posicion_cancha():
    posicion_cancha_1 = len([p for p in jugadores if p['posicion_cancha'] == 'arquero'] )
    posicion_cancha_2 = len([p for p in jugadores if p['posicion_cancha'] == 'defensor'] )
    posicion_cancha_3= len([p for p in jugadores if p['posicion_cancha'] == 'central'] )
    posicion_cancha_7=  len([p for p in jugadores if p['posicion_cancha'] == 'saguero'] )
    posicion_cancha_5= len([p for p in jugadores if p['posicion_cancha'] == 'mediocampo'] )
    posicion_cancha_9 = len([p for p in jugadores if p['posicion_cancha'] == 'delantero'] )
    posicion_cancha_10= len([p for p in jugadores if p['posicion_cancha'] == 'armador'] )
    return  posicion_cancha_1, posicion_cancha_2, posicion_cancha_3 , posicion_cancha_7, posicion_cancha_5 , posicion_cancha_9 ,posicion_cancha_10 

def contar_por_nivel():
    nivel_regular = len([p for p in jugadores if p['nivel_jugador'] == 'REGULAR'])
    nivel_medio = len([p for p in jugadores if p['nivel_jugador'] == 'MEDIO'])
    nivel_bueno = len([p for p in jugadores if p['nivel_jugador'] == 'BUENO'])
    return nivel_regular, nivel_medio, nivel_bueno

def guardar_jugadores(jugadores, archivo="jugadores.txt"):
    with open(archivo, "a") as file:
        for jugador in jugadores:
            # Convierte el diccionario a una línea de texto
            linea = f"{jugador['nombre_apellido']},{jugador['velocidad']},{jugador['posicion_cancha']},{jugador['nivel_jugador']},{jugador['edad']}\n"
            file.write(linea)
    print(f"Jugadores guardados en {archivo}")
    
# Función para cargar jugadores desde un archivo .txt
def cargar_jugadores(archivo="jugadores.txt"):
    global jugadores
    jugadores_txt = []
    jugadores = jugadores_txt
    
    try:
        with open(archivo, "r") as file:
            for linea in file:
                nombre_apellido, velocidad, posicion_cancha, nivel_jugador, edad = linea.strip().split(",")
                jugadores_txt.append({
                    'nombre_apellido': nombre_apellido,
                    'velocidad': velocidad,
                    'posicion_cancha': posicion_cancha,
                    'nivel_jugador': nivel_jugador,
                    'edad': edad
                })
        # print(f"Jugadores cargados desde {archivo}")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Se creará uno nuevo al guardar jugadores.")
    return jugadores_txt

    # return None

