 

# Juego de Conversión de Productos y Troncos

## Variables

- `MOVE_SPEED_X`, `MOVE_SPEED_Y` – Velocidad de movimiento del jugador.
- `MAX_VISIBLE` – Número máximo de opciones visibles en el menú.
- `GALLINA_LENA`, `CABRA_LENA`, `CABALLO_LENA`, `HUEVOS_LENA`, `PATATA_FACTOR` – Factores de conversión entre productos y troncos.
- `MENU_PRINCIPAL`, `MENU_TRONCOS`, `MENU_INVERSO` – Listas de opciones de menú.
- `menu_index`, `menu_index_troncos`, `menu_index_inverso` – Índices actuales de los menús.
- `menu_abierto`, `menu_abierto_troncos`, `menu_abierto_inverso` – Estados de apertura de los menús.
- `a_prev`, `up_prev`, `down_prev` – Estados previos de los botones.
- `mensaje_npc_mostrado`, `mensaje_npc2_mostrado` – Controlan si los mensajes de los NPC ya se mostraron.

---

## Funciones

### `round2(x: number)`
Redondea `x` a dos decimales.

### `convertir_a_troncos(producto: str)`
Pregunta la cantidad de un producto y muestra cuántos troncos equivalen.

### `convertir_troncos_a(producto: str)`
Pregunta la cantidad de troncos y muestra cuántos productos se pueden obtener.

### `seleccionar_opcion(menu: List[str], index: number)`
Procesa la opción seleccionada de un menú:
- Convertir productos a troncos.
- Convertir troncos a productos.
- Mostrar tabla de precios.
- Salir del juego.

### `mostrar_menu_scroll(menu: List[str], index: number)`
Muestra un menú con scroll limitado a `MAX_VISIBLE` opciones y resalta la opción seleccionada.

### `game_loop()`
Se ejecuta continuamente. Controla:
- Mostrar diálogos de los NPCs.
- Abrir menús al presionar `A`.
- Navegar por los menús con las flechas arriba/abajo.
- Ejecutar la opción seleccionada al presionar `A`.

### `menu_inicio()`
Muestra la pantalla inicial con opciones: jugar, instrucciones o salir. Configura la imagen de fondo.

### `on_forever()`
Llama a `game_loop()` de forma continua para mantener la lógica del juego activa.

---

## Flujo de Juego

1. Se muestra `menu_inicio()` con las opciones iniciales.
2. Se crea el jugador y los NPCs.
3. `game_loop()` se ejecuta continuamente mediante `on_forever()`.
4. Al acercarse al NPC y presionar `A`, se abre el menú correspondiente.
5. El jugador puede navegar por el menú y seleccionar opciones que ejecutan las funciones de conversión o muestran la tabla de precios.
6. Los menús se cierran y el jugador puede moverse libremente nuevamente.


> Open this page at [https://raimonizard.github.io/demo/](https://raimonizard.github.io/demo/)

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://arcade.makecode.com/](https://arcade.makecode.com/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/raimonizard/demo** and import

## Edit this project ![Build status badge](https://github.com/raimonizard/demo/workflows/MakeCode/badge.svg)

To edit this repository in MakeCode.

* open [https://arcade.makecode.com/](https://arcade.makecode.com/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/raimonizard/demo** and click import

## Blocks preview

This image shows the blocks code from the last commit in master.
This image may take a few minutes to refresh.

![A rendered view of the blocks](https://github.com/raimonizard/demo/raw/master/.github/makecode/blocks.png)

#### Metadata (used for search, rendering)

* for PXT/arcade
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
