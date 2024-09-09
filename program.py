"""Falta: 
- Slicing
- Funcion Lambda
- Reportes (Recaudación, Pelicula más vista, etc..)
- Aplicar descuentos
- Validar asientos
"""

from users import loginUsuarios
from snacks import seleccionarSnack
from peliculas import seleccionarPelicula
from asientos import seleccionarAsiento
from reportes import generarReporte, imprimirTicket

def main():
    flagContinue = True

    while flagContinue:
        loginUsuarios()
        pelicula, sala = seleccionarPelicula()

        # Snacks
        snacksSeleccionados = []
        snack_elegido = seleccionarSnack()
        snacksSeleccionados.append(snack_elegido)

        # Asientos
        asientosSeleccionados = []
        asiento, sala = seleccionarAsiento(sala)
        asientosSeleccionados.append(asiento)
        
        otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Si
2 - No
-1  Salir                                
Ingrese una opción: """))
        while otroAsiento != 1 and otroAsiento != 2 and otroAsiento != -1:
            print("Opción no válida")
            otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Si
2 - No
-1  Salir                                
Ingrese una opción: """))
        while otroAsiento == 1:
            asiento, sala = seleccionarAsiento(sala)
            asientosSeleccionados.append(asiento)
            otroAsiento = int(input("""
¿Desea elegir otro asiento? 
1 - Si
2 - No
-1  Salir
Ingrese una opción: """))
            
        if otroAsiento == 2:
            print("""
                Por favor, retire su entrada y deje pasar al siguiente usuario
                ¡Disfrute su pelicula!""")
            imprimirTicket(pelicula, asientosSeleccionados, snacksSeleccionados)
            flagContinue = True
        if otroAsiento == -1:
            flagContinue = False

if __name__ == "__main__":
    main()
