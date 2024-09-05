def asientosDisponibles(asientos):
    print("  " + " ".join([str(i+1) for i in range(len(asientos[0]))]))
    for index, fila in enumerate(asientos):
        print(f"{chr(65+index)} " + " ".join(fila))

def seleccionarAsiento(asientos):
    asientosDisponibles(asientos)
    asiento = input("Ingrese el asiento que desea (Ej: B2): ")

    filaIndex = ord(asiento[0].upper()) - 65
    columnaIndex = int(asiento[1]) - 1

    if asientos[filaIndex][columnaIndex] == "🟢":
        asientos[filaIndex][columnaIndex] = "🔴"
        print(f"Asiento {asiento} seleccionado")
        print("")
    else:
        print("Asiento no disponible. Por favor, elija otro asiento.")
        return seleccionarAsiento(asientos)
    
    return asiento, asientos