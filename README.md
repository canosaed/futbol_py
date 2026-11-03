# Fútbol Py ⚽

Aplicación simple y didáctica en Python para administrar un equipo de **Fútbol 5**.

Diseñada especialmente para quienes están dando sus primeros pasos en Python: tiene una estructura clara, módulos separados con responsabilidades bien definidas y una interfaz de consola fácil de usar.

---

## 📁 Estructura del Proyecto

El proyecto está organizado en módulos independientes para no mezclar las funciones:

- **`carga_jugadores.py`**:
  - Contiene la lógica para validar, solicitar y crear jugadores.
  - Maneja la lectura y guardado persistente en el archivo `jugadores.txt`.

- **`conteo_jugadores.py`**:
  - Encargado de los cálculos y estadísticas del equipo.
  - Informa la cantidad total de jugadores cargados y calcula si alcanza para armar los equipos de Fútbol 5 (5 o 10 jugadores, o suplentes).
  - Permite agrupar y contar por posiciones (arquero, defensor, mediocampista, delantero), nivel de habilidad y velocidad.

- **`interfaz.py`**:
  - Menú interactivo por consola (CLI) amigable para el usuario.
  - Conecta la carga de datos con los conteos y reportes sin lógica enredada ni recursión innecesaria.

- **`test_futbol.py`**:
  - Pruebas unitarias automatizadas con `pytest` para verificar el correcto funcionamiento del sistema.

---

## 🚀 Cómo Usar la Aplicación

### 1. Iniciar la aplicación
Ejecutá en la terminal:

```bash
python3 interfaz.py
```

### 2. Opciones del menú
Al iniciar el programa verás:
1. **Ver jugadores registrados**: muestra el listado de jugadores en un formato prolijo de tabla.
2. **Cargar nuevo jugador**: asistente paso a paso para ingresar nombre, posición, nivel (regular, medio, bueno), edad y velocidad (L, M, R).
3. **Ver cantidad total de jugadores**: muestra cuántos jugadores hay en total y si alcanza para armar 1 o 2 equipos de Fútbol 5.
4. **Ver estadísticas**: desglose por posición en cancha, nivel y velocidad.
5. **Salir**: cierra la aplicación guardando todos los cambios.

---

## 🧪 Ejecución de Pruebas

Para correr los tests unitarios automatizados:

```bash
pytest
```
