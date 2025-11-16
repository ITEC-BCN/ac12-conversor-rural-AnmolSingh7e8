//  --- Variables globales ---
let opcio_usuari = 0
let current_product = ""
let current_value = 0
let step = 0
let conversion_factor = 0
let result_kg = 0
let conversion_direction = "A->B"
//  Producto -> leña
//  --- Función de menú ---
function menu(): number {
    
    opcio_usuari = game.askForNumber(`1: Gallina
2: Patata
3: Cabra
4: Huevos
5: Caballo
6: Salir`, 1)
    return opcio_usuari
}

//  --- Selector de cantidad ---
function input_cantidad() {
    
    //  Inicializar cantidad y step según producto
    if (["Gallina", "Cabra", "Caballo", "Huevos"].indexOf(current_product) >= 0) {
        current_value = 1
        step = 1
    } else if (current_product == "Patata") {
        current_value = 0.5
        step = 0.1
    }
    
    //  Preguntar al usuario la cantidad
    current_value = game.askForNumber("Introduce cantidad de " + current_product + ":", current_value)
    calcular_conversion()
}

//  Ir a cálculo
//  --- Calcular conversión ---
function calcular_conversion() {
    let conversion_factor: number;
    
    //  Asignar factor según producto
    if (current_product == "Gallina") {
        conversion_factor = 6
    } else if (current_product == "Cabra") {
        conversion_factor = 5
    } else if (current_product == "Caballo") {
        conversion_factor = 12
    } else if (current_product == "Huevos") {
        conversion_factor = 0.25
    } else if (current_product == "Patata") {
        conversion_factor = 2 / 1.5
    } else {
        conversion_factor = 0
    }
    
    //  Validaciones
    if (current_value <= 0) {
        game.showLongText("Introduce un valor mayor que 0", DialogLayout.Bottom)
        input_cantidad()
        return
    }
    
    if (["Gallina", "Cabra", "Caballo"].indexOf(current_product) >= 0 && current_value % 1 != 0) {
        game.showLongText("Animales deben ser enteros", DialogLayout.Bottom)
        input_cantidad()
        return
    }
    
    //  Cálculo
    let redondeado = Math.trunc(result_kg * 100) / 100
    mostrar_resultado()
}

//  --- Mostrar resultado ---
function mostrar_resultado() {
    let redondeado = Math.trunc(result_kg * 100) / 100
    let texto = "" + current_value + " " + current_product + " → " + ("" + redondeado) + " kg leña"
    game.showLongText(texto, DialogLayout.Top)
    //  Volver al menú después del resultado
    procesar_opcio(menu())
}

//  --- Procesar opción del menú ---
function procesar_opcio(opcio: number) {
    
    if (opcio == 1) {
        current_product = "Gallina"
        game.showLongText("Has elegido: Gallina", DialogLayout.Top)
        input_cantidad()
    } else if (opcio == 2) {
        current_product = "Patata"
        game.showLongText("Has elegido: Patata", DialogLayout.Top)
        input_cantidad()
    } else if (opcio == 3) {
        current_product = "Cabra"
        game.showLongText("Has elegido: Cabra", DialogLayout.Top)
        input_cantidad()
    } else if (opcio == 4) {
        current_product = "Huevos"
        game.showLongText("Has elegido: Huevos", DialogLayout.Top)
        input_cantidad()
    } else if (opcio == 5) {
        current_product = "Caballo"
        game.showLongText("Has elegido: Caballo", DialogLayout.Top)
        input_cantidad()
    } else if (opcio == 6) {
        game.showLongText("Saliendo...", DialogLayout.Top)
        game.over(false)
    } else {
        game.showLongText("Opción no válida", DialogLayout.Bottom)
        procesar_opcio(menu())
    }
    
}

//  --- MAIN ---
procesar_opcio(menu())
