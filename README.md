# Juego de Memoria con Emojis

Este es un juego de memoria simple implementado en Python utilizando el módulo `turtle`. El objetivo es encontrar todos los pares de emojis iguales en el menor número de toques posible.

## Descripción del Juego

- **Tablero**: El juego presenta un tablero de 8x8 fichas, sumando un total de 64 fichas.
- **Emojis**: Se utilizan 32 emojis únicos duplicados para crear pares, mezclados aleatoriamente y ocultos detrás de las fichas.
- **Objetivo**: Descubrir todas las parejas de emojis haciendo coincidir las fichas iguales.
- **Interacción**: El jugador hace clic en las fichas para voltearlas y revelar el emoji oculto.
- **Contador de Toques**: Se registra y muestra en pantalla el número de toques o clics realizados durante el juego.
- **Finalización**: El juego termina cuando se han descubierto todas las parejas, mostrando un mensaje en la consola con el total de toques realizados.

## Requisitos

- **Python 3.x**: Asegúrate de tener Python instalado en tu sistema.
- **Módulo turtle**: Viene incluido en la instalación estándar de Python.

## Instrucciones de Instalación y Ejecución

1. **Descarga o Copia el Código**: Guarda el código en un archivo llamado `juego_memoria.py`.

2. **Ejecuta el Juego**:
   - Abre una terminal o línea de comandos.
   - Navega hasta el directorio donde guardaste `juego_memoria.py`.
   - Ejecuta el siguiente comando:

     ```bash
     python juego_memoria.py
     ```

   - Si tienes múltiples versiones de Python instaladas, puede que necesites usar `python3` en lugar de `python`.

## Cómo Jugar

- **Iniciar**: Al ejecutar el script, se abrirá una ventana con el tablero del juego.
- **Voltear Fichas**: Haz clic en cualquier ficha para revelar el emoji oculto.
- **Encontrar Pares**:
  - Si volteas dos fichas con el mismo emoji consecutivamente, permanecerán descubiertas.
  - Si los emojis no coinciden, las fichas se volverán a ocultar.
- **Seguir Jugando**: Continúa volteando fichas y memorizando la posición de los emojis para encontrar todos los pares.
- **Contador de Toques**: Observa el contador de "Toques" en la parte superior de la pantalla para ver cuántos clics has realizado.
- **Finalizar**: Una vez que hayas descubierto todos los pares, el juego te notificará en la consola y mostrará el total de toques.

## Personalización del Juego

- **Cambiar Emojis**: Puedes modificar la lista de emojis en la variable `emojis` para personalizar las imágenes del juego.
- **Ajustar Tamaño del Tablero**:
  - Para cambiar el tamaño del tablero, necesitarás ajustar las funciones `index()`, `xy()`, y las dimensiones de las fichas en `square()`.
  - Asegúrate de actualizar también la lista `hide` para que coincida con el nuevo número de fichas.

## Estructura del Código

### Importaciones

- `import turtle as t`: Importa el módulo `turtle` para manejar los gráficos.
- `from random import shuffle`: Importa la función `shuffle` para mezclar los emojis aleatoriamente.

### Variables Globales

- `emojis`: Cadena que contiene los emojis utilizados en el juego.
- `tiles`: Lista que duplica los emojis para crear pares y luego se mezcla.
- `state`: Diccionario para mantener el estado actual del juego, incluyendo la ficha marcada y el contador de toques.
- `hide`: Lista booleana que indica si cada ficha está oculta (`True`) o descubierta (`False`).

### Funciones Principales

- `square(x, y)`: Dibuja un cuadrado blanco con borde negro en las coordenadas especificadas.
- `index(x, y)`: Convierte las coordenadas de pantalla en un índice de la lista de fichas.
- `xy(count)`: Convierte un índice de ficha en coordenadas de pantalla.
- `tap(x, y)`: Maneja la lógica del juego cuando el jugador hace clic en una ficha.
  - Actualiza el estado de la ficha marcada.
  - Incrementa el contador de toques.
  - Verifica si se ha encontrado un par o si las fichas deben volver a ocultarse.
  - Comprueba si el juego ha terminado.
- `draw()`: Dibuja el estado actual del tablero, incluyendo fichas ocultas, fichas descubiertas y el contador de toques.
  - Se llama a sí misma cada 100 milisegundos utilizando `t.ontimer()` para actualizar la pantalla.

### Configuración Inicial

- `shuffle(tiles)`: Mezcla las fichas antes de iniciar el juego.
- `t.setup(500, 550, 370, 0)`: Configura el tamaño y posición de la ventana del juego.
- `t.hideturtle()`: Oculta el cursor de la tortuga.
- `t.tracer(False)`: Desactiva la animación para dibujar más rápido.
- `t.onscreenclick(tap)`: Vincula la función `tap` al evento de clic del mouse.
- `draw()`: Inicia el ciclo de dibujo del juego.
- `t.done()`: Mantiene la ventana abierta hasta que el usuario decida cerrarla.





---

¡Disfruta del juego y buena suerte encontrando todos los pares de emojis!
