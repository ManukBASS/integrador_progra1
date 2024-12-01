import random

diccionariohorario={"14:00": [["🟢" for _ in range(6)] for _ in range(4)], 
                    "18:00": [["🟢" for _ in range(6)] for _ in range(4)], 
                    "22:00": [["🟢" for _ in range(6)] for _ in range(4)]}

peliculas = {
    1: {"nombre": "Shrek 2", "horarios": diccionariohorario.copy()},
    2: {"nombre": "High School Musical 3", "horarios": diccionariohorario.copy()},
    3: {"nombre": "Interestelar", "horarios": diccionariohorario.copy()}}

def seleccionarPelicula():
    print("Películas en cartelera: ")
    for key, pelicula in peliculas.items():
        print(f"{key}. Película: {pelicula['nombre']}")

    try:
        eleccion = int(input("Seleccione el número de la película que desea ver: "))
    except ValueError:
        print("Entrada incorrecta. Por favor, ingrese un número")
        return seleccionarPelicula()

    if eleccion in peliculas:
        peliculaSeleccionada = peliculas[eleccion]
        print(f"Usted ha elegido {peliculaSeleccionada['nombre']}")

        print("Horarios disponibles:")
        listahorarios=list(peliculaSeleccionada["horarios"].keys())
        for index, horario in enumerate(listahorarios):
            print(f"{index + 1}. {horario}")

        eleccionHorario = int(input("Seleccione el número del horario que desea: "))-1
        while eleccionHorario > len(listahorarios) or eleccionHorario < 0:
            print("Por favor ingrese un valor correcto")
            eleccionHorario = int(input("Seleccione el número del horario que desea: "))-1

        horarioSeleccionado = listahorarios[eleccionHorario]

        print(f"Usted ha elegido la película {peliculaSeleccionada['nombre']} a las {horarioSeleccionado} hs.")
        return peliculaSeleccionada, peliculaSeleccionada["horarios"][listahorarios[eleccionHorario]], horarioSeleccionado
    else:
        print("Selección no válida. Intente nuevamente.")
        return seleccionarPelicula()
def mostrarSala(sala):
    print("\n   1  2  3  4  5  6")
    filas = ['A', 'B', 'C', 'D']

    for i, fila in enumerate(sala):
        print(f"{filas[i]}  {'  '.join(fila)}")