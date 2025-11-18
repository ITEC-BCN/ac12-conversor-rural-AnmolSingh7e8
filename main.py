# --- VARIABLES ---
current_product = ""
current_value = 0
factor = 0
result = 0
talking = True

productos = {
    1: "Gallina",
    2: "Patata",
    3: "Cabra",
    4: "Huevos",
    5: "Caballo",
    6: "Salir"
}

factores = {
    "Gallina": 6,
    "Patata": 2 / 1.5,
    "Cabra": 5,
    "Huevos": 0.25,
    "Caballo": 12
}

npc = None
npc_trigger = None
player2: Sprite = None


# --- OVERLAP ---
def on_overlap(player2, trigger):
    player2.say_text("Pulsa A", 500)

sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap)


# --- BOTÓN A ---
def on_a_pressed():
    global player2
    for spr in sprites.all_of_kind(SpriteKind.food):
        if player2.overlaps_with(spr):
            abrir_menu()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)


# --- CREAR NPC + TRIGGER ---
def create_npc():
    global npc, npc_trigger
    npc = sprites.create(assets.image("""
        aldeano
    """), SpriteKind.enemy)
    npc.set_position(22, 18)

    npc_trigger = sprites.create(assets.image("""
        myImage0
    """), SpriteKind.food)
    npc_trigger.set_flag(SpriteFlag.INVISIBLE, True)
    npc_trigger.set_position(npc.x, npc.y)


# --- MENÚ ---
def abrir_menu():
    procesar_opcio(menu())
def menu():
    return game.ask_for_number("""
            1 Gallina
            2 Patata
            3 Cabra
            4 Huevos
            5 Caballo
            6 Salir
            """,
        1)


def procesar_opcio(opcio: number):
    global current_product
    if opcio == 1:
        current_product = "Gallina"
    elif opcio == 2:
        current_product = "Patata"
    elif opcio == 3:
        current_product = "Cabra"
    elif opcio == 4:
        current_product = "Huevos"
    elif opcio == 5:
        current_product = "Caballo"
    elif opcio == 6:
        game.over(False)
        return
    else:
        game.show_long_text("Opción no válida", DialogLayout.BOTTOM)
        abrir_menu()
        return
    input_cantidad()
def calcular_conversion():
    global factor, result
    if current_product == "Gallina":
        factor = 6
    elif current_product == "Patata":
        factor = 2 / 1.5
    elif current_product == "Cabra":
        factor = 5
    elif current_product == "Huevos":
        factor = 0.25
    elif current_product == "Caballo":
        factor = 12
    result = current_value * factor
    game.show_long_text("" + str(result) + " kg de leña", DialogLayout.TOP)
def input_cantidad():
    global current_value
    current_value = game.ask_for_number("Cantidad de " + current_product, 1)
    calcular_conversion()


# --- INICIO ---
create_npc()

player2 = sprites.create(assets.image(""". . . . . . f f f f . . . . . .
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
        . . . . . f f . . f f . . . . ."""), SpriteKind.food)
controller.move_sprite(player2)

scene.set_background_image(img("""
    ....................................
"""))
