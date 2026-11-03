import os
import pytest
import carga_jugadores
import conteo_jugadores


def test_crear_jugador_valido():
    jugador = carga_jugadores.crear_jugador("Lionel Messi", "delantero", "bueno", 36, "R")
    assert jugador["nombre_apellido"] == "Lionel Messi"
    assert jugador["posicion_cancha"] == "delantero"
    assert jugador["nivel_jugador"] == "BUENO"
    assert jugador["edad"] == 36
    assert jugador["velocidad"] == "R"


def test_crear_jugador_invalido():
    # Nombre vacío
    with pytest.raises(ValueError):
        carga_jugadores.crear_jugador("", "delantero", "bueno", 25, "R")

    # Nivel inválido
    with pytest.raises(ValueError):
        carga_jugadores.crear_jugador("Juan Perez", "arquero", "crack", 25, "R")

    # Edad inválida
    with pytest.raises(ValueError):
        carga_jugadores.crear_jugador("Juan Perez", "arquero", "medio", -5, "R")

    # Velocidad inválida
    with pytest.raises(ValueError):
        carga_jugadores.crear_jugador("Juan Perez", "arquero", "medio", 25, "X")


def test_guardar_y_cargar_jugadores(tmp_path):
    archivo_prueba = str(tmp_path / "jugadores_test.txt")
    jugadores_muestra = [
        {"nombre_apellido": "Dibu Martinez", "posicion_cancha": "arquero", "nivel_jugador": "BUENO", "edad": 31, "velocidad": "M"},
        {"nombre_apellido": "Cuti Romero", "posicion_cancha": "defensor", "nivel_jugador": "BUENO", "edad": 26, "velocidad": "R"}
    ]

    carga_jugadores.guardar_jugadores(jugadores_muestra, archivo=archivo_prueba)
    assert os.path.exists(archivo_prueba)

    cargados = carga_jugadores.cargar_jugadores(archivo=archivo_prueba)
    assert len(cargados) == 2
    assert cargados[0]["nombre_apellido"] == "Dibu Martinez"
    assert cargados[0]["posicion_cancha"] == "arquero"
    assert cargados[1]["nombre_apellido"] == "Cuti Romero"
    assert cargados[1]["posicion_cancha"] == "defensor"


def test_cargar_archivo_inexistente(tmp_path):
    archivo_falso = str(tmp_path / "no_existe.txt")
    resultado = carga_jugadores.cargar_jugadores(archivo=archivo_falso)
    assert resultado == []


def test_conteo_total():
    # Menos de 5
    jugadores_4 = [{"nombre_apellido": f"Jugador {i}"} for i in range(4)]
    total, msg = conteo_jugadores.contar_total(jugadores_4)
    assert total == 4
    assert "Faltan 1 para completar un equipo" in msg

    # Exactamente 5
    jugadores_5 = [{"nombre_apellido": f"Jugador {i}"} for i in range(5)]
    total, msg = conteo_jugadores.contar_total(jugadores_5)
    assert total == 5
    assert "Se completó un equipo (5)" in msg

    # Exactamente 10
    jugadores_10 = [{"nombre_apellido": f"Jugador {i}"} for i in range(10)]
    total, msg = conteo_jugadores.contar_total(jugadores_10)
    assert total == 10
    assert "justo para armar 2 equipos completos" in msg

    # Más de 10
    jugadores_12 = [{"nombre_apellido": f"Jugador {i}"} for i in range(12)]
    total, msg = conteo_jugadores.contar_total(jugadores_12)
    assert total == 12
    assert "quedan 2 suplente(s)" in msg


def test_conteos_estadisticas():
    plantel = [
        {"nombre_apellido": "J1", "posicion_cancha": "arquero", "nivel_jugador": "BUENO", "velocidad": "R"},
        {"nombre_apellido": "J2", "posicion_cancha": "defensor", "nivel_jugador": "MEDIO", "velocidad": "M"},
        {"nombre_apellido": "J3", "posicion_cancha": "mediocampo", "nivel_jugador": "REGULAR", "velocidad": "L"},
        {"nombre_apellido": "J4", "posicion_cancha": "delantero", "nivel_jugador": "BUENO", "velocidad": "R"},
        {"nombre_apellido": "J5", "posicion_cancha": "volante", "nivel_jugador": "BUENO", "velocidad": "M"}
    ]

    # Posiciones agrupadas
    agrupadas = conteo_jugadores.contar_por_posicion_agrupada(plantel)
    assert agrupadas["arquero"] == 1
    assert agrupadas["defensor"] == 1
    assert agrupadas["mediocampo"] == 2  # mediocampo + volante
    assert agrupadas["delantero"] == 1

    # Niveles
    reg, med, bno = conteo_jugadores.contar_por_nivel(plantel)
    assert reg == 1
    assert med == 1
    assert bno == 3

    # Velocidad
    l, m, r = conteo_jugadores.contar_velocidad(plantel)
    assert l == 1
    assert m == 2
    assert r == 2
