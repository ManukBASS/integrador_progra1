def imprimirTicket(pelicula, asientosSeleccionados, snacks, total_entradas, total_snacks, total_a_pagar,lista_recaudacion):
    lista_recaudacion.append(total_a_pagar)
    print("\n" + "="*30)
    print(" " * 9 + "TICKET DE CINE")
    print("="*30)
    print(f"Película: {pelicula[1]}".ljust(30) + f" ${total_entradas:.2f}")
    print(f"Sala: {pelicula[0]}")
    print(f"Asientos: {', '.join(asientosSeleccionados)}")

    if snacks:
        snacks_str = [f"{snack[0]} ${snack[1]:.2f}" for snack in snacks]
        print(f"Snacks: {', '.join(snacks_str)}")
    else:
        print("Snacks: Ninguno")
    
    print("="*30)
    print(" " * 5 + "¡Disfrute su película!")
    print("="*30)
    print(f"Total a pagar: ${total_a_pagar:.2f}")
    print("="*30 + "\n")

def generarReporte(total_a_pagar, recaudacionDiaria):
    recaudacionDiaria.append(total_a_pagar)
    total_recaudacion = sum(recaudacionDiaria)

    # Imprimir el reporte
    print("\n--- Reporte del Día ---")
    print(f"💰 Recaudación total 💰: ${total_recaudacion:.2f}")