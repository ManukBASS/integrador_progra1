snackDisponibles = [
    "Combo 1: Nachos + Bebida", 
    "Combo 2: Pochoclos Med + Bebida", 
    "Combo 3: Balde de Pochoclos + 2 Bebidas",
    "Combo 4: 2 Pizzetas + Bebida",
    "Sin Combo"
]

precioSnacks = [8000, 9500, 15000, 6000, 0]

def selecionarSnack():
    print("Snacks disponibles: ")
    for index, snack in enumerate(snackDisponibles):
        print(f"{index + 1}- {snack} / ${precioSnacks[index]}")
    eleccion = int(input("Seleccione el snack que desea llevar: "))
    while eleccion < 1 or eleccion > 5:
        print("Opción incorrecta, ingrese un valor válido.")
        eleccion = int(input("Seleccione el snack que desea llevar: "))
    snackElegido = snackDisponibles[int(eleccion) - 1]
    precioSnackElegido = precioSnacks[int(eleccion) -1]
    if snackElegido == 5:
        print("No se agrega Combo")
    print(f"Usted eligió: {snackElegido} - Total: ${precioSnackElegido}")
    return snackElegido, precioSnackElegido