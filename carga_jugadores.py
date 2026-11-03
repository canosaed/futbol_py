"""
Módulo para la carga y persistencia de jugadores de Fútbol 5.
"""
import os

ARCHIVO_JUGADORES = "jugadores.txt"
jugadores = []


def crear_jugador(nombre_apellido, posicion_cancha, nivel_jugador, edad, velocidad):
    """Crea y valida un diccionario con los datos de un jugador."""
    nombre = nombre_apellido.strip()
    if not nombre:
        raise ValueError("El nombre y apellido no pueden estar vacíos.")

    posicion = posicion_cancha.strip().lower()
    if not posicion:
        raise ValueError("La posición en cancha no puede estar vacía.")

    nivel = nivel_jugador.strip().upper()
    if nivel not in ["REGULAR", "MEDIO", "BUENO"]:
        raise ValueError("El nivel debe ser 'regular', 'medio' o 'bueno'.")

    edad = int(edad)
    if edad <= 0 or edad > 100:
        raise ValueError("La edad debe ser un número positivo razonable.")

    velocidad = velocidad.strip().upper()
    if velocidad not in ["L", "M", "R"]:
        raise ValueError("La velocidad debe ser 'L' (lenta), 'M' (media) o 'R' (rápida).")

    return {
        "nombre_apellido": nombre,
        "posicion_cancha": posicion,
        "nivel_jugador": nivel,
        "edad": edad,
        "velocidad": velocidad
    }


def guardar_jugadores(lista_jugadores, archivo=ARCHIVO_JUGADORES):
    """Guarda la lista completa de jugadores en el archivo de texto."""
    with open(archivo, "w", encoding="utf-8") as f:
        for jugador in lista_jugadores:
            linea = f"{jugador['nombre_apellido']},{jugador['velocidad']},{jugador['posicion_cancha']},{jugador['nivel_jugador']},{jugador['edad']}\n"
            f.write(linea)


def cargar_jugadores(archivo=ARCHIVO_JUGADORES):
    """Lee y carga la lista de jugadores desde el archivo de texto."""
    global jugadores
    jugadores_cargados = []
    if not os.path.exists(archivo):
        jugadores = jugadores_cargados
        return jugadores_cargados

    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            if len(partes) == 5:
                nombre_apellido, velocidad, posicion_cancha, nivel_jugador, edad = partes
                try:
                    jugador = {
                        "nombre_apellido": nombre_apellido.strip(),
                        "velocidad": velocidad.strip().upper(),
                        "posicion_cancha": posicion_cancha.strip().lower(),
                        "nivel_jugador": nivel_jugador.strip().upper(),
                        "edad": int(edad.strip())
                    }
                    jugadores_cargados.append(jugador)
                except ValueError:
                    continue
    jugadores = jugadores_cargados
    return jugadores_cargados


def pedir_datos_jugador():
    """Solicita los datos de un único jugador por teclado."""
    print("\n--- Ingreso de Nuevo Jugador ---")
    while True:
        nombre = input("Ingrese nombre y apellido del jugador: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    posiciones_validas = ["arquero", "defensor", "mediocampo", "delantero"]
    print(f"Posiciones sugeridas: {', '.join(posiciones_validas)}")
    while True:
        posicion = input("Ingrese la posición en cancha: ").strip().lower()
        if posicion:
            break
        print("La posición no puede estar vacía.")

    while True:
        nivel = input("Ingrese nivel del jugador (regular / medio / bueno): ").strip().upper()
        if nivel in ["REGULAR", "MEDIO", "BUENO"]:
            break
        print("Por favor, ingrese REGULAR, MEDIO o BUENO.")

    while True:
        try:
            edad = int(input("Ingrese la edad del jugador: "))
            if 5 <= edad <= 100:
                break
            print("Ingrese una edad válida (entre 5 y 100 años).")
        except ValueError:
            print("Por favor, ingrese un número entero para la edad.")

    while True:
        velocidad = input("Indique la velocidad promedio (L = Lento, M = Medio, R = Rápido): ").strip().upper()
        if velocidad in ["L", "M", "R"]:
            break
        print("Opción inválida. Ingrese 'L', 'M' o 'R'.")

    return crear_jugador(nombre, posicion, nivel, edad, velocidad)


def ingresar_jugadores():
    """Permite el ingreso interactivo de jugadores por consola."""
    global jugadores
    nuevos = []
    while True:
        jugador = pedir_datos_jugador()
        jugadores.append(jugador)
        nuevos.append(jugador)
        print(f"¡Jugador {jugador['nombre_apellido']} agregado con éxito!")

        continuar = input("\n¿Desea agregar a otro jugador? (S/N): ").strip().lower()
        if continuar != 's':
            break
    return nuevos
