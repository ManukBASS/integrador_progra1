"""Falta: 
- Slicing
- Funcion Lambda
- Asiento Random 
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
from snacks import selecionarSnack
from peliculas import seleccionarPelicula
from asientos import seleccionarAsiento

def main():
    asientos = [["🟢" for _ in range(6)] for _ in range(4)]
    loginUsuarios()
    seleccionarPelicula()
    selecionarSnack()
    seleccionarAsiento(asientos)
    seleccionarAsiento(asientos)

if __name__ == "__main__":
    main()
