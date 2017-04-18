
def find_units(name):
    unit_dict = {"Mass": "kg",
                 "Radius": "m",
                 "Gravity": "m s^-2",
                 "Semimajor axis": 'm',
                 "Eccentricity": ''}

    return(unit_dict[name])
