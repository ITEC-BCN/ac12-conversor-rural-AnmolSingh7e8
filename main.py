cantidad = 0
cantidad2 = 0
cantidad3 = 0
cantidad4 = 0
cantidad5 = 0
opcion2 = 0
texto = ""
menu_index = 0
menu_abierto = False
npc: Sprite = None
jugador: Sprite = None
CABALLO_LENA = 12
HUEVOS_LENA = 3
CABRA_LENA = 5
PATATA_LENA = 2
GALLINA_LENA = 6
MAX_VISIBLE = 3
cursor_sprite: Sprite = None
menu_options = ["Gallinas","Patatas","Cabras","Huevos","Caballos","Tabla de precios","Salir"]

jugador = sprites.create(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f f e 2 2 2 2 2 2 e e f . .
        . . f e 2 f f f f f f 2 e f . .
        . . f f f f e e e e f f f f . .
        . f f e f b f 4 4 f b f e f f .
        . f e e 4 1 f d d f 1 4 e e f .
        . . f f f f d d d d d e e f . .
        . f d d d d f 4 4 4 e e f . . .
        . f b b b b f 2 2 2 2 f 4 e . .
        . f b b b b f 2 2 2 2 f d 4 . .
        . . f c c f 4 5 5 4 4 f 4 4 . .
        . . . f f f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """), SpriteKind.player)
npc = sprites.create(assets.image("""
    npc
    """), SpriteKind.enemy)
jugador.set_stay_in_screen(True)
controller.move_sprite(jugador, 100, 100)
scene.set_background_image(img("""
    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
"""))

def crear_menu():
    global menu_abierto, menu_index
    menu_abierto = True
    menu_index = 0
    controller.move_sprite(jugador, 0, 0)
    mostrar_menu_scroll()

def mostrar_menu_scroll():
    global texto
    texto = ""
    start_index = menu_index - (menu_index % MAX_VISIBLE)
    end_index = min(start_index + MAX_VISIBLE, len(menu_options))
    for i in range(start_index, end_index):
        if i == menu_index:
            texto += "> " + menu_options[i] + "\n"
        else:
            texto += "  " + menu_options[i] + "\n"
    game.show_long_text(texto, DialogLayout.BOTTOM)

def actualizar_cursor():
    mostrar_menu_scroll()

def cerrar_menu():
    global menu_abierto
    menu_abierto = False
    controller.move_sprite(jugador, 100, 100)

def seleccionar_opcion():
    global opcion2
    opcion2 = menu_index
    if opcion2 == 0:
        procesar_gallinas()
    elif opcion2 == 1:
        procesar_patatas()
    elif opcion2 == 2:
        procesar_cabras()
    elif opcion2 == 3:
        procesar_huevos()
    elif opcion2 == 4:
        procesar_caballos()
    elif opcion2 == 5:
        mostrar_tabla_precios()
    elif opcion2 == 6:
        cerrar_menu()
        game.splash("Hasta pronto!", "Gracias por venir al mercado")
        return
    cerrar_menu()

def procesar_gallinas():
    global cantidad
    cantidad = game.ask_for_number("Cuantas gallinas?", 1)
    if cantidad > 0:
        game.splash("" + str(cantidad) + " gallinas = " + str(cantidad * GALLINA_LENA) + " kg de leña")

def procesar_patatas():
    global cantidad2
    cantidad2 = game.ask_for_number("Cuantos kg de patatas?", 1)
    if cantidad2 > 0:
        game.splash("" + str(cantidad2) + " kg patatas = " + str(cantidad2 / 1.5 * PATATA_LENA) + " kg de leña")

def procesar_cabras():
    global cantidad3
    cantidad3 = game.ask_for_number("Cuantas cabras?", 1)
    if cantidad3 > 0:
        game.splash("" + str(cantidad3) + " cabras = " + str(cantidad3 * CABRA_LENA) + " kg de leña")

def procesar_huevos():
    global cantidad4
    cantidad4 = game.ask_for_number("Cuantos huevos?", 1)
    if cantidad4 > 0:
        game.splash("" + str(cantidad4) + " huevos = " + str(cantidad4 / 12 * HUEVOS_LENA) + " kg de leña")

def procesar_caballos():
    global cantidad5
    cantidad5 = game.ask_for_number("Cuantos caballos?", 1)
    if cantidad5 > 0:
        game.splash("" + str(cantidad5) + " caballos = " + str(cantidad5 * CABALLO_LENA) + " kg de leña")

def mostrar_tabla_precios():
    texto2 = "TABLA DE PRECIOS\n"
    texto2 += "1 Gallina = 6 kg lena\n1.5 kg Patatas = 2 kg lena\n1 Cabra = 5 kg lena\n12 Huevos = 3 kg lena\n1 Caballo = 12 kg lena"
    game.show_long_text(texto2, DialogLayout.CENTER)

def on_up_pressed():
    global menu_index
    if menu_abierto:
        menu_index = (menu_index - 1) % len(menu_options)
        actualizar_cursor()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_down_pressed():
    global menu_index
    if menu_abierto:
        menu_index = (menu_index + 1) % len(menu_options)
        actualizar_cursor()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_a_pressed():
    if menu_abierto:
        seleccionar_opcion()
    elif jugador.overlaps_with(npc):
        crear_menu()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_forever():
    if jugador.overlaps_with(npc) and not menu_abierto:
        npc.say_text("Pulsa A para abrir el conversor", 500, False)
    else:
        npc.say_text("", 0, False)
forever(on_forever)
