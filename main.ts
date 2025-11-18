let cantidad = 0
let cantidad2 = 0
let cantidad3 = 0
let cantidad4 = 0
let cantidad5 = 0
let opcion2 = 0
let texto = ""
let menu_index = 0
let menu_abierto = false
let npc : Sprite = null
let jugador : Sprite = null
let CABALLO_LENA = 12
let HUEVOS_LENA = 3
let CABRA_LENA = 5
let PATATA_LENA = 2
let GALLINA_LENA = 6
let MAX_VISIBLE = 3
let cursor_sprite : Sprite = null
let menu_options = ["Gallinas", "Patatas", "Cabras", "Huevos", "Caballos", "Tabla de precios", "Salir"]
jugador = sprites.create(img`
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
        `, SpriteKind.Player)
npc = sprites.create(assets.image`
    npc
    `, SpriteKind.Enemy)
jugador.setStayInScreen(true)
controller.moveSprite(jugador, 100, 100)
scene.setBackgroundImage(img`
    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
`)
function crear_menu() {
    
    menu_abierto = true
    menu_index = 0
    controller.moveSprite(jugador, 0, 0)
    mostrar_menu_scroll()
}

function mostrar_menu_scroll() {
    
    texto = ""
    let start_index = menu_index - menu_index % MAX_VISIBLE
    let end_index = Math.min(start_index + MAX_VISIBLE, menu_options.length)
    for (let i = start_index; i < end_index; i++) {
        if (i == menu_index) {
            texto += "> " + menu_options[i] + "\n"
        } else {
            texto += "  " + menu_options[i] + "\n"
        }
        
    }
    game.showLongText(texto, DialogLayout.Bottom)
}

function actualizar_cursor() {
    mostrar_menu_scroll()
}

function cerrar_menu() {
    
    menu_abierto = false
    controller.moveSprite(jugador, 100, 100)
}

function seleccionar_opcion() {
    
    opcion2 = menu_index
    if (opcion2 == 0) {
        procesar_gallinas()
    } else if (opcion2 == 1) {
        procesar_patatas()
    } else if (opcion2 == 2) {
        procesar_cabras()
    } else if (opcion2 == 3) {
        procesar_huevos()
    } else if (opcion2 == 4) {
        procesar_caballos()
    } else if (opcion2 == 5) {
        mostrar_tabla_precios()
    } else if (opcion2 == 6) {
        cerrar_menu()
        game.splash("Hasta pronto!", "Gracias por venir al mercado")
        return
    }
    
    cerrar_menu()
}

function procesar_gallinas() {
    
    cantidad = game.askForNumber("Cuantas gallinas?", 1)
    if (cantidad > 0) {
        game.splash("" + ("" + cantidad) + " gallinas = " + ("" + cantidad * GALLINA_LENA) + " kg de leña")
    }
    
}

function procesar_patatas() {
    
    cantidad2 = game.askForNumber("Cuantos kg de patatas?", 1)
    if (cantidad2 > 0) {
        game.splash("" + ("" + cantidad2) + " kg patatas = " + ("" + cantidad2 / 1.5 * PATATA_LENA) + " kg de leña")
    }
    
}

function procesar_cabras() {
    
    cantidad3 = game.askForNumber("Cuantas cabras?", 1)
    if (cantidad3 > 0) {
        game.splash("" + ("" + cantidad3) + " cabras = " + ("" + cantidad3 * CABRA_LENA) + " kg de leña")
    }
    
}

function procesar_huevos() {
    
    cantidad4 = game.askForNumber("Cuantos huevos?", 1)
    if (cantidad4 > 0) {
        game.splash("" + ("" + cantidad4) + " huevos = " + ("" + cantidad4 / 12 * HUEVOS_LENA) + " kg de leña")
    }
    
}

function procesar_caballos() {
    
    cantidad5 = game.askForNumber("Cuantos caballos?", 1)
    if (cantidad5 > 0) {
        game.splash("" + ("" + cantidad5) + " caballos = " + ("" + cantidad5 * CABALLO_LENA) + " kg de leña")
    }
    
}

function mostrar_tabla_precios() {
    let texto2 = "TABLA DE PRECIOS\n"
    texto2 += `1 Gallina = 6 kg lena
1.5 kg Patatas = 2 kg lena
1 Cabra = 5 kg lena
12 Huevos = 3 kg lena
1 Caballo = 12 kg lena`
    game.showLongText(texto2, DialogLayout.Center)
}

controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    
    if (menu_abierto) {
        menu_index = (menu_index - 1) % menu_options.length
        actualizar_cursor()
    }
    
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    
    if (menu_abierto) {
        menu_index = (menu_index + 1) % menu_options.length
        actualizar_cursor()
    }
    
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    if (menu_abierto) {
        seleccionar_opcion()
    } else if (jugador.overlapsWith(npc)) {
        crear_menu()
    }
    
})
forever(function on_forever() {
    if (jugador.overlapsWith(npc) && !menu_abierto) {
        npc.sayText("Pulsa A para abrir el conversor", 500, false)
    } else {
        npc.sayText("", 0, false)
    }
    
})
