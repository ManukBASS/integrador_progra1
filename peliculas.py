# peliculas = [
#     [1, "Shrek 2"],
#     [2, "High School Musical 3"],
#     [3, "Interestelar",],
# ]

# salas = [
# [["🟢" for _ in range(6)] for _ in range(4)],  # Shrek 2
# [["🟢" for _ in range(6)] for _ in range(4)],  # High School Musical 3
# [["🟢" for _ in range(6)] for _ in range(4)],  # Interestelar
# ]

# def seleccionarPelicula():
#     print("Peliculas en cartelera: ")
#     for index, pelicula in enumerate(peliculas):
#         print(f"{index + 1}. Sala {pelicula[0]} - Pelicula {pelicula[1]}")

#     eleccion = int(input("Seleccine el número de la película que desea ver: ")) - 1
#     peliculaSeleccionada = peliculas[eleccion]
#     salaSeleccionada = salas[peliculaSeleccionada[0]-1]
#     print(f"Usted ha elegido {peliculas[eleccion][1]}")
#     return peliculaSeleccionada, salaSeleccionada
#-------------------------------

import random

# Películas con horarios y salas
peliculas = {
    1: {"nombre": "Shrek 2", "horarios": ["14:00", "18:00", "22:00"], "numerosala":1, "sala": [["🟢" for _ in range(6)] for _ in range(4)]},
    2: {"nombre": "High School Musical 3", "horarios": ["14:00", "18:00", "22:00"], "numerosala":2, "sala": [["🟢" for _ in range(6)] for _ in range(4)]},
    3: {"nombre": "Interestelar", "horarios": ["14:00", "18:00", "22:00"],"numerosala":3, "sala": [["🟢" for _ in range(6)] for _ in range(4)]}
}

# Función para mostrar las películas y permitir la selección de una
def seleccionarPelicula():
    print("Películas en cartelera: ")
    for key, pelicula in peliculas.items():
        print(f"{key}. Película: {pelicula['nombre']}")

    eleccion = int(input("Seleccione el número de la película que desea ver: "))

    if eleccion in peliculas:
        peliculaSeleccionada = peliculas[eleccion]
        print(f"Usted ha elegido {peliculaSeleccionada['nombre']}")

        # Mostrar los horarios disponibles para la película seleccionada
        print("Horarios disponibles:")
        for index, horario in enumerate(peliculaSeleccionada["horarios"]):
            print(f"{index + 1}. {horario}")
        
        # Selección de horario
        eleccionHorario = int(input("Seleccione el número del horario que desea: ")) - 1
        horarioSeleccionado = peliculaSeleccionada["horarios"][eleccionHorario]
        
        print(f"Usted ha elegido la película {peliculaSeleccionada['nombre']} a las {horarioSeleccionado} hs.")
        return peliculaSeleccionada,peliculaSeleccionada["sala"], horarioSeleccionado
    else:
        print("Selección no válida. Intente nuevamente.")
        return seleccionarPelicula()

# Función para mostrar la sala de la película y permitir la selección de asientos
def mostrarSala(sala):
    # Mostrar las columnas numeradas
    print("\n   1  2  3  4  5  6")
    filas = ['A', 'B', 'C', 'D']  # Nombres de las filas

    # Mostrar la sala con los asientos correctamente formateados
    for i, fila in enumerate(sala):
        # Usamos '  '.join(fila) para unir los símbolos correctamente en cada fila
        print(f"{filas[i]}  {'  '.join(fila)}")

# Función para seleccionar un asiento de manera manual o aleatoria
def seleccionarAsiento(sala):
    mostrarSala(sala)

    opcion = int(input("\n¿Quiere elegir asiento o desea uno aleatorio?\n1 - Elegir\n2 - Aleatorio\nIngrese una opción: "))
    
    if opcion == 1:
        asiento = input("Ingrese el asiento que desea (Ej: B2): ").upper()
        fila = asiento[0]  # Ej: 'B'
        columna = int(asiento[1]) - 1  # Ej: '2', convierte a índice 1

        # Convertir fila en índice numérico
        fila_idx = ord(fila) - ord('A')

        # Verificar si el asiento está disponible
        if sala[fila_idx][columna] == "🟢":
            sala[fila_idx][columna] = "🔴"
            print(f"Asiento {fila}{columna+1} reservado con éxito.")
        else:
            print("El asiento ya está ocupado. Seleccione otro.")
            return seleccionarAsiento(sala)  # Volver a intentar si está ocupado

    elif opcion == 2:
        # Elegir asiento aleatorio disponible
        asientos_disponibles = [(i, j) for i in range(4) for j in range(6) if sala[i][j] == "🟢"]
        if asientos_disponibles:
            fila_idx, columna = random.choice(asientos_disponibles)
            sala[fila_idx][columna] = "🔴"
            print(f"Asiento aleatorio {chr(fila_idx + ord('A'))}{columna+1} asignado.")
        else:
            print("No quedan asientos disponibles.")
    return sala



