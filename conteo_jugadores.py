"""
Módulo para realizar conteos y estadísticas de jugadores de Fútbol 5.
"""
from carga_jugadores import cargar_jugadores, guardar_jugadores

# Lista en memoria para compatibilidad
jugadores = []


def contar_total(lista_jugadores=None):
    """
    Cuenta la cantidad total de jugadores y devuelve un resumen del equipo para Fútbol 5.
    Para Fútbol 5 se necesitan 5 jugadores por equipo (10 para un partido completo).
    """
    if lista_jugadores is None:
        lista_jugadores = cargar_jugadores()

    total = len(lista_jugadores)

    # Evaluación del estado para Fútbol 5
    if total < 5:
        mensaje = f"Hay {total} jugador(es). Faltan {5 - total} para completar un equipo de Fútbol 5."
    elif total < 10:
        mensaje = f"Hay {total} jugador(es). Se completó un equipo (5), faltan {10 - total} para armar 2 equipos (10 jugadores)."
    elif total == 10:
        mensaje = f"¡Perfecto! Hay 10 jugadores, justo para armar 2 equipos completos de Fútbol 5."
    else:
        suplentes = total - 10
        mensaje = f"Hay {total} jugadores. Se pueden armar 2 equipos de 5 y quedan {suplentes} suplente(s)/cambio(s)."

    return total, mensaje


def posicion_cancha(lista_jugadores=None):
    """Cuenta los jugadores según su posición en la cancha."""
    if lista_jugadores is None:
        lista_jugadores = cargar_jugadores()

    posicion_cancha_1 = len([p for p in lista_jugadores if p.get('posicion_cancha') in ['arquero', '1']])
    posicion_cancha_2 = len([p for p in lista_jugadores if p.get('posicion_cancha') in ['defensor', '2']])
    posicion_cancha_3 = len([p for p in lista_jugadores if p.get('posicion_cancha') in ['central', '3']])
    posicion_cancha_7 = len([p for p in lista_jugadores if p.get('posicion_cancha') in ['saguero', 'zaguero', '7']])
    posicion_cancha_5 = len([p for p in lista_jugadores if p.get('posicion_cancha') in ['mediocampo', 'medio', '5']])
    posicion_cancha_9 = len([p for p in lista_jugadores if p.get('posicion_cancha') in ['delantero', '9']])
    posicion_cancha_10 = len([p for p in lista_jugadores if p.get('posicion_cancha') in ['armador', '10']])

    return (
        posicion_cancha_1,
        posicion_cancha_2,
        posicion_cancha_3,
        posicion_cancha_7,
        posicion_cancha_5,
        posicion_cancha_9,
        posicion_cancha_10
    )


def contar_por_posicion_agrupada(lista_jugadores=None):
    """
    Retorna un diccionario simple agrupando en las 4 posiciones típicas de Fútbol 5:
    Arquero, Defensor, Mediocampista, Delantero (y Otros).
    """
    if lista_jugadores is None:
        lista_jugadores = cargar_jugadores()

    conteo = {
        "arquero": 0,
        "defensor": 0,
        "mediocampo": 0,
        "delantero": 0,
        "otros": 0
    }

    for p in lista_jugadores:
        pos = p.get('posicion_cancha', '').lower()
        if pos in ['arquero', '1', 'portero']:
            conteo['arquero'] += 1
        elif pos in ['defensor', 'central', 'saguero', 'zaguero', '2', '3', '7', 'lateral']:
            conteo['defensor'] += 1
        elif pos in ['mediocampo', 'medio', 'armador', 'volante', '5', '10']:
            conteo['mediocampo'] += 1
        elif pos in ['delantero', 'punta', 'atacante', '9']:
            conteo['delantero'] += 1
        else:
            conteo['otros'] += 1

    return conteo


def contar_por_nivel(lista_jugadores=None):
    """Cuenta los jugadores según su nivel técnico."""
    if lista_jugadores is None:
        lista_jugadores = cargar_jugadores()

    nivel_regular = len([p for p in lista_jugadores if p.get('nivel_jugador') == 'REGULAR'])
    nivel_medio = len([p for p in lista_jugadores if p.get('nivel_jugador') == 'MEDIO'])
    nivel_bueno = len([p for p in lista_jugadores if p.get('nivel_jugador') == 'BUENO'])
    return nivel_regular, nivel_medio, nivel_bueno


def contar_velocidad(lista_jugadores=None):
    """Cuenta los jugadores según su velocidad promedio."""
    if lista_jugadores is None:
        lista_jugadores = cargar_jugadores()

    velocidad_L = len([p for p in lista_jugadores if p.get('velocidad') == 'L'])
    velocidad_M = len([p for p in lista_jugadores if p.get('velocidad') == 'M'])
    velocidad_R = len([p for p in lista_jugadores if p.get('velocidad') == 'R'])
    return velocidad_L, velocidad_M, velocidad_R
