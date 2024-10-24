#VERIFICAR RECURSIVIDAD EN SELEECION DE ASIENTOS

import random

def asientosDisponibles(asientos):
    print("   " + "  ".join([str(i+1) for i in range(len(asientos[0]))]))
    for index, fila in enumerate(asientos):
        print(f"{chr(65+index)} " + " ".join(fila))

def seleccionarAsiento(asientos):
    preguntaInicial = int(input("""
¿Quiere elegir asiento o desea uno aleatorio? 
1 - Elegir
2 - Aleatorio
Ingrese una opción: """))
    
    if preguntaInicial == 1:
        asientosDisponibles(asientos)
        asiento = input("Ingrese el asiento que desea (Ej: B2): ")
        filaIndex = ord(asiento[0].upper()) - 65
        columnaIndex = int(asiento[1]) - 1
        while int(asiento[1]) < 1 or int(asiento[1]) > 6 or ord(asiento[0].upper())<65 or ord(asiento[0].upper())>68 or len(asiento) > 2:
            asiento = input("Asiento inexistente. Ingrese el asiento que desea (Ej: B2): ")
            filaIndex = ord(asiento[0].upper()) - 65
            columnaIndex = int(asiento[1]) - 1
        
        

        if asientos[filaIndex][columnaIndex] == "🟢":
            asientos[filaIndex][columnaIndex] = "🔴"
            print(f"Asiento {asiento} seleccionado")
        else:
            print("Asiento no disponible. Por favor, elija otro asiento.")
            return seleccionarAsiento(asientos)

    elif preguntaInicial == 2:
        asientoSeleccionado, asientosActualizados = seleccionarAsientoAleatorio(asientos)
        asientosDisponibles(asientosActualizados)
        return asientoSeleccionado, asientosActualizados

    else:
        print("Opción incorrecta. Por favor, ingrese una opción válida.")
        return seleccionarAsiento(asientos)

    return asiento, asientos

def seleccionarAsientoAleatorio(asientos):
    filasDisponibles = [i for i, fila in enumerate(asientos) if "🟢" in fila]
    
    if not filasDisponibles:
        print("No quedan asientos disponibles.")
        return None, asientos

    filaAleatoria = random.choice(filasDisponibles)

    asientosDisponiblesEnFila = [i for i, asiento in enumerate(asientos[filaAleatoria]) if asiento == "🟢"]
    columnaAleatoria = random.choice(asientosDisponiblesEnFila)

    asientos[filaAleatoria][columnaAleatoria] = "🔴"
    asientoSeleccionado = f"{chr(65+filaAleatoria)}{columnaAleatoria + 1}"

    print(f"Se ha seleccionado aleatoriamente el asiento: {asientoSeleccionado}")
    
    return asientoSeleccionado, asientos



