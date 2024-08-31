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

def main():
    loginUsuarios()
    seleccionarPelicula()
    selecionarSnack()

if __name__ == "__main__":
    main()
