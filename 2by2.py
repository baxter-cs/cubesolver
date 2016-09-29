import json

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

    def dump(self):
        return json.dumps(self.faces)

    def load(self, json_string):
        self.faces = json.loads(json_string)

    def turn_u(self):
        # Change Top
        self.faces['u'][0][1], self.faces['u'][1][1], self.faces['u'][0][0], self.faces['u'][1][0] = \
            self.faces['u'][0][0], self.faces['u'][0][1], self.faces['u'][1][0], self.faces['u'][1][1]
        # Changing other sides
        self.faces['l'][0], self.faces['b'][0], self.faces['f'][0], self.faces['r'][0] = \
            self.faces['f'][0], self.faces['l'][0], self.faces['r'][0], self.faces['b'][0]


class TestSuite:
    def __init__(self):
        pass

    def turn_u(self):
        test_cube = Cube()
        before = '{"f": [["white", "white"], ["white", "white"]], "r": [["blue", "blue"], ["blue", "blue"]], "l": [["green", "green"], ["green", "green"]], "b": [["yellow", "yellow"], ["yellow", "yellow"]], "d": [["red", "red"], ["red", "red"]], "u": [["orange", "orange"], ["orange", "orange"]]}'
        expected_after = json.loads('{"f": [["blue", "blue"], ["white", "white"]], "r": [["yellow", "yellow"], ["blue", "blue"]], "l": [["white", "white"], ["green", "green"]], "b": [["green", "green"], ["yellow", "yellow"]], "d": [["red", "red"], ["red", "red"]], "u": [["orange", "orange"], ["orange", "orange"]]}')
        test_cube.load(before)
        test_cube.turn_u()
        after = dict(test_cube.faces)
        return expected_after == after

    def run_all_tests(self):
        if self.turn_u():
            print("Turn U Test Passed")
        else:
            print("Turn U Test Failed")

test = TestSuite()
test.run_all_tests()
