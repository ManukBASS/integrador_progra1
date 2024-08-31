snack_disponibles = [
    "Combo 1: Nachos + Bebida", 
    "Combo 2: Pochoclos Med + Bebida", 
    "Combo 3: Balde de Pochoclos + 2 Bebidas",
    "Combo 4: 2 Pizzetas + Bebida"
]

precios_snacks = [8000, 9500, 15000, 6000]

def selecionarSnack():
    print("Snacks disponibles: ")
    for index, snack in enumerate(snack_disponibles):
        print(f"{index + 1}- {snack} / ${precios_snacks[index]}")
    eleccion = int(input("Seleccione el snack que desea llevar: "))
    snackElegido = snack_disponibles[int(eleccion) - 1]
    precioSnackElegido = precios_snacks[int(eleccion) -1]
    print(f"Usted eligió: {snackElegido} - Total: ${precioSnackElegido}")
    return snackElegido, precioSnackElegido