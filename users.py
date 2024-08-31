usuarios_registrados = ["manu", "mili", "mica"]
descuentos = 0.15

def loginUsuarios():
    preguntaInicial = int(input("""
¡Bienvenido! ¿Está registrado en nuestro cine? 
1 - Si
2 - No
Ingrese una opción: """))
    while preguntaInicial != 1  and preguntaInicial != 2:
        preguntaInicial = int(input("""
Opción incorrecta, por favor elija una de las siguientes: 
1 - Si
2 - No
Ingrese una opción: """))
    if preguntaInicial == 1:
        user = input("Ingrese su nombre de usuario: ")
        while user not in usuarios_registrados:
            user = input("Usuario inexistente, ingrese su nombre de usuario: ")
        print(f"¡Bienvenido {user}! Tienes un descuento de {descuentos*100}%")
        return descuentos
    if preguntaInicial == 2:
        print("Usuario no registrado, no hay descuento :(")
        return 0
    