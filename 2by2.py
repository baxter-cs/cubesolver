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

    def turn_u(self):
        # Change Top
        self.faces['u'][0][1], self.faces['u'][1][1], self.faces['u'][0][0], self.faces['u'][1][0] = self.faces['u'][0][0], self.faces['u'][0][1], self.faces['u'][1][0], self.faces['u'][1][1]
        # Changing other sides
        self.faces['l'][0][0], self.faces['l'][0][1], self.faces['b'][0][0], self.faces['b'][0][1], self.faces['f'][0][0], self.faces['f'][0][1], self.faces['r'][0][0], self.faces['r'][0][1] = self.faces['f'][0][0], self.faces['f'][0][1], self.faces['l'][0][0], self.faces['l'][0][1], self.faces['r'][0][0], self.faces['r'][0][1], self.faces['b'][0][0], self.faces['b'][0][1]

cube = Cube()
print(cube.face_to_str('u'))
print(cube.face_to_str('d'))
print(cube.face_to_str('l'))
print(cube.face_to_str('r'))
print(cube.face_to_str('f'))
print(cube.face_to_str('b'))
cube.turn_u()
print("Turned")
print(cube.face_to_str('u'))
print(cube.face_to_str('d'))
print(cube.face_to_str('l'))
print(cube.face_to_str('r'))
print(cube.face_to_str('f'))
print(cube.face_to_str('b'))