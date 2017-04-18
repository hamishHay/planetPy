
from planetarypy import units

class Parameter:
    def __init__(self, name, val, unit=False, citation=False):
        self.name = name
        self.val = val
        self.citation = citation

        if not unit:
            self.unit = units.find_units(name)
        else:
            self.unit = unit

    def value(self):
        return self.val

    def units(self):
        return self.unit

    def citation(self):
        return self.citation