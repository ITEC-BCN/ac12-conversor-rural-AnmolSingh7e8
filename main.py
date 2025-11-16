def menu():
    opcio_usuari = game.ask_for_number("1: Gallina\n2: Patata\n3: Cabra", 1)
    if opcio_usuari >= 3 and opcio_usuari <6:
        opcio_usuari = game.ask_for_number("4: Huevos\n5: Caballo\n6: Salir\n7", 4)
    elif opcio_usuari > 6:
        opcio_usuari = game.ask_for_number("Salir", 7)
    return opcio_usuari

def procesar_opcio(opcio: int):
    if opcio == 1:
        game.show_long_text("Has elegido: Gallina", DialogLayout.TOP)
    elif opcio == 2:
        game.show_long_text("Has elegido: Patata", DialogLayout.TOP)
    elif opcio == 3:
        game.show_long_text("Has elegido: Cabra", DialogLayout.TOP)
    elif opcio == 4:
        game.show_long_text("Has elegido: Huevos", DialogLayout.TOP)
    elif opcio == 5:
        game.show_long_text("Has elegido: Caballo", DialogLayout.TOP)
    elif opcio == 6:
        game.show_long_text("Saliendo...", DialogLayout.TOP)
        game.over(False)
        return
    else:
        game.show_long_text("Opción no válida", DialogLayout.BOTTOM)
        procesar_opcio(menu())

procesar_opcio(menu())