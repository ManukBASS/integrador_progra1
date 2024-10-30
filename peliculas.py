import random

peliculas = {
    1: {"nombre": "Shrek 2", "horarios": ["14:00", "18:00", "22:00"], "numerosala": 1, "sala": [["🟢" for _ in range(6)] for _ in range(4)]},
    2: {"nombre": "High School Musical 3", "horarios": ["14:00", "18:00", "22:00"], "numerosala": 2, "sala": [["🟢" for _ in range(6)] for _ in range(4)]},
    3: {"nombre": "Interestelar", "horarios": ["14:00", "18:00", "22:00"], "numerosala": 3, "sala": [["🟢" for _ in range(6)] for _ in range(4)]}
}

def seleccionarPelicula():
    print("Películas en cartelera: ")
    for key, pelicula in peliculas.items():
        print(f"{key}. Película: {pelicula['nombre']}")

    try:
        eleccion = int(input("Seleccione el número de la película que desea ver: "))
    except ValueError:
        print("Entrada incorrecta. Por favor, ingrese un número válido.")
        return seleccionarPelicula()

    if eleccion in peliculas:
        peliculaSeleccionada = peliculas[eleccion]
        print(f"Usted ha elegido {peliculaSeleccionada['nombre']}")

        print("Horarios disponibles:")
        for index, horario in enumerate(peliculaSeleccionada["horarios"]):
            print(f"{index + 1}. {horario}")

        try:
            eleccionHorario = int(input("Seleccione el número del horario que desea: ")) - 1
            horarioSeleccionado = peliculaSeleccionada["horarios"][eleccionHorario]
        except ValueError:
            print("Entrada incorrecta. Por favor, ingrese un número.")
            return seleccionarPelicula()
        except IndexError:
            print("Número incorrecto. Seleccione un número de la lista.")
            return seleccionarPelicula()

        print(f"Usted ha elegido la película {peliculaSeleccionada['nombre']} a las {horarioSeleccionado} hs.")
        return peliculaSeleccionada, peliculaSeleccionada["sala"], horarioSeleccionado
    else:
        print("Selección no válida. Intente nuevamente.")
        return seleccionarPelicula()
def mostrarSala(sala):
    print("\n   1  2  3  4  5  6")
    filas = ['A', 'B', 'C', 'D']

    for i, fila in enumerate(sala):
        print(f"{filas[i]}  {'  '.join(fila)}")