# Colors
white = 'white'
green = 'green'
orange = 'orange'
red = 'red'
blue = 'blue'
yellow = 'yellow'


class Cube:

    def __init__(self):
        faces = {
            'u': [[orange, orange], [orange, orange]],
            'd': [[red, red], [red, red]],
            'l': [[green, green], [green, green]],
            'r': [[blue, blue], [blue, blue]],
            'f': [[white, white], [white, white]],
            'b': [[yellow, yellow], [yellow, yellow]]
        }
