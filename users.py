# usuarios_registrados = ["manuzarraga99", "milinunes99", "micaflores96"]
# descuentos = 0.15

# def loginUsuarios():
#     preguntaInicial = int(input("""
# ¡Bienvenido! ¿Está registrado en nuestro cine? 
# 1 - Si
# 2 - No
# 3 - Deseo crear un usuario
# Ingrese una opción: """))
#     while preguntaInicial != 1  and preguntaInicial != 2 and preguntaInicial != 3:
#         preguntaInicial = int(input("""
# Opción incorrecta, por favor elija una de las siguientes: 
# 1 - Si
# 2 - No
# 3 - Deseo crear un usuario
# Ingrese una opción: """))
#     if preguntaInicial == 1:
#         user = input("Ingrese su nombre de usuario: ")
#         while user not in usuarios_registrados:
#             user = input("Usuario inexistente, ingrese su nombre de usuario: ")
#         print(f"¡Bienvenido {user.capitalize()}! Tienes un descuento de {descuentos*100}%")
#         return descuentos
#     if preguntaInicial == 2:
#         print("Usuario no registrado, no hay descuento :(")
#         return 0
#     if preguntaInicial == 3:
#         user = input("Cree su nombre de usuario, debe tener minimo 8 caracteres y al menos un número: ")
#         flagAlnum = user.isalpha()
#         while flagAlnum or len(user) < 8:
#             user = input("El nombre debe tener minimo 8 caracteres y al menos un número: ")
#             flagAlnum = user.isalpha()
#         usuarios_registrados.append(user)
#         print(usuarios_registrados)
#         return descuentos
#------------------------------------------------

from reportes import generarReporte

usuarios_registrados = ["manuzarraga99", "milinunes99", "micaflores96"]
descuentos = 0.15

def loginUsuarios(reportes):
    preguntaInicial = int(input("""
¡Bienvenido! ¿Está registrado en nuestro cine? 
1 - Si
2 - No
3 - Deseo crear un usuario
-1 - Generar reporte
Ingrese una opción: """))
    while preguntaInicial != 1  and preguntaInicial != 2 and preguntaInicial != 3 and preguntaInicial != -1:
        preguntaInicial = int(input("""
Opción incorrecta, por favor elija una de las siguientes: 
1 - Si
2 - No
3 - Deseo crear un usuario
-1 - Generar reporte
Ingrese una opción: """))
    if preguntaInicial == 1:
        user = input("Ingrese su nombre de usuario: ")
        while user not in usuarios_registrados:
            user = input("Usuario inexistente, ingrese su nombre de usuario: ")
        print(f"¡Bienvenido {user.capitalize()}! Tienes un descuento de {descuentos*100}%")
        return descuentos
    if preguntaInicial == 2:
        print("Usuario no registrado, no hay descuento :(")
        return 0
    if preguntaInicial == 3:
        user = input("Cree su nombre de usuario, debe tener minimo 8 caracteres y al menos un número: ")
        flagAlnum = user.isalpha()
        while flagAlnum or len(user) < 8:
            user = input("El nombre debe tener minimo 8 caracteres y al menos un número: ")
            flagAlnum = user.isalpha()
        usuarios_registrados.append(user)
        print(usuarios_registrados)
        return descuentos
    #---------------------------------
    if preguntaInicial == -1:
        clave_admin = input("Ingrese clave de administrador: ")
        while clave_admin != "admin123":
            clave_admin = input("Clave incorrecta. Ingrese clave de administrador: ")
            
        generarReporte(reportes)


