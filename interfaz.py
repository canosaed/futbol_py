# interfaz.py
import carga_jugadores
import conteo_jugadores
def menu():
    while True:
        print("\n--- Menú de opciones ---")
        print("0. Ver jugadores")
        print("1. Ingresar jugadores")
        print("2. muestra la posicion en cancha")
        print("3. jugadores por nivel")
        print("4. Mostrar por velocidad")
        # print("5. Guardar")
        print("5. Salir")

        #jugadores = conteo_jugadores.cargar_jugadores()  # Cargar jugadores al inicio
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '0':
            jtxt = conteo_jugadores.cargar_jugadores()
            print("\n--- Jugadores registrados ---")
            if not jtxt:
                print("No hay jugadores registrados.")
                menu()
            else:
                for jugador in jtxt:
                    print(f"Nombre: {jugador['nombre_apellido']}, Velocidad: {jugador['velocidad']}, Posición: {jugador['posicion_cancha']} , Nivel: {jugador['nivel_jugador']}, Edad: {jugador['edad']}")
                menu() 
        
        
        if opcion == '1':
            carga_jugadores.ingresar_jugadores()  # Solo ingresa jugadores si seleccionas esta opción
            #jugadores.extend(carga_jugadores.jugadores)  # Agregar nuevos jugadores a la lista en memoria
            conteo_jugadores.guardar_jugadores(carga_jugadores.jugadores) # Guarda la lista actualizada en el archivo
        
        elif opcion == '2':
            resultado = conteo_jugadores.posicion_cancha()
            if isinstance(resultado, str):  # Si no hay jugadores
                print(resultado)
            else:    #posicion del 1/2/3/4/5/7/9/10
                posicion_cancha_1, posicion_cancha_2, posicion_cancha_3, posicion_cancha_7, posicion_cancha_5, posicion_cancha_9, posicion_cancha_10 = resultado
                print (f"arqueros : {posicion_cancha_1}, defensores: {posicion_cancha_2}, centrales: {posicion_cancha_3} , mediocampo:{posicion_cancha_5}, saguero : {posicion_cancha_7}, delantero:{posicion_cancha_9}, armador:{posicion_cancha_10} ")
        
        
        elif opcion == '3':
            resultado = conteo_jugadores.contar_por_nivel()
            if isinstance(resultado, str):  # Si no hay jugadores
                print(resultado)
            else:
                nivel_regular, nivel_medio, nivel_bueno = resultado
                print(f"jugadores nivel regular: {nivel_regular}, jugadores nivel medio: {nivel_medio} , jugadores nivel bueno: {nivel_bueno}")
          
        elif opcion == '4':
            resultado= conteo_jugadores.contar_velocidad()
            if isinstance(resultado, str):  # Si no hay jugadores
                print(resultado)
            else:
                velocidad_L,velocidad_M,velocidad_R = resultado
                print (f"velocidad_jugador L: {velocidad_L},velocidad_jugador M: {velocidad_M},velocidad_jugador R: {velocidad_R}")
       
        # elif opcion == '6':
        #     conteo_jugadores.guardar_jugadores(carga_jugadores.jugadores)
        #     print("guardando...")
       
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida, por favor intente nuevamente.")

if __name__ == '__main__':
    menu()  # Siempre inicia mostrando el menú primero
