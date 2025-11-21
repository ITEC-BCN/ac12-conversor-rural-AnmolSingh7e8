
MOVE_SPEED_X = 100
MOVE_SPEED_Y = 100
MAX_VISIBLE = 3

GALLINA_LENA = 6
CABRA_LENA = 5
CABALLO_LENA = 12
HUEVOS_LENA = 3
PATATA_FACTOR = 2 / 1.5

MENU_PRINCIPAL = ["Gallinas", "Patatas", "Cabras", "Huevos", "Caballos", "Tabla de precios", "Salir"]
MENU_TRONCOS = ["Gallinas a troncos", "Patatas a troncos", "Cabras a troncos", "Huevos a troncos", "Caballos a troncos", "Salir"]
MENU_INVERSO = ["Troncos a Gallinas", "Troncos a Patatas", "Troncos a Cabras", "Troncos a Huevos", "Troncos a Caballos", "Salir"]

menu_index = 0
menu_index_troncos = 0
menu_index_inverso = 0
menu_abierto = False
menu_abierto_troncos = False
menu_abierto_inverso = False

a_prev = False
up_prev = False
down_prev = False

mensaje_npc_mostrado = False
mensaje_npc2_mostrado = False


def round2(x: number):
    return Math.idiv(x * 100 + 0.5, 1) / 100

def convertir_a_troncos(producto: str):
    cantidad = game.ask_for_number("Cuantos " + producto + "?", 2)
    if producto == "Gallinas":
        troncos = round2(cantidad * GALLINA_LENA)
    elif producto == "Cabras":
        troncos = round2(cantidad * CABRA_LENA)
    elif producto == "Caballos":
        troncos = round2(cantidad * CABALLO_LENA)
    elif producto == "Huevos":
        troncos = round2(cantidad / 12 * HUEVOS_LENA)
    elif producto == "Patatas":
        troncos = round2(cantidad * PATATA_FACTOR)
    else:
        troncos = 0
    game.splash("" + str(cantidad) + " " + producto + " = " + str(troncos) + " troncos")

def convertir_troncos_a(producto: str):
    troncos = game.ask_for_number("Cuantos troncos tienes?", 2)
    if producto == "Gallinas":
        cantidad = Math.idiv(troncos, GALLINA_LENA)
    elif producto == "Cabras":
        cantidad = Math.idiv(troncos, CABRA_LENA)
    elif producto == "Caballos":
        cantidad = Math.idiv(troncos, CABALLO_LENA)
    elif producto == "Huevos":
        cantidad = Math.idiv(troncos * 12, HUEVOS_LENA)
    elif producto == "Patatas":
        cantidad = Math.idiv(troncos, PATATA_FACTOR)
    else:
        cantidad = 0
    game.splash("" + str(troncos) + " troncos = " + str(cantidad) + " " + producto)

def seleccionar_opcion(menu: List[str], index: number):
    opcion = menu[index]
    if opcion[0:10] == "Troncos a ":
        producto = opcion[10:]
        convertir_troncos_a(producto)
    elif opcion[-10:] == "a troncos":
        opcion_len = 0
        i = 0
        while i < len(opcion):
            opcion_len += 1
            i += 1
        producto = opcion[0:opcion_len-10]
        convertir_a_troncos(producto)
    elif opcion == "Salir":
        game.splash("Hasta pronto!")
        game.over(False)
    elif opcion == "Tabla de precios":
        game.show_long_text("""1 Gallina = 6 kg leña
1.5 kg Patatas = 2 kg leña
1 Cabra = 5 kg leña
12 Huevos = 3 kg leña
1 Caballo = 12 kg leña""", DialogLayout.TOP)
    else:
        convertir_a_troncos(opcion)

def mostrar_menu_scroll(menu: List[str], index: number):
    texto = ""
    menu_len = 0
    i = 0
    while i < len(menu):
        menu_len += 1
        i += 1
    start_index = index - index % MAX_VISIBLE
    if start_index < 0:
        start_index = 0
    end_index = start_index + MAX_VISIBLE
    if end_index > menu_len:
        end_index = menu_len
    i = start_index
    while i < end_index:
        if i == index:
            texto += "> " + menu[i] + "\n"
        else:
            texto += "  " + menu[i] + "\n"
        i += 1
    game.show_long_text(texto, DialogLayout.TOP)


