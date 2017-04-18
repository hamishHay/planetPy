from planetarypy.planet import Planet

class Database:
    def __init__(self):
        self.version = "v0.1"

        self.mercury = Planet("Mercury")
        self.mercury.set_val("Radius", 2439.7e3)
        self.mercury.set_val("Mass", 3.3011e23)
        self.mercury.set_val("Gravity", 3.7)

        self.venus = Planet("Venus")
        self.venus.set_val("Radius", 69911e3)
        self.venus.set_val("Mass", 1.8986e27)
        self.venus.set_val("Gravity", 24.79)

        self.earth = Planet("Earth")
        self.earth.set_val("Radius", 69911e3)
        self.earth.set_val("Mass", 1.8986e27)
        self.earth.set_val("Gravity", 24.79)

        self.mars = Planet("Mars")
        self.mars.set_val("Radius", 69911e3)
        self.mars.set_val("Mass", 1.8986e27)
        self.mars.set_val("Gravity", 24.79)

        self.jupiter = Planet("Jupiter")
        self.jupiter.set_val("Radius", 69911e3)
        self.jupiter.set_val("Mass", 1.8986e27)
        self.jupiter.set_val("Gravity", 24.79)

        self.saturn = Planet("Saturn")

        self.uranus = Planet("Uranus")

        self.neptune = Planet("Neptune")

        self.pluto = Planet("Pluto")


if __name__ == "__main__":

    planets = Database()
    jupiter = planets.jupiter

    print(jupiter.radius, jupiter.mass, jupiter.gravity)

    print(jupiter.vals["Radius"].units())