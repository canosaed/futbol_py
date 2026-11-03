"""
Módulo de interfaz de usuario para administrar un equipo de Fútbol 5.
Provee una interacción limpia y amigable por consola pensada para principiantes.
"""
import carga_jugadores
import conteo_jugadores


def mostrar_jugadores(jugadores):
    """Muestra la lista de jugadores de forma formateada y legible."""
    print("\n--- Lista de Jugadores Registrados ---")
    if not jugadores:
        print("No hay jugadores registrados todavía. Elija la opción 2 para agregar uno.")
        return

    print(f"{'#':<3} | {'Nombre y Apellido':<22} | {'Posición':<12} | {'Nivel':<10} | {'Edad':<5} | {'Velocidad':<10}")
    print("-" * 75)
    for i, j in enumerate(jugadores, start=1):
        print(f"{i:<3} | {j['nombre_apellido']:<22} | {j['posicion_cancha'].capitalize():<12} | {j['nivel_jugador']:<10} | {j['edad']:<5} | {j['velocidad']:<10}")


def opcion_ver_jugadores():
    jugadores = carga_jugadores.cargar_jugadores()
    mostrar_jugadores(jugadores)


def opcion_ingresar_jugadores():
    jugadores_actuales = carga_jugadores.cargar_jugadores()
    nuevos = carga_jugadores.ingresar_jugadores()
    if nuevos:
        jugadores_actuales.extend(nuevos)
        carga_jugadores.guardar_jugadores(jugadores_actuales)
        print(f"\n¡Se guardaron los datos! Total actual en archivo: {len(jugadores_actuales)} jugadores.")


def opcion_ver_total():
    jugadores = carga_jugadores.cargar_jugadores()
    total, mensaje = conteo_jugadores.contar_total(jugadores)
    print("\n--- Conteo Total de Jugadores ---")
    print(f"Total de jugadores registrados: {total}")
    print(f"Estado del equipo de Fútbol 5: {mensaje}")


def opcion_ver_estadisticas():
    jugadores = carga_jugadores.cargar_jugadores()
    if not jugadores:
        print("\nNo hay jugadores para mostrar estadísticas.")
        return

    print("\n--- Estadísticas del Plantel ---")

    # Posiciones agrupadas
    posiciones = conteo_jugadores.contar_por_posicion_agrupada(jugadores)
    print("\n[Distribución por Posición]")
    print(f" • Arqueros:       {posiciones['arquero']}")
    print(f" • Defensores:     {posiciones['defensor']}")
    print(f" • Mediocampistas: {posiciones['mediocampo']}")
    print(f" • Delanteros:     {posiciones['delantero']}")
    if posiciones['otros'] > 0:
        print(f" • Otras posiciones: {posiciones['otros']}")

    # Niveles
    reg, med, bno = conteo_jugadores.contar_por_nivel(jugadores)
    print("\n[Distribución por Nivel]")
    print(f" • Regular: {reg}")
    print(f" • Medio:   {med}")
    print(f" • Bueno:   {bno}")

    # Velocidad
    l, m, r = conteo_jugadores.contar_velocidad(jugadores)
    print("\n[Distribución por Velocidad]")
    print(f" • Lenta (L):  {l}")
    print(f" • Media (M):  {m}")
    print(f" • Rápida (R): {r}")


def menu():
    """Bucle principal de la interfaz de consola."""
    while True:
        print("\n" + "=" * 40)
        print("⚽  ADMINISTRADOR DE FÚTBOL 5  ⚽")
        print("=" * 40)
        print("1. Ver jugadores registrados")
        print("2. Cargar nuevo jugador")
        print("3. Ver cantidad total de jugadores")
        print("4. Ver estadísticas (posiciones, nivel, velocidad)")
        print("5. Salir")
        print("=" * 40)

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == '1':
            opcion_ver_jugadores()
        elif opcion == '2':
            opcion_ingresar_jugadores()
        elif opcion == '3':
            opcion_ver_total()
        elif opcion == '4':
            opcion_ver_estadisticas()
        elif opcion == '5':
            print("\n¡Gracias por usar el Administrador de Fútbol 5! ¡Hasta la próxima!\n")
            break
        else:
            print("Opción inválida, por favor elija una opción del 1 al 5.")


if __name__ == '__main__':
    menu()