def game_loop():
    global a_prev, up_prev, down_prev
    global menu_index, menu_index_troncos, menu_index_inverso
    global menu_abierto, menu_abierto_troncos, menu_abierto_inverso
    global mensaje_npc_mostrado, mensaje_npc2_mostrado

    a_now = controller.A.is_pressed()
    up_now = controller.up.is_pressed()
    down_now = controller.down.is_pressed()

    if jugador.overlaps_with(npc) and not menu_abierto:
        if not mensaje_npc_mostrado:
            npc.say_text("Pulsa A para abrir el conversor", 500, False)
            mensaje_npc_mostrado = True
    else:
        mensaje_npc_mostrado = False

    if jugador.overlaps_with(npc2) and not menu_abierto_inverso:
        if not mensaje_npc2_mostrado:
            npc2.say_text("Pulsa A para convertir troncos a productos", 500, False)
            mensaje_npc2_mostrado = True
    else:
        mensaje_npc2_mostrado = False

    if a_now and not a_prev:
        if menu_abierto:
            seleccionar_opcion(MENU_PRINCIPAL, menu_index)
            menu_abierto = False
            controller.move_sprite(jugador, MOVE_SPEED_X, MOVE_SPEED_Y)
        elif menu_abierto_troncos:
            seleccionar_opcion(MENU_TRONCOS, menu_index_troncos)
            menu_abierto_troncos = False
            controller.move_sprite(jugador, MOVE_SPEED_X, MOVE_SPEED_Y)
        elif menu_abierto_inverso:
            seleccionar_opcion(MENU_INVERSO, menu_index_inverso)
            menu_abierto_inverso = False
            controller.move_sprite(jugador, MOVE_SPEED_X, MOVE_SPEED_Y)
        elif jugador.overlaps_with(npc):
            menu_abierto = True
            menu_index = 0
            controller.move_sprite(jugador, 0, 0)
            mostrar_menu_scroll(MENU_PRINCIPAL, menu_index)
        elif jugador.overlaps_with(npc2):
            menu_abierto_inverso = True
            menu_index_inverso = 0
            controller.move_sprite(jugador, 0, 0)
            
            mostrar_menu_scroll(MENU_INVERSO, menu_index_inverso)

    if menu_abierto:
        if up_now and not up_prev:
            menu_index = (menu_index - 1 + len(MENU_PRINCIPAL)) % len(MENU_PRINCIPAL)
            mostrar_menu_scroll(MENU_PRINCIPAL, menu_index)
        if down_now and not down_prev:
            menu_index = (menu_index + 1) % len(MENU_PRINCIPAL)
            mostrar_menu_scroll(MENU_PRINCIPAL, menu_index)

    if menu_abierto_troncos:
        if up_now and not up_prev:
            menu_index_troncos = (menu_index_troncos - 1 + len(MENU_TRONCOS)) % len(MENU_TRONCOS)
            mostrar_menu_scroll(MENU_TRONCOS, menu_index_troncos)
        if down_now and not down_prev:
            menu_index_troncos = (menu_index_troncos + 1) % len(MENU_TRONCOS)
            mostrar_menu_scroll(MENU_TRONCOS, menu_index_troncos)

    if menu_abierto_inverso:
        if up_now and not up_prev:
            menu_index_inverso = (menu_index_inverso - 1 + len(MENU_INVERSO)) % len(MENU_INVERSO)
            mostrar_menu_scroll(MENU_INVERSO, menu_index_inverso)
        if down_now and not down_prev:
            menu_index_inverso = (menu_index_inverso + 1) % len(MENU_INVERSO)
            mostrar_menu_scroll(MENU_INVERSO, menu_index_inverso)

    a_prev = a_now
    up_prev = up_now
    down_prev = down_now


def menu_inicio():
    game.show_long_text("¡Bienvenido al juego de conversión de productos y troncos!", DialogLayout.CENTER)
    scene.set_background_image(assets.image("""myImage"""))
    while True:
        game.show_long_text("1-Jugar\n2-Instructions\n3-Salir", DialogLayout.CENTER)
        opcion = game.ask_for_number("Elige 1-3", 1)
        if opcion == 1:
            break
        elif opcion == 2:
            game.show_long_text("Convierte productos <-> leña/troncos. Acerca al NPC y pulsa A.", DialogLayout.TOP)
        elif opcion == 3:
            game.splash("Adiós", "Hasta la próxima")
            game.over(False)
        else:
            game.show_long_text("Opción no válida", DialogLayout.TOP)

menu_inicio()

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
"""), SpriteKind.player)
jugador.set_stay_in_screen(True)

npc = sprites.create(assets.image("""vill"""), SpriteKind.enemy)
npc.set_position(44, 97)

npc2 = sprites.create(assets.image("""vill0"""), SpriteKind.enemy)
npc2.set_position(120, 80)

controller.move_sprite(jugador, MOVE_SPEED_X, MOVE_SPEED_Y)

scene.set_background_image(assets.image("""myImage"""))

def on_forever():
    game_loop()
forever(on_forever)
