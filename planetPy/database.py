from planetPy.body import Star
from planetPy.body import Planet
from planetPy.body import Moon
from planetPy.constants import AU

class Database:
    def __init__(self):
        self.version = "v0.1"

        self.stars = []
        self.planets = []
        self.moons = []

        self.sun = Star("Sun")
        self.sun.setVal("Mass", 1.98855e30)
        self.sun.setVal("Radius", 695700e3)
        self.stars.append(self.sun)

        # -----------------------------------------------
        # ----------------DEFINE PLANETS-----------------
        # -----------------------------------------------

        self.mercury = Planet("Mercury", parent=self.sun)
        self.mercury.setVal("Radius", 2439.7e3)
        self.mercury.setVal("Mass", 3.3011e23)
        self.mercury.setVal("Semimajor axis", 57909050e3)
        self.mercury.setVal("Eccentricity", 0.205630)
        self.planets.append(self.mercury)

        self.venus = Planet("Venus", parent=self.sun)
        self.venus.setVal("Radius",6051.8e3)
        self.venus.setVal("Mass", 4.8675e24)
        self.venus.setVal("Semimajor axis", 1.08208e11)
        self.venus.setVal("Eccentricity", 0.006772)
        self.planets.append(self.venus)

        self.earth = Planet("Earth", parent=self.sun)
        self.earth.setVal("Radius", 6371.0e3)
        self.earth.setVal("Mass", 5.97237e24)
        self.earth.setVal("Semimajor axis", 1.49598023e11)
        self.earth.setVal("Eccentricity", 0.0167086)
        self.planets.append(self.earth)

        self.mars = Planet("Mars", parent=self.sun)
        self.mars.setVal("Radius", 3389.5e3)
        self.mars.setVal("Mass", 6.4171e23)
        self.mars.setVal("Semimajor axis", 1.523679*AU)
        self.mars.setVal("Eccentricity", 0.0934)
        self.planets.append(self.mars)

        self.jupiter = Planet("Jupiter", parent=self.sun)
        self.jupiter.setVal("Radius", 69911e3)
        self.jupiter.setVal("Mass", 1.8986e27)
        self.jupiter.setVal("Semimajor axis", 5.20260*AU)
        self.jupiter.setVal("Eccentricity", 0.048498)
        self.planets.append(self.jupiter)

        self.saturn = Planet("Saturn", parent=self.sun)
        self.saturn.setVal("Radius", 58232e3)
        self.saturn.setVal("Mass", 5.6836e26)
        self.saturn.setVal("Semimajor axis", 9.5549*AU)
        self.saturn.setVal("Eccentricity", 0.05555)
        self.planets.append(self.saturn)

        self.uranus = Planet("Uranus", parent=self.sun)
        self.uranus.setVal("Radius", 25362e3)
        self.uranus.setVal("Mass", 8.6810e25)
        self.uranus.setVal("Semimajor axis", 19.2184*AU)
        self.uranus.setVal("Eccentricity", 0.046381)
        self.planets.append(self.uranus)

        self.neptune = Planet("Neptune", parent=self.sun)
        self.neptune.setVal("Radius", 24622e3)
        self.neptune.setVal("Mass", 1.0243e26)
        self.neptune.setVal("Semimajor axis", 30.33*AU)
        self.neptune.setVal("Eccentricity", 0.009456)
        self.planets.append(self.neptune)

        self.pluto = Planet("Pluto", parent=self.sun)
        self.pluto.setVal("Radius", 1187e3)
        self.pluto.setVal("Mass", 1.303e22)
        self.pluto.setVal("Semimajor axis", 39.48*AU)
        self.pluto.setVal("Eccentricity", 0.2488)
        self.planets.append(self.pluto)

        # -----------------------------------------------
        # ---------------DEFINE SATELLITES---------------
        # -----------------------------------------------

        # EARTH
        self.moon = Moon("Moon", parent=self.earth)
        self.moon.setVal("Radius", 1737.1e3)
        self.moon.setVal("Mass", 7.34767309e22)
        self.moon.setVal("Semimajor axis", 384399e3)
        self.moon.setVal("Eccentricity", 0.0549)
        self.moon.setVal("Rotation period", "Synchronous")

        # MARS
        self.phobos = Moon("Phobos", parent=self.mars)
        self.phobos.setVal("Radius", 11.2667e3)
        self.phobos.setVal("Mass", 1.0659e16)
        self.phobos.setVal("Gravity", 5.7e-3)
        self.phobos.setVal("Semimajor axis", 9376e3)
        self.phobos.setVal("Eccentricity", 0.0151)
        self.phobos.setVal("Rotation period", "Synchronous")

        self.deimos = Moon("Deimos", parent=self.mars)
        self.deimos.setVal("Radius", 6.2e3)
        self.deimos.setVal("Mass", 1.4762e15)
        self.deimos.setVal("Gravity", 3e-3)
        self.deimos.setVal("Semimajor axis", 23463.2e3)
        self.deimos.setVal("Eccentricity", 0.00033)
        self.deimos.setVal("Rotation period", "Synchronous")

        # JUPITER
        self.io = Moon("Io", parent=self.jupiter)
        self.io.setVal("Radius", 1821.6e3)
        self.io.setVal("Mass", 8.931938e22)
        self.io.setVal("Semimajor axis", 421800e3)
        self.io.setVal("Eccentricity", 0.0041)
        self.io.setVal("Rotation period", "Synchronous")

        self.europa = Moon("Europa", parent=self.jupiter)
        self.europa.setVal("Radius", 1560.8e3)
        self.europa.setVal("Mass", 4.799844e22)
        self.europa.setVal("Semimajor axis", 671100e3)
        self.europa.setVal("Eccentricity", 0.0094)
        self.europa.setVal("Rotation period", "Synchronous")

        self.ganymede = Moon("Ganymede", parent=self.jupiter)
        self.ganymede.setVal("Radius", 2634.1e3)
        self.ganymede.setVal("Mass", 1.4819e23)
        self.ganymede.setVal("Semimajor axis", 1070400e3)
        self.ganymede.setVal("Eccentricity", 0.0013)
        self.ganymede.setVal("Rotation period", "Synchronous")

        self.callisto = Moon("Callisto", parent=self.jupiter)
        self.callisto.setVal("Radius", 2410.3e3)
        self.callisto.setVal("Mass", 1.075938e23)
        self.callisto.setVal("Semimajor axis", 1882700e3)
        self.callisto.setVal("Eccentricity", 0.0074)
        self.callisto.setVal("Rotation period", "Synchronous")

        # SATURN
        self.mimas = Moon("Mimas", parent=self.saturn)
        self.mimas.setVal("Radius", 198.2e3)
        self.mimas.setVal("Mass", 3.7493e19)
        self.mimas.setVal("Semimajor axis", 185539e3)
        self.mimas.setVal("Eccentricity", 0.0196)
        self.mimas.setVal("Rotation period", "Synchronous")

        self.enceladus = Moon("Enceladus", parent=self.saturn)
        self.enceladus.setVal("Radius", 252.1e3)
        self.enceladus.setVal("Mass", 1.08022e20)
        self.enceladus.setVal("Semimajor axis", 237948e3)
        self.enceladus.setVal("Eccentricity", 0.0047)
        self.enceladus.setVal("Rotation period", "Synchronous")

        self.tethys = Moon("Tethys", parent=self.saturn)
        self.tethys.setVal("Radius", 531.1e3)
        self.tethys.setVal("Mass", 6.17449e20)
        self.tethys.setVal("Semimajor axis", 294670e3)
        self.tethys.setVal("Eccentricity", 0.0001)
        self.tethys.setVal("Rotation period", "Synchronous")

        self.dione = Moon("Dione", parent=self.saturn)
        self.dione.setVal("Radius", 561.4e3)
        self.dione.setVal("Mass", 1.095452e21)
        self.dione.setVal("Semimajor axis", 377396e3)
        self.dione.setVal("Eccentricity", 0.0022)
        self.dione.setVal("Rotation period", "Synchronous")

        self.rhea = Moon("Rhea", parent=self.saturn)
        self.rhea.setVal("Radius", 763.8e3)
        self.rhea.setVal("Mass", 2.306518e21)
        self.rhea.setVal("Semimajor axis", 527068e3)
        self.rhea.setVal("Eccentricity", 0.0002)
        self.rhea.setVal("Rotation period", "Synchronous")

        self.titan = Moon("Titan", parent=self.saturn)
        self.titan.setVal("Radius", 2575.5e3)
        self.titan.setVal("Mass", 1.3452e23)
        self.titan.setVal("Semimajor axis", 1221865e3)
        self.titan.setVal("Eccentricity", 0.0288)
        self.titan.setVal("Rotation period", "Synchronous")

        self.iapetus = Moon("Iapetus", parent=self.saturn)
        self.iapetus.setVal("Radius", 734.5e3)
        self.iapetus.setVal("Mass", 1.805635e21)
        self.iapetus.setVal("Semimajor axis", 3560840e3)
        self.iapetus.setVal("Eccentricity", 0.0283)
        self.iapetus.setVal("Rotation period", "Synchronous")

        # -----------------------------------------------
        # ---------------55-CANCRI SYSTEM----------------
        # -----------------------------------------------

        self.exo_55_cancri_a= Star("55-cancri a")
        self.exo_55_cancri_a.setVal("Mass", 0.905*self.sun.mass)
        self.exo_55_cancri_a.setVal("Radius", 0.943*self.sun.radius)
        self.stars.append(self.exo_55_cancri_a)

        self.exo_55_cancri_b = Planet("55-cancri b", parent=self.exo_55_cancri_a)
        self.exo_55_cancri_b.setVal("Mass", 263.9785*self.earth.mass)
        # self.exo_55_cancri_b.setVal("Radius", 1.91*self.earth.radius)
        self.exo_55_cancri_b.setVal("Semimajor axis", 0.11522725*AU)
        self.planets.append(self.exo_55_cancri_b)

        self.exo_55_cancri_e = Planet("55-cancri e", parent=self.exo_55_cancri_a)
        self.exo_55_cancri_e.setVal("Mass", 8.08*self.earth.mass)
        self.exo_55_cancri_e.setVal("Radius", 1.91*self.earth.radius)
        self.exo_55_cancri_e.setVal("Semimajor axis", 0.01544*AU)
        self.planets.append(self.exo_55_cancri_e)

if __name__ == "__main__":

    planets = Database()
    jupiter = planets.jupiter

    print(jupiter.radius, jupiter.mass, jupiter.gravity)

    print(jupiter.vals["Radius"].units())
