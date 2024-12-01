def leer_recaudacion():
    datos = []
    try:
        file = open("recaudacion.csv", mode="rt")
        
    except IOError:
        print("El archivo de recaudación no existe.")
    else:
        linea = file.readline()
        while linea:
            pelicula, snack, horario, total = linea.split(";")
            total = float(total)
            datos.append((pelicula, snack, horario, total))
            linea = file.readline()
        
    finally:
        file.close()
    return datos

def leer_usuarios():
    usuarios = []
    try:
        with open("usuarios.txt", "rt") as file:
            for line in file:
                usuarios.append(line.strip())
    except IOError:
        print("El archivo de usuarios no existe.")
    return usuarios

def generarReporteDiario():
    datos_recaudacion = leer_recaudacion()

    recaudacion_total = sum(dato[3] for dato in datos_recaudacion)
    conteo_snacks = {
        "Combo 1: Nachos + Bebida": 0,
        "Combo 2: Pochoclos Med + Bebida": 0,
        "Combo 3: Balde de Pochoclos + 2 Bebidas": 0,
        "Combo 4: 2 Pizzetas + Bebida": 0,
        "Sin Combo": 0
    }
    for pelicula, snack, horario, total in datos_recaudacion:
        if snack in conteo_snacks:
            conteo_snacks[snack] += 1  
    print("📊 🟢🟡🔵 REPORTE DIARIO 🟢🟡🔵 📊")
    print("=" * 40)
    print(f"💵 Recaudación Total: ${recaudacion_total:.2f}")
    print("=" * 40)
    print("Ranking de ventas por snack:")
    for snack, cantidad in sorted(conteo_snacks.items(), key=lambda x: x[1], reverse=True):
        print(f"{snack}: {cantidad} ventas")
    print("📅 ¡Fin del reporte del día!")
