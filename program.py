"""Falta: 
- Slicing
- Funcion Lambda
- Tickets 
- Reportes (Recaudación, Pelicula más vista, etc..)
- Aplicar descuentos 
- Checkeo de sala 
- Compra múltiples entradas
- Cancelar compra
- Salas
"""

import random
from users import loginUsuarios
from snacks import seleccionarSnack
from peliculas import seleccionarPelicula
from asientos import seleccionarAsiento
from reportes import generarReporte

def main():
    asientos = [["🟢" for _ in range(6)] for _ in range(4)]
    loginUsuarios()
    seleccionarPelicula()
    seleccionarSnack()
    seleccionarAsiento(asientos)
    seleccionarAsiento(asientos)
    seleccionarAsiento(asientos)

if __name__ == "__main__":
    main()
