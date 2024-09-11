def imprimirTicket(pelicula, asientosSeleccionados, snacks, total_entradas, total_snacks, total_a_pagar, lista_recaudacion):
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

def generarReporte(recaudacionDelDia, peliculas_vendidas, snacks_vendidos, usuarios_registrados, total_usuarios):
    total_recaudacion = sum(recaudacionDelDia)

    pelicula_mas_vendida_index = peliculas_vendidas.index(max(peliculas_vendidas))
    peliculas = ["Shrek 2", "High School Musical 3", "Interestelar"]
    pelicula_mas_vendida = peliculas[pelicula_mas_vendida_index]

    snack_mas_vendido_index = snacks_vendidos.index(max(snacks_vendidos))
    snacks = ["Combo 1: Nachos + Bebida", "Combo 2: Pochoclos Med + Bebida", "Combo 3: Balde de Pochoclos + 2 Bebidas", "Combo 4: 2 Pizzetas + Bebida"]
    snack_mas_vendido = snacks[snack_mas_vendido_index]

    porcentaje_usuarios_registrados = (usuarios_registrados / total_usuarios) * 100

    print("\n--- Reporte del Día ---")
    print(f"💰 Recaudación total 💰: ${total_recaudacion:.2f}")
    print(f"🎬 Película más vendida 🎬: {pelicula_mas_vendida}")
    print(f"🍿 Snack más vendido 🍿: {snack_mas_vendido}")
    print(f"👤 Porcentaje de usuarios registrados 👤: {porcentaje_usuarios_registrados:.2f}%")
