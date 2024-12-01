def generarReporteEntradas(pelicula,asiento,horario):
    cantidad_asientos = len(asiento)
    nombre = pelicula["nombre"]

    try:
        archivo = open("recaudacion.csv", mode='at')
    except IOError:
        print("No se pudo abrir el archivo")
    else:
        archivo.write(nombre+";"+str(cantidad_asientos)+";"+horario+"\n")
    archivo.close()