usuarios_registrados = ["manuzarraga99", "milinunes99", "micaflores96"]

def loginUsuarios(usuarios):
    descuentos = 0.15
    preguntaInicial = int(input("""¡Bienvenido! ¿Está registrado en nuestro cine? 
1 - Si
2 - No
3 - Deseo crear un usuario
-1 - Generar reporte
Ingrese una opción: """))
    
    while preguntaInicial not in [1, 2, 3, -1]:
        preguntaInicial = int(input("""Opción incorrecta, por favor elija una de las siguientes: 
1 - Si
2 - No
3 - Deseo crear un usuario
-1 - Generar reporte
Ingrese una opción: """))

    if preguntaInicial == 1:
        user = input("Ingrese su nombre de usuario: ")
        while user not in usuarios:
            user = input("Usuario inexistente, ingrese su nombre de usuario: ")
        print(f"¡Bienvenido {user.capitalize()}! Tienes un descuento de {descuentos*100}%")
        return descuentos
    elif preguntaInicial == 2:
        print("Usuario no registrado, no hay descuento :(")
        return 0
    elif preguntaInicial == 3:
        user = input("Cree su nombre de usuario, debe tener mínimo 8 caracteres y al menos un número: ")
        flagAlnum = user.isalpha()
        while flagAlnum or len(user) < 8:
            user = input("El nombre debe tener mínimo 8 caracteres y al menos un número: ")
            flagAlnum = user.isalpha()
        usuarios.append(user)
        print(usuarios)
        return descuentos
    elif preguntaInicial == -1:
        clave_admin = input("Ingrese clave de administrador: ")
        while clave_admin != "admin123":
            clave_admin = input("Clave incorrecta. Ingrese clave de administrador: ")
        
        return 'reporte'

