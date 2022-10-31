import math
class Tire:

    def __init__ (self, tire_type="estandar", width="estandar", ratio="estandar", diameter="estandar", brand=" ", construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction
    def circumference(self):
        side_wall_inches = (self.width * (self.ratio / 100)) / 25.4
        total_diameter = side_wall_inches * 2 + self.diameter
        return round (total_diameter * math.pl, 1)

class SnowTire(Tire):
     def __init__ (self, tipo_nieve="fria"):
       super().__init__()
       self.tipo_nieve=tipo_nieve