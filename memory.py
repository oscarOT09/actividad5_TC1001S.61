import turtle as t
from random import shuffle

# Usar 32 emojis únicos para cubrir 64 fichas (duplicados para que haya pares)
emojis = (
    '🍎🍊🍉🍇🍓🍒🍍🥥'
    '🍋🍑🥭🍌🍈🍐🍏🥝'
    '🍔🍟🍕🌭🍿🍫🍩🍪'
    '🍰🍦🍨🍧🍫🍬⭐🌻'
)
tiles = list(emojis) * 2
state = {'mark': None, 'taps': 0}
hide = [True] * 64

def square(x, y):
    """Dibuja un cuadrado blanco con borde negro en la posición (x, y)."""
    t.up()
    t.goto(x, y)
    t.down()
    t.color('black', 'white')
    t.begin_fill()
    for count in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()

def index(x, y):
    """Convierte las coordenadas (x, y) en un índice de fichas."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convierte el índice de la ficha a coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Actualiza la marca y las fichas ocultas en función del toque."""
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
    """Dibuja las fichas y las imágenes en el tablero."""
    t.clear()

    for count in range(64):
        x, y = xy(count)
        if hide[count]:
            square(x, y)
        else:
            t.up()
            t.goto(x + 25, y + 10)
            t.color('black')
            t.write(
                tiles[count],
                align='center',
                font=('Arial', 30, 'normal')
            )

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        t.up()
        t.goto(x + 25, y + 10)  # Ajusta la posición del emoji
        t.color('black')
        t.write(
            tiles[mark],
            align='center',
            font=('Arial', 30, 'normal')
        )  # Ajusta el tamaño de fuente para emojis

    # Muestra el contador de toques
    t.up()
    t.goto(-180, 220)  # Ajustamos la posición para que sea visible
    t.color('black')
    t.write(
        f'Toques: {state["taps"]}',
        font=('Arial', 20, 'normal')
    )

    t.update()
    t.ontimer(draw, 100)

# Configuración inicial del juego
shuffle(tiles)
t.setup(500, 550, 370, 0)  # Aumentamos el alto para acomodar el contador
t.hideturtle()
t.tracer(False)
t.onscreenclick(tap)
draw()
t.done()
