def generarReporte(ventas, peliculas_vendidas, snacks, usuarios):
    total_recaudacion = sum(ventas)
    peliculas_vistas = [pelicula[0] for pelicula in peliculas_vendidas]
    pelicula_mas_vista = max(set(peliculas_vistas), key=peliculas_vistas.count)
    snack_mas_vendido = max(set(snacks), key=snacks.count)
    porcentaje_usuarios_registrados = (len(usuarios) / len(ventas)) * 100

    print("\n--- Reporte del Día ---")
    print(f"Recaudación total: ${total_recaudacion}")
    print(f"Película más vista: {pelicula_mas_vista}")
    print(f"Snack más vendido: {snack_mas_vendido}")
    print(f"Porcentaje de usuarios registrados: {porcentaje_usuarios_registrados:.2f}%")
