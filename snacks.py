snacks = [
    [1, "Combo 1: Nachos + Bebida", 8000],
    [2, "Combo 2: Pochoclos Med + Bebida", 9500],
    [3, "Combo 3: Balde de Pochoclos + 2 Bebidas", 15000],
    [4, "Combo 4: 2 Pizzetas + Bebida", 6000],
    [5, "Sin Combo", 0]
]

def seleccionarSnack():
    print("Snacks disponibles: ")
    for snack in snacks:
        print(f"{snack[0]}- {snack[1]} / ${snack[2]}")
    eleccion = int(input("Seleccione el snack que desea llevar: "))

    while eleccion < 1 or eleccion > 5:
        print("Opción incorrecta, ingrese un valor válido.")
        eleccion = int(input("Seleccione el snack que desea llevar: "))
    
    snackElegido = snacks[eleccion - 1]
    print(f"Usted eligió: {snackElegido[1]} - Total: ${snackElegido[2]}")
    
    return eleccion, snackElegido[1], snackElegido[2]
