function menu(): number {
    let opcio_usuari = game.askForNumber(`1: Gallina
2: Patata
3: Cabra`, 1)
    if (opcio_usuari >= 3 && opcio_usuari < 6) {
        opcio_usuari = game.askForNumber(`4: Huevos
5: Caballo
6: Salir
7`, 4)
    } else if (opcio_usuari > 6) {
        opcio_usuari = game.askForNumber("Salir", 7)
    }
    
    return opcio_usuari
}

function procesar_opcio(opcio: number) {
    if (opcio == 1) {
        game.showLongText("Has elegido: Gallina", DialogLayout.Top)
    } else if (opcio == 2) {
        game.showLongText("Has elegido: Patata", DialogLayout.Top)
    } else if (opcio == 3) {
        game.showLongText("Has elegido: Cabra", DialogLayout.Top)
    } else if (opcio == 4) {
        game.showLongText("Has elegido: Huevos", DialogLayout.Top)
    } else if (opcio == 5) {
        game.showLongText("Has elegido: Caballo", DialogLayout.Top)
    } else if (opcio == 6) {
        game.showLongText("Saliendo...", DialogLayout.Top)
        game.over(false)
        return
    } else {
        game.showLongText("Opción no válida", DialogLayout.Bottom)
        procesar_opcio(menu())
    }
    
}

procesar_opcio(menu())
