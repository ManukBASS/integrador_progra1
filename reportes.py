def imprimirTicket(pelicula, asientosSeleccionados, snacks, total_entradas, total_snacks, total_a_pagar,lista_recaudacion):
    lista_recaudacion.append(total_a_pagar)
    print("\n" + "="*30)
    print(" " * 9 + "TICKET DE CINE")
    print("="*30)
    print(f"Película: {pelicula[1]}".ljust(30) + f"${total_entradas:.2f}")
    print(f"Sala: {pelicula[0]}")
    print(f"Asientos: {', '.join(asientosSeleccionados)}")


    if snacks:
#         Se limita el nombre de la película a 25 caracteres para que el ticket se vea más ordenado. (SLICE)
#         Se usa slicing en los nombres de los snacks que exceden 15 caracteres, agregando "..." para que la información sea más manejable en el ticket.
        snacks_str = [f"{snack[0]} ${snack[1]:.2f}" for snack in snacks]
        print(f"Snacks: {', '.join(snacks_str)}")
    else:
        print("Snacks: Ninguno")
    
    print("="*30)
    print(" " * 5 + "¡Disfrute su película!")
    print("="*30)
    print(f"Total a pagar: ${total_a_pagar:.2f}")
    print("="*30 + "\n")

def generarReporte(lista_recaudacion, peliculas_vendidas, snacks_vendidos, usuarios):
    total_recaudacion = sum(lista_recaudacion)
    
    # Obtener la película más vista
    if peliculas_vendidas:
        pelicula_mas_vista = max(peliculas_vendidas, key=peliculas_vendidas.get)
    else:
        pelicula_mas_vista = "N/A"
    
    # Obtener el snack más vendido
    if snacks_vendidos:
        snack_mas_vendido = max(snacks_vendidos, key=snacks_vendidos.get)
    else:
        snack_mas_vendido = "N/A"
    
    # Calcular el porcentaje de usuarios registrados
    if len(lista_recaudacion) > 0:
        porcentaje_usuarios_registrados = (len(usuarios) / len(lista_recaudacion)) * 100
    else:
        porcentaje_usuarios_registrados = 0

    # Imprimir el reporte
    print("\n--- Reporte del Día ---")
    print(f"💰 Recaudación total 💰: ${total_recaudacion:.2f}")
    print(f"🎬 Película más vista 🎬: {pelicula_mas_vista} ({peliculas_vendidas.get(pelicula_mas_vista, 0)} ventas)")
    print(f"🍿 Snack más vendido 🍿: {snack_mas_vendido} ({snacks_vendidos.get(snack_mas_vendido, 0)} ventas)")
    print(f"🧍🏻‍♂️ Porcentaje de usuarios registrados 🧍🏻‍♀️: {porcentaje_usuarios_registrados:.2f}%")

