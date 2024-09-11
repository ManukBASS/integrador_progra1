from users import loginUsuarios
from snacks import seleccionarSnack
from peliculas import seleccionarPelicula
from asientos import seleccionarAsiento
from reportes import imprimirTicket, generarReporte

def main():
    PRECIO_ENTRADA = 4000
    flagContinue = True

    while flagContinue:
        recaudacionDelDia = []
        descuento = loginUsuarios()
        pelicula, sala = seleccionarPelicula()

        # Snacks Ticket
        snacksSeleccionados = []
        snack_elegido = seleccionarSnack()
        snacksSeleccionados.append(snack_elegido)
        total_snacks = snack_elegido[1]

        # Asientos Ticket
        asientosSeleccionados = []
        asiento, sala = seleccionarAsiento(sala)
        asientosSeleccionados.append(asiento)
        total_entradas = PRECIO_ENTRADA
        
        otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Si
2 - No
-1  Salir y Generar Reporte                         
Ingrese una opción: """))
        while otroAsiento != 1 and otroAsiento != 2 and otroAsiento != -1:
            print("Opción no válida")
            otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Si
2 - No
-1  Salir y Generar Reporte                       
Ingrese una opción: """))
        while otroAsiento == 1:
            asiento, sala = seleccionarAsiento(sala)
            asientosSeleccionados.append(asiento)
            otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Si
2 - No
-1  Salir y Generar Reporte
Ingrese una opción: """))

        calcular_total = lambda entradas, snacks, desc: (entradas + snacks) * (1 - desc)
        calcular_total_sin_descuento = lambda entradas, snacks: entradas + snacks

        if descuento > 0:
            total_a_pagar = calcular_total(total_entradas, total_snacks, descuento)
            print(f"Total con descuento aplicado: ${total_a_pagar:.2f}")
        else:
            total_a_pagar = calcular_total_sin_descuento(total_entradas, total_snacks)
            print(f"Total sin descuento: ${total_a_pagar:.2f}")
        imprimirTicket(pelicula, asientosSeleccionados, snacksSeleccionados, total_entradas, total_snacks, total_a_pagar, recaudacionDelDia)

        if otroAsiento == 2:
            print("""
                Por favor, retire su entrada y deje pasar al siguiente usuario
                ¡Disfrute su pelicula!""")
            flagContinue = True
        if otroAsiento == -1:
            contraAdmin = "admin123"
            admin = input("Ingrese la contraseña: ")
            while admin != contraAdmin:
                admin = input("Contraseña incorrecta. Intente otra vez: ")
            generarReporte(total_a_pagar, recaudacionDelDia)
            flagContinue = False

if __name__ == "__main__":
    main()
