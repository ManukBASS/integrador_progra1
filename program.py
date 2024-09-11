
from users import loginUsuarios
from snacks import seleccionarSnack
from peliculas import seleccionarPelicula
from asientos import seleccionarAsiento
from reportes import imprimirTicket

def main(): 
    PRECIO_ENTRADA = 4000
    recaudacion = []
    
    # Diccionarios para contar las películas y snacks vendidos
    peliculas_vendidas = {}   # Diccionario para acumular las películas
    snacks_vendidos = {}      # Diccionario para acumular los snacks
    usuarios = ["manuzarraga99", "milinunes99", "micaflores96"]  # Lista de usuarios registrados

    flagContinue = True

    while flagContinue:
        # Login del usuario y posible descuento
        descuento = loginUsuarios(recaudacion, peliculas_vendidas, snacks_vendidos, usuarios)  # Pasar las listas adicionales

        # Revisar si se generó el reporte y reiniciar
        if descuento == 'reporte':
            print("Excelente recaudacion! Nos vemos mañana :)")
            break  # Rompe el bucle principal para reiniciar

        # Seleccionar película y sala
        pelicula, sala = seleccionarPelicula()

        # Registrar la película en el diccionario
        if pelicula[1] in peliculas_vendidas:
            peliculas_vendidas[pelicula[1]] += 1
        else:
            peliculas_vendidas[pelicula[1]] = 1

        # Snacks
        snacksSeleccionados = []
        snack_elegido = seleccionarSnack()
        snacksSeleccionados.append(snack_elegido)

        # Registrar el snack en el diccionario
        if snack_elegido[0] in snacks_vendidos:
            snacks_vendidos[snack_elegido[0]] += 1
        else:
            snacks_vendidos[snack_elegido[0]] = 1

        total_snacks = snack_elegido[1]  # Precio del snack seleccionado

        # Asientos
        asientosSeleccionados = []
        asiento, sala = seleccionarAsiento(sala)
        asientosSeleccionados.append(asiento)
        total_entradas = PRECIO_ENTRADA  # Precio inicial para una entrada

        # Selección de más asientos
        otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Sí
2 - No
-1  Salir                                
Ingrese una opción: """))
        while otroAsiento != 1 and otroAsiento != 2 and otroAsiento != -1:
            print("Opción no válida")
            otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Sí
2 - No
-1  Salir                                
Ingrese una opción: """))
        while otroAsiento == 1:
            asiento, sala = seleccionarAsiento(sala)
            asientosSeleccionados.append(asiento)
            total_entradas += PRECIO_ENTRADA  # Sumar precio de otra entrada
            otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Sí
2 - No
-1  Salir                                
Ingrese una opción: """))

        # Función lambda para calcular el total
        calcular_total = lambda entradas, snacks, desc: (entradas + snacks) * (1 - desc)
        calcular_total_sin_descuento = lambda entradas, snacks: entradas + snacks

        # Calcular total
        if descuento > 0:
            total_a_pagar = calcular_total(total_entradas, total_snacks, descuento)
            print(f"Total con descuento aplicado: ${total_a_pagar:.2f}")
        else:
            total_a_pagar = calcular_total_sin_descuento(total_entradas, total_snacks)
            print(f"Total sin descuento: ${total_a_pagar:.2f}")

        # Imprimir ticket con el desglose de costos
        imprimirTicket(pelicula, asientosSeleccionados, snacksSeleccionados, total_entradas, total_snacks, total_a_pagar, recaudacion)

        if otroAsiento == 2:
            print("""
                Por favor, retire su entrada y deje pasar al siguiente usuario.
                                ¡Disfrute su película!""")
            flagContinue = True

if __name__ == "__main__":
    while True:
        main()
