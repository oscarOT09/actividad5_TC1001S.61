from random import shuffle
from turtle import *

# Usar 32 emojis únicos para cubrir 64 fichas (duplicados para que haya pares)
tiles = list('🍎🍊🍉🍇🍓🍒🍍🥥🍋🍑🥭🍌🍈🍐🍏🥝🍔🍟🍕🌭🍿🍫🍩🍪🍰🍦🍨🍧🍫🍬⭐🌻') * 2
state = {'mark': None, 'taps': 0}
hide = [True] * 64

def square(x, y):
    "Dibuja un cuadrado blanco con borde negro en (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convierte las coordenadas (x, y) en un índice de fichas."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convierte el índice de la ficha a coordenadas (x, y)."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Actualiza la marca y las fichas ocultas en función del toque."
    spot = index(x, y)
    mark = state['mark']

    state['taps'] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Verifica si todas las fichas están destapadas
    if all(not hidden for hidden in hide):
        print("¡Has destapado todas las fichas! ¡Juego terminado!")
        print(f"Has completado el juego con {state['taps']} toques.")

def draw():
    "Dibuja las fichas e imágenes."
    clear()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 10)  # Ajustar la posición del emoji
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))  # Ajustar el tamaño de fuente para emojis

    # Muestra el contador de toques
    up()
    goto(140, 200)  # Nueva posición fuera del tablero
    color('black')
    write(f'Taps: {state["taps"]}', font=('Arial', 20, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(500, 500, 370, 0)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
