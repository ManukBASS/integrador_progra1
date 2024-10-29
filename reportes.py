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

    try:
        file = open("recaudacion.csv", mode='at')
    except IOError:
        print("No se pudo abrir el archivo")
    else:
        snacknombre,snackprecio = snacks[0]
        ticket = (str(nombre), str(snacknombre),str(horario), f"{total_a_pagar:.2f}")
        ticket_str = ';'.join(ticket)  
        file.write(ticket_str+"\n")
    file.close()
import csv
def generarReporte(archivo_csv,index_columna=3, total_recaudacion=0, csv_reader=None):

    if csv_reader is None:
        csv_reader = csv.reader(archivo_csv)
        next(csv_reader)  # Omitir la cabecera si existe
    try:
        # Leer la siguiente fila y sumar el valor de la columna 4
        fila = next(csv_reader)
        total_recaudacion += int(fila[index_columna])
        # Llamada recursiva con la suma actualizada
        return generarReporte(archivo_csv,index_columna,total_recaudacion)
    except StopIteration:
        # Caso base: no quedan filas, cerrar archivo y retornar la suma final
        print("\n--- 💰 Reporte del Día 💰 ---")
        print(f"Total recaudado: ${total_recaudacion:.2f}")
        return total_recaudacion
        
    except IOError:
        print("No se pudo abrir el archivo")




    

