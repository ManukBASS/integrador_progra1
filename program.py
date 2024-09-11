from users import loginUsuarios
from snacks import seleccionarSnack
from peliculas import seleccionarPelicula
from asientos import seleccionarAsiento
from reportes import imprimirTicket, generarReporte

def main():
    PRECIO_ENTRADA = 4000
    flagContinue = True

    recaudacionDelDia = []
    peliculas_vendidas = [0, 0, 0]
    snacks_vendidos = [0, 0, 0, 0]
    total_usuarios = 0
    usuarios_registrados = 0

    while flagContinue:
        descuento, esAdmin = loginUsuarios()
        
        if esAdmin:
            generarReporte(recaudacionDelDia, peliculas_vendidas, snacks_vendidos, usuarios_registrados, total_usuarios)
            flagContinue = False
            return
        
        total_usuarios += 1
        if descuento > 0:
            usuarios_registrados += 1

        pelicula, sala = seleccionarPelicula()
        peliculas_vendidas[pelicula[0] - 1] += 1

        # Snacks Ticket
        snacksSeleccionados = []
        snack_opcion, snack_nombre, snack_precio = seleccionarSnack()
        snacksSeleccionados.append((snack_nombre, snack_precio))
        total_snacks = snack_precio
        snacks_vendidos[snack_opcion - 1] += 1


        # Asientos Ticket
        asientosSeleccionados = []
        asiento, sala = seleccionarAsiento(sala)
        asientosSeleccionados.append(asiento)
        total_entradas = PRECIO_ENTRADA
        
        otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Si
2 - No                        
Ingrese una opción: """))
        while otroAsiento != 1 and otroAsiento != 2 and otroAsiento != -1:
            print("Opción no válida")
            otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Si
2 - No                     
Ingrese una opción: """))

        while otroAsiento == 1:
            asiento, sala = seleccionarAsiento(sala)
            asientosSeleccionados.append(asiento)
            total_entradas += PRECIO_ENTRADA
            otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Si
2 - No
Ingrese una opción: """))

        calcular_total = lambda entradas, snacks, desc: (entradas + snacks) * (1 - desc)
        calcular_total_sin_descuento = lambda entradas, snacks: entradas + snacks

        if descuento > 0:
            total_a_pagar = calcular_total(total_entradas, total_snacks, descuento)
            print(f"Total con descuento aplicado: ${total_a_pagar:.2f}")
        else:
            total_a_pagar = calcular_total_sin_descuento(total_entradas, total_snacks)
            print(f"Total sin descuento: ${total_a_pagar:.2f}")

        recaudacionDelDia.append(total_a_pagar)
        imprimirTicket(pelicula, asientosSeleccionados, snacksSeleccionados, total_entradas, total_snacks, total_a_pagar, recaudacionDelDia)

        if otroAsiento == 2:
            print("""
                Por favor, retire su entrada y deje pasar al siguiente usuario
                ¡Disfrute su pelicula!""")
            flagContinue = True

if __name__ == "__main__":
    main()
