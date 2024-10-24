snacks = [
    [1, "Combo 1: Nachos + Bebida", 8000],
    [2, "Combo 2: Pochoclos Med + Bebida", 9500],
    [3, "Combo 3: Balde de Pochoclos + 2 Bebidas", 15000],
    [4, "Combo 4: 2 Pizzetas + Bebida", 6000],
    [5, "Sin Combo", 0]
]

def seleccionarSnack():
    try:
        print("Snacks disponibles: ")
        for snack in snacks:
            print(f"{snack[0]}- {snack[1]} / ${snack[2]}")
        eleccion = int(input("Seleccione el snack que desea llevar: "))
        1/eleccion
        if eleccion < 0:
            raise ValueError
        print(f"Usted eligió: {snackElegido[1]} - Total: ${snackElegido[2]}")
        
        return snackElegido[1], snackElegido[2]
    except IndexError:
        print("Opción incorrecta, ingrese un valor válido.")
        seleccionarSnack()
    except ValueError:
        print("Opción incorrecta, ingrese un valor válido.")
        seleccionarSnack()
    except ZeroDivisionError:
        print("Opción incorrecta, ingrese un valor válido.")
        seleccionarSnack()