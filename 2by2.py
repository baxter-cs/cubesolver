# Colors
white = 'white'
green = 'green'
orange = 'orange'
red = 'red'
blue = 'blue'
yellow = 'yellow'


class Cube:

    def __init__(self):
        self.faces = {
            'u': [[orange, orange], [orange, orange]],
            'd': [[red, red], [red, red]],
            'l': [[green, green], [green, green]],
            'r': [[blue, blue], [blue, blue]],
            'f': [[white, white], [white, white]],
            'b': [[yellow, yellow], [yellow, yellow]]
        }

    def face_to_str(self, face):
        if face in self.faces is False:
            return 'INVALID FACE'
        face = self.faces[face]
        output = ''
        for row in face:
            for cell in row:
                output += '{} '.format(cell)
        return output

cube = Cube()
print(cube.face_to_str('u'))
