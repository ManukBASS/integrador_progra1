def imprimirTicket(pelicula, asientosSeleccionados, snacks, total_entradas, total_snacks, total_a_pagar, lista_recaudacion,horario):
    nombre = pelicula["nombre"]
    numerosala = pelicula["numerosala"]
    print("\n" + "="*30)
    print(" " * 9 + "TICKET DE CINE")
    print("="*30)
    print(f"Película: {nombre}".ljust(30) + f"${total_entradas:.2f}")
    print(f"Sala: {numerosala}")
    print(f"Horario: {horario} hs")
    print(f"Asientos: {', '.join(asientosSeleccionados)}")

    if snacks:
        snacks_str = [f"{snack[0][:15]} {'...' if len(snack[0]) > 15 else ''} ${snack[1]:.2f}" for snack in snacks]
        print(f"Snacks: {', '.join(snacks_str)}")
    else:
        print("Snacks: Ninguno")
    
    print("="*30)
    print(" " * 5 + "¡Disfrute su película!")
    print("="*30)
    print(f"Total a pagar: ${total_a_pagar:.2f}")
    print("="*30 + "\n")

def generarReporte(lista_recaudacion):
    total_recaudacion = sum(lista_recaudacion)
    print("\n--- 💰 Reporte del Día 💰 ---")
    print(f"Total recaudado: ${total_recaudacion:.2f}")


