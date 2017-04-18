# planet.py

from planetarypy.parameter import Parameter

class Planet:
    def __init__(self, name):
        self.name = name
        self.mass = 0.0
        self.radius = 0.0
        self.gravity = 0.0
        self.vals = {}

        if not isinstance(self.name,str):
            raise TypeError("Planet name must be of type 'string'")

    def set_val(self, name, val, unit=False, citation=False):
        self.vals[name] = Parameter(name, val, unit, citation)

        if name == 'Mass':
            self.mass = val

        elif name == "Radius":
            self.radius = val

        elif name == "Gravity":
            self.gravity = val


if __name__ == "__main__":
    jupiter = Planet("Jupiter")
    jupiter.set_val('Mass', 1.3e27, 'kg', "wikipedia")
    a = jupiter.vals['Mass'].value()
    a_unit = jupiter.vals['Mass'].units()
    a2 = jupiter.mass
    print(a,a_unit,a2)

