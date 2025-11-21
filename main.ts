let MOVE_SPEED_X = 100
let MOVE_SPEED_Y = 100
let MAX_VISIBLE = 3
let GALLINA_LENA = 6
let CABRA_LENA = 5
let CABALLO_LENA = 12
let HUEVOS_LENA = 3
let PATATA_FACTOR = 2 / 1.5
let MENU_PRINCIPAL = ["Gallinas", "Patatas", "Cabras", "Huevos", "Caballos", "Tabla de precios", "Salir"]
let MENU_TRONCOS = ["Gallinas a troncos", "Patatas a troncos", "Cabras a troncos", "Huevos a troncos", "Caballos a troncos", "Salir"]
let MENU_INVERSO = ["Troncos a Gallinas", "Troncos a Patatas", "Troncos a Cabras", "Troncos a Huevos", "Troncos a Caballos", "Salir"]
let menu_index = 0
let menu_index_troncos = 0
let menu_index_inverso = 0
let menu_abierto = false
let menu_abierto_troncos = false
let menu_abierto_inverso = false
let a_prev = false
let up_prev = false
let down_prev = false
let mensaje_npc_mostrado = false
let mensaje_npc2_mostrado = false
function round2(x: number): number {
    return Math.idiv(x * 100 + 0.5, 1) / 100
}

function convertir_a_troncos(producto: string) {
    let troncos: number;
    let cantidad = game.askForNumber("Cuantos " + producto + "?", 2)
    if (producto == "Gallinas") {
        troncos = round2(cantidad * GALLINA_LENA)
    } else if (producto == "Cabras") {
        troncos = round2(cantidad * CABRA_LENA)
    } else if (producto == "Caballos") {
        troncos = round2(cantidad * CABALLO_LENA)
    } else if (producto == "Huevos") {
        troncos = round2(cantidad / 12 * HUEVOS_LENA)
    } else if (producto == "Patatas") {
        troncos = round2(cantidad * PATATA_FACTOR)
    } else {
        troncos = 0
    }
    
    game.splash("" + ("" + cantidad) + " " + producto + " = " + ("" + troncos) + " troncos")
}

function convertir_troncos_a(producto: string) {
    let cantidad: number;
    let troncos = game.askForNumber("Cuantos troncos tienes?", 2)
    if (producto == "Gallinas") {
        cantidad = Math.idiv(troncos, GALLINA_LENA)
    } else if (producto == "Cabras") {
        cantidad = Math.idiv(troncos, CABRA_LENA)
    } else if (producto == "Caballos") {
        cantidad = Math.idiv(troncos, CABALLO_LENA)
    } else if (producto == "Huevos") {
        cantidad = Math.idiv(troncos * 12, HUEVOS_LENA)
    } else if (producto == "Patatas") {
        cantidad = Math.idiv(troncos, PATATA_FACTOR)
    } else {
        cantidad = 0
    }
    
    game.splash("" + ("" + troncos) + " troncos = " + ("" + cantidad) + " " + producto)
}

function seleccionar_opcion(menu: string[], index: number) {
    let producto: string;
    let opcion_len: number;
    let i: number;
    let opcion = menu[index]
    if (opcion.slice(0, 10) == "Troncos a ") {
        producto = opcion.slice(10)
        convertir_troncos_a(producto)
    } else if (opcion.slice(-10) == "a troncos") {
        opcion_len = 0
        i = 0
        while (i < opcion.length) {
            opcion_len += 1
            i += 1
        }
        producto = opcion.slice(0, opcion_len - 10)
        convertir_a_troncos(producto)
    } else if (opcion == "Salir") {
        game.splash("Hasta pronto!")
        game.over(false)
    } else if (opcion == "Tabla de precios") {
        game.showLongText(`1 Gallina = 6 kg leña
1.5 kg Patatas = 2 kg leña
1 Cabra = 5 kg leña
12 Huevos = 3 kg leña
1 Caballo = 12 kg leña`, DialogLayout.Top)
    } else {
        convertir_a_troncos(opcion)
    }
    
}

function mostrar_menu_scroll(menu: string[], index: number) {
    let texto = ""
    let menu_len = 0
    let i = 0
    while (i < menu.length) {
        menu_len += 1
        i += 1
    }
    let start_index = index - index % MAX_VISIBLE
    if (start_index < 0) {
        start_index = 0
    }
    
    let end_index = start_index + MAX_VISIBLE
    if (end_index > menu_len) {
        end_index = menu_len
    }
    
    i = start_index
    while (i < end_index) {
        if (i == index) {
            texto += "> " + menu[i] + "\n"
        } else {
            texto += "  " + menu[i] + "\n"
        }
        
        i += 1
    }
    game.showLongText(texto, DialogLayout.Top)
}

