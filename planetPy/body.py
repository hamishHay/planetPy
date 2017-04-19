# planet.py

from planetPy.parameter import Parameter
from planetPy.constants import G
from numpy import pi, sqrt

class Body:
    def __init__(self, name, body_type):
        self.name = name
        self.body_type = body_type
        self.mass = 0.0
        self.radius = 0.0
        self.density = 0.0
        self.gravity = 0.0
        self.rotation_period = 0.0

        self.semimajor_axis = 0.0
        self.orbit_period = 0.0
        self.mean_motion = 0.0
        self.eccentricity = 0.0
        self.pericenter = 0.0
        self.apocenter = 0.0

        self.parent = None

        self.vals = {}

        if not isinstance(self.name,str):
            raise TypeError("Planet name must be of type 'string'")

    def setVal(self, name, val, unit=False, citation=False):
        # self.vals[name] = Parameter(name, val, unit, citation)

        if name == 'Mass':
            self.mass = val
        elif name == "Radius":
            self.radius = val
        elif name == "Gravity":
            self.gravity = val
        elif name == "Rotation period":
            self.rotation_period = val
        elif name == "Semimajor axis":
            self.semimajor_axis = val
        elif name == "Eccentricity":
            self.eccentricity = val

        if self.mass != 0.0 and self.radius != 0.0:
            if self.gravity == 0.0:
                self.calcGravity()
            if self.density == 0.0:
                self.calcDensity()

        if self.mass != 0.0 and self.semimajor_axis != 0.0 and self.parent.mass != 0.0:
            if self.orbit_period == 0.0:
                self.calcOrbitPeriod()

        if self.eccentricity != 0.0 and self.semimajor_axis != 0.0:
            self.calcApocenter()
            self.calcPericenter()

    def calcGravity(self):
        self.gravity = G*self.mass/self.radius**2.0
        # self.vals["Gravity"] = Parameter("Gravity", self.gravity, "m s^-2", False)

    def calcDensity(self):
        self.density = self.mass / (4./3. * pi * self.radius**3)
        # self.vals["Density"] = Parameter("Density", self.density, "kg m^-3", False)

    def calcOrbitPeriod(self):
        self.orbit_period = 2.*pi * sqrt((self.semimajor_axis**3.)/(G*(self.parent.mass + self.mass)))
        # self.vals["Orbit period"] = Parameter("Orbit period", self.orbit_period, "s", False)

        self.mean_motion = 2.*pi/self.orbit_period
        # self.vals["Mean motion"] = Parameter("Mean motion", self.mean_motion, "rad s^-1", False)

    def calcApocenter(self):
        self.apocenter = self.semimajor_axis * (1.0 - self.eccentricity)
        # self.vals["Apocenter"] = Parameter("Apocenter", self.apocenter, "m", False)

    def calcPericenter(self):
        self.pericenter = self.semimajor_axis * (1.0 + self.eccentricity)
        # self.vals["Pericenter"] = Parameter("Pericenter", self.pericenter, "m", False)

class Star(Body):
    def __init__(self, name):
        Body.__init__(self, name, "Star")

        self.planets = {}
        self.planet_list = []

    def addPlanet(self, planet):
        self.planets[planet.name] = planet
        self.planet_list.append(planet)

    def __str__(self):
        return self.name

class Planet(Body):
    def __init__(self, name, parent=False):
        Body.__init__(self, name, "Planet")

        if isinstance(parent, Star):
            self.parent = parent
            parent.addPlanet(self)

        self.moons = {}
        self.moon_list = []

    def addMoon(self, moon):
        self.moons[moon.name] = moon
        self.moon_list.append(moon)

    def __str__(self):
        return self.name

class Moon(Body):
    def __init__(self, name, parent=False):
        Body.__init__(self, name, "Moon")

        if isinstance(parent, Planet):
            self.parent = parent
            parent.addMoon(self)

    def __str__(self):
        return self.name

if __name__ == "__main__":
    jupiter = Planet("Jupiter")
    jupiter.set_val('Mass', 1.3e27, 'kg', "wikipedia")
    a = jupiter.vals['Mass'].value()
    a_unit = jupiter.vals['Mass'].units()
    a2 = jupiter.mass
    print(a,a_unit,a2)
