
from users import loginUsuarios, usuarios_registrados
from snacks import seleccionarSnack
from peliculas import seleccionarPelicula
from asientos import seleccionarAsiento
from reportes import generarReporte, imprimirTicket

def main():
    PRECIO_ENTRADA = 4000
    recaudacion = []  
    usuarios = usuarios_registrados.copy() 
    
    while True:
        descuento = loginUsuarios(usuarios)  
        
        if descuento == 'reporte':
            generarReporte(recaudacion)  
            recaudacion.clear()  
            print("Excelente recaudación! Nos vemos mañana :)")
            return
        
        pelicula, sala, horario = seleccionarPelicula()

        snacksSeleccionados = []
        snack_elegido = seleccionarSnack()
        snacksSeleccionados.append(snack_elegido)

        asientosSeleccionados = []
        asiento, sala = seleccionarAsiento(sala)
        asientosSeleccionados.append(asiento)
        
        otroAsiento = int(input("""¿Desea elegir otro asiento? 
1 - Si
2 - No
-1  Salir                                 
Ingrese una opción: """))
        
        while otroAsiento == 1:
            asiento, sala = seleccionarAsiento(sala)
            asientosSeleccionados.append(asiento)
            otroAsiento = int(input("""¿Desea elegir otro asiento? 
1 - Si
2 - No
-1  Salir                                 
Ingrese una opción: """))
        
        if otroAsiento == 2:
            print("""Por favor, retire su entrada y deje pasar al siguiente usuario
¡Disfrute su película!""")
            total_snacks = sum(snack[1] for snack in snacksSeleccionados)  
            total_entradas = PRECIO_ENTRADA * len(asientosSeleccionados)  
            

            calcular_total = lambda entradas, snacks, desc: (entradas + snacks) * (1 - desc)
            calcular_total_sin_descuento = lambda entradas, snacks: entradas + snacks
            
            if descuento > 0:
                total_a_pagar = calcular_total(total_entradas, total_snacks, descuento)
                print(f"Total con descuento aplicado: ${total_a_pagar:.2f}")
            else:
                total_a_pagar = calcular_total_sin_descuento(total_entradas, total_snacks)
                print(f"Total sin descuento: ${total_a_pagar:.2f}")
            

            imprimirTicket(pelicula, asientosSeleccionados, snacksSeleccionados, total_entradas, total_snacks, total_a_pagar, recaudacion, horario)

            recaudacion.append(total_a_pagar)

if __name__ == "__main__":
    main()