function game_loop() {
    
    
    
    
    let a_now = controller.A.isPressed()
    let up_now = controller.up.isPressed()
    let down_now = controller.down.isPressed()
    if (jugador.overlapsWith(npc) && !menu_abierto) {
        if (!mensaje_npc_mostrado) {
            npc.sayText("Pulsa A para abrir el conversor", 500, false)
            mensaje_npc_mostrado = true
        }
        
    } else {
        mensaje_npc_mostrado = false
    }
    
    if (jugador.overlapsWith(npc2) && !menu_abierto_inverso) {
        if (!mensaje_npc2_mostrado) {
            npc2.sayText("Pulsa A para convertir troncos a productos", 500, false)
            mensaje_npc2_mostrado = true
        }
        
    } else {
        mensaje_npc2_mostrado = false
    }
    
    if (a_now && !a_prev) {
        if (menu_abierto) {
            seleccionar_opcion(MENU_PRINCIPAL, menu_index)
            menu_abierto = false
            controller.moveSprite(jugador, MOVE_SPEED_X, MOVE_SPEED_Y)
        } else if (menu_abierto_troncos) {
            seleccionar_opcion(MENU_TRONCOS, menu_index_troncos)
            menu_abierto_troncos = false
            controller.moveSprite(jugador, MOVE_SPEED_X, MOVE_SPEED_Y)
        } else if (menu_abierto_inverso) {
            seleccionar_opcion(MENU_INVERSO, menu_index_inverso)
            menu_abierto_inverso = false
            controller.moveSprite(jugador, MOVE_SPEED_X, MOVE_SPEED_Y)
        } else if (jugador.overlapsWith(npc)) {
            menu_abierto = true
            menu_index = 0
            controller.moveSprite(jugador, 0, 0)
            mostrar_menu_scroll(MENU_PRINCIPAL, menu_index)
        } else if (jugador.overlapsWith(npc2)) {
            menu_abierto_inverso = true
            menu_index_inverso = 0
            controller.moveSprite(jugador, 0, 0)
            mostrar_menu_scroll(MENU_INVERSO, menu_index_inverso)
        }
        
    }
    
    if (menu_abierto) {
        if (up_now && !up_prev) {
            menu_index = (menu_index - 1 + MENU_PRINCIPAL.length) % MENU_PRINCIPAL.length
            mostrar_menu_scroll(MENU_PRINCIPAL, menu_index)
        }
        
        if (down_now && !down_prev) {
            menu_index = (menu_index + 1) % MENU_PRINCIPAL.length
            mostrar_menu_scroll(MENU_PRINCIPAL, menu_index)
        }
        
    }
    
    if (menu_abierto_troncos) {
        if (up_now && !up_prev) {
            menu_index_troncos = (menu_index_troncos - 1 + MENU_TRONCOS.length) % MENU_TRONCOS.length
            mostrar_menu_scroll(MENU_TRONCOS, menu_index_troncos)
        }
        
        if (down_now && !down_prev) {
            menu_index_troncos = (menu_index_troncos + 1) % MENU_TRONCOS.length
            mostrar_menu_scroll(MENU_TRONCOS, menu_index_troncos)
        }
        
    }
    
    if (menu_abierto_inverso) {
        if (up_now && !up_prev) {
            menu_index_inverso = (menu_index_inverso - 1 + MENU_INVERSO.length) % MENU_INVERSO.length
            mostrar_menu_scroll(MENU_INVERSO, menu_index_inverso)
        }
        
        if (down_now && !down_prev) {
            menu_index_inverso = (menu_index_inverso + 1) % MENU_INVERSO.length
            mostrar_menu_scroll(MENU_INVERSO, menu_index_inverso)
        }
        
    }
    
    a_prev = a_now
    up_prev = up_now
    down_prev = down_now
}

function menu_inicio() {
    let opcion: number;
    game.showLongText("¡Bienvenido al juego de conversión de productos y troncos!", DialogLayout.Center)
    scene.setBackgroundImage(assets.image`myImage`)
    while (true) {
        game.showLongText(`1-Jugar
2-Instructions
3-Salir`, DialogLayout.Center)
        opcion = game.askForNumber("Elige 1-3", 1)
        if (opcion == 1) {
            break
        } else if (opcion == 2) {
            game.showLongText("Convierte productos <-> leña/troncos. Acerca al NPC y pulsa A.", DialogLayout.Top)
        } else if (opcion == 3) {
            game.splash("Adiós", "Hasta la próxima")
            game.over(false)
        } else {
            game.showLongText("Opción no válida", DialogLayout.Top)
        }
        
    }
}

menu_inicio()
let jugador = sprites.create(img`
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
`, SpriteKind.Player)
jugador.setStayInScreen(true)
let npc = sprites.create(assets.image`vill`, SpriteKind.Enemy)
npc.setPosition(44, 97)
let npc2 = sprites.create(assets.image`vill0`, SpriteKind.Enemy)
npc2.setPosition(120, 80)
controller.moveSprite(jugador, MOVE_SPEED_X, MOVE_SPEED_Y)
scene.setBackgroundImage(assets.image`myImage`)
forever(function on_forever() {
    game_loop()
})
