def leer_recaudacion():
    datos = []
    try:
        file = open("recaudacion.csv", mode="rt")
        
    except IOError:
        print("El archivo de recaudación no existe.")
    else:
        linea = file.readline()
        while linea:
            pelicula, snack, total = linea.split(";")
            total = float(total)
            datos.append((pelicula, snack, total))
            linea = file.readline()
        
    finally:
        file.close()
    return datos

def leer_ranking():
    datospeliculas = []
    try:
        file = open("reportepeliculas.csv", mode="rt")          
    except IOError:
        print("El archivo de recaudación de las peliculas no existe.")
    else:
        linea = file.readline()
        while linea:
            pelicula, total_entradas, horario = linea.split(";")
            datospeliculas.append((pelicula, total_entradas, horario ))
            linea = file.readline() 
    finally:
        file.close()
    return datospeliculas


def generarReporteDiario():
    datos_recaudacion = leer_recaudacion()

    recaudacion_total = sum(dato[2] for dato in datos_recaudacion)

    conteo_snacks = {
        "Combo 1: Nachos + Bebida": 0,
        "Combo 2: Pochoclos Med + Bebida": 0,
        "Combo 3: Balde de Pochoclos + 2 Bebidas": 0,
        "Combo 4: 2 Pizzetas + Bebida": 0,
        "Sin Combo": 0
    }
    for pelicula, snack, total in datos_recaudacion:
        if snack in conteo_snacks:
            conteo_snacks[snack] += 1
    
    datos_peliculas = leer_ranking()
    conteo_peliculas = {
        "Shrek 2": 0,
        "High School Musical 3": 0,
        "Interestelar": 0,
    }
    conteo_horarios = {
        "14:00": 0,
        "18:00": 0,
        "22:00": 0,
    }
    for pelicula, total_entradas, horario in datos_peliculas:
        if pelicula in conteo_peliculas:
            conteo_peliculas[pelicula] += int(total_entradas)
        if horario.strip() in conteo_horarios:
            conteo_horarios[horario.strip()] += int(total_entradas)




    
      
    print("📊 🟢🟡🔵 REPORTE DIARIO 🟢🟡🔵 📊")
    print("=" * 40)
    print(f"💵 Recaudación Total: ${recaudacion_total:.2f}")
    print("=" * 40)
    print("Ranking de ventas por snack:")
    for snack, cantidad in sorted(conteo_snacks.items(), key=lambda x: x[1], reverse=True):
        print(f"{snack}: {cantidad} ventas")
    print("=" * 40)
    print("Ranking de ventas por pelicula:")
    for pelicula, cantidad in sorted(conteo_peliculas.items(), key=lambda x: x[1], reverse=True):
        print(f"{pelicula}: {cantidad} entradas vendidas para esta pelicula")
    print("=" * 40)
    print("Ranking de ventas por horario:")
    for horario, cantidad in sorted(conteo_horarios.items(), key=lambda x: x[1], reverse=True):
        print(f"{horario}: {cantidad} entradas vendidas para este horario")
    print("📅 ¡Fin del reporte del día!")
