# --- Variables globales ---
opcio_usuari = 0
current_product = ""
current_value = 0
step = 0
conversion_factor = 0
result_kg = 0
conversion_direction = "A->B"  # Producto -> leña

# --- Función de menú ---
def menu():
    global opcio_usuari
    opcio_usuari = game.ask_for_number("""1: Gallina
2: Patata
3: Cabra
4: Huevos
5: Caballo
6: Salir""", 1)
    return opcio_usuari

# --- Selector de cantidad ---
def input_cantidad():
    global current_value, step, current_product
    # Inicializar cantidad y step según producto
    if current_product in ["Gallina", "Cabra", "Caballo", "Huevos"]:
        current_value = 1
        step = 1
    elif current_product == "Patata":
        current_value = 0.5
        step = 0.1

    # Preguntar al usuario la cantidad
    current_value = game.ask_for_number(
        "Introduce cantidad de " + current_product + ":", current_value
    )

    calcular_conversion()  # Ir a cálculo

# --- Calcular conversión ---
def calcular_conversion():
    global result_kg
    # Asignar factor según producto
    if current_product == "Gallina":
        conversion_factor = 6
    elif current_product == "Cabra":
        conversion_factor = 5
    elif current_product == "Caballo":
        conversion_factor = 12
    elif current_product == "Huevos":
        conversion_factor = 0.25
    elif current_product == "Patata":
        conversion_factor = 2/1.5
    else:
        conversion_factor = 0

    # Validaciones
    if current_value <= 0:
        game.show_long_text("Introduce un valor mayor que 0", DialogLayout.BOTTOM)
        input_cantidad()
        return

    if current_product in ["Gallina", "Cabra", "Caballo"] and current_value % 1 != 0:
        game.show_long_text("Animales deben ser enteros", DialogLayout.BOTTOM)
        input_cantidad()
        return

    # Cálculo
    redondeado = int(result_kg * 100) / 100
    mostrar_resultado()

# --- Mostrar resultado ---
def mostrar_resultado():
    redondeado = int(result_kg * 100) / 100

    texto = str(current_value) + " " + current_product + " → " + str(redondeado) + " kg leña"
    game.show_long_text(texto, DialogLayout.TOP)
    # Volver al menú después del resultado
    procesar_opcio(menu())

# --- Procesar opción del menú ---
def procesar_opcio(opcio: number):
    global current_product
    if opcio == 1:
        current_product = "Gallina"
        game.show_long_text("Has elegido: Gallina", DialogLayout.TOP)
        input_cantidad()
    elif opcio == 2:
        current_product = "Patata"
        game.show_long_text("Has elegido: Patata", DialogLayout.TOP)
        input_cantidad()
    elif opcio == 3:
        current_product = "Cabra"
        game.show_long_text("Has elegido: Cabra", DialogLayout.TOP)
        input_cantidad()
    elif opcio == 4:
        current_product = "Huevos"
        game.show_long_text("Has elegido: Huevos", DialogLayout.TOP)
        input_cantidad()
    elif opcio == 5:
        current_product = "Caballo"
        game.show_long_text("Has elegido: Caballo", DialogLayout.TOP)
        input_cantidad()
    elif opcio == 6:
        game.show_long_text("Saliendo...", DialogLayout.TOP)
        game.over(False)
    else:
        game.show_long_text("Opción no válida", DialogLayout.BOTTOM)
        procesar_opcio(menu())

# --- MAIN ---
procesar_opcio(menu())
