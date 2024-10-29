import csv

def leer_recaudacion():
    datos = []
    try:
        with open("recaudacion.csv", mode="rt") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                pelicula, snack, horario, total = row
                total = float(total)
                datos.append((pelicula, snack, horario, total))
    except FileNotFoundError:
        print("El archivo de recaudación no existe.")
    return datos

def leer_usuarios():
    usuarios = []
    try:
        with open("usuarios.txt", "rt") as file:
            for line in file:
                usuarios.append(line.strip())
    except FileNotFoundError:
        print("El archivo de usuarios no existe.")
    return usuarios

def generarReporteDiario():
    datos_recaudacion = leer_recaudacion()
    usuarios_registrados = leer_usuarios()

    recaudacion_total = sum(dato[3] for dato in datos_recaudacion)
    recaudacion_por_pelicula = {}
    
    for pelicula, snack, horario, total in datos_recaudacion:
        if pelicula not in recaudacion_por_pelicula:
            recaudacion_por_pelicula[pelicula] = 0
        recaudacion_por_pelicula[pelicula] += total

    total_entradas = sum(recaudacion_por_pelicula.values())
    ranking_peliculas = {pelicula: (recaudacion / total_entradas) * 100 for pelicula, recaudacion in recaudacion_por_pelicula.items()}
    ranking_peliculas = sorted(ranking_peliculas.items(), key=lambda x: x[1], reverse=True)

    ventas_por_horario = {}
    for pelicula, snack, horario, total in datos_recaudacion:
        if horario not in ventas_por_horario:
            ventas_por_horario[horario] = 0
        ventas_por_horario[horario] += total
    porcentaje_horarios = {horario: (total / recaudacion_total) * 100 for horario, total in ventas_por_horario.items()}

    ventas_por_snack = {}
    for pelicula, snack, horario, total in datos_recaudacion:
        if snack not in ventas_por_snack:
            ventas_por_snack[snack] = 0
        ventas_por_snack[snack] += total
    porcentaje_snacks = {snack: (total / recaudacion_total) * 100 for snack, total in ventas_por_snack.items()}

    total_usuarios = len(usuarios_registrados)
    porcentaje_usuarios_registrados = (total_usuarios / (total_usuarios + len(datos_recaudacion))) * 100

    print("📊 🟢🟡🔵 REPORTE DIARIO 🟢🟡🔵 📊")
    print("=" * 40)
    print(f"💵 Recaudación Total: ${recaudacion_total:.2f}")
    print("=" * 40)
    
    print("\n🎬 Recaudación por Película:")
    for pelicula, total in recaudacion_por_pelicula.items():
        print(f"  🎞️ {pelicula}: ${total:.2f}")
    
    print("\n🏆 Ranking de Películas (por % de Entradas Vendidas):")
    for pelicula, porcentaje in ranking_peliculas:
        print(f"  🔹 {pelicula}: {porcentaje:.2f}%")

    print("\n⏰ Porcentaje de Ventas por Horario:")
    for horario, porcentaje in porcentaje_horarios.items():
        print(f"  🕒 {horario}: {porcentaje:.2f}%")
    
    print("\n🍿 Porcentaje de Ventas por Snack:")
    for snack, porcentaje in porcentaje_snacks.items():
        print(f"  🍔 {snack}: {porcentaje:.2f}%")
    
    print(f"\n👥 Porcentaje de Usuarios Registrados: {porcentaje_usuarios_registrados:.2f}%")
    print("=" * 40)
    print("📅 ¡Fin del reporte del día!")
