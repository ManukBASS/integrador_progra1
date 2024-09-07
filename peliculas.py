peliculas = [
    [1, "Shrek 2"],
    [2, "High School Musical 3"],
    [3, "Interestelar",],
]

salas = {
    1: [["🟢" for _ in range(6)] for _ in range(4)],  # Shrek 2
    2: [["🟢" for _ in range(6)] for _ in range(4)],  # High School Musical 3
    3: [["🟢" for _ in range(6)] for _ in range(4)],  # Interestelar
}

def seleccionarPelicula():
    print("Peliculas en cartelera: ")
    for index, pelicula in enumerate(peliculas):
        print(f"{index + 1}. Sala {pelicula[0]} - Pelicula {pelicula[1]}")

    eleccion = int(input("Seleccine el número de la película que desea ver: ")) - 1
    peliculaSeleccionada = peliculas[eleccion]
    salaSeleccionada = salas[peliculaSeleccionada[0]]
    print(f"Usted ha elegido {peliculas[eleccion][1]}")
    return peliculaSeleccionada, salaSeleccionada
