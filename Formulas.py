import math
pi = math.pi

class Spheres:
    def __init__(self, r):
        self.radius = r
        self.area = 0
        self.volume = 0

    def Radius(self):
        return self.radius

    def SA(self):
        r = self.radius
        self.area = 4 * pi * (r**2)
        return (self.area)

    def V(self):
        r = self.radius
        self.volume = (4/3) * pi * (r**3)
        return (self.volume)

class Cylinder:
    def __init__(self, r, h):
        self.radius = r
        self.height = h
        self.area = 0
        self.volume = 0

    def Radius(self):
        return self.radius

    def Height(self):
        return self.height

    def SA(self):
        r = self.radius
        h = self.height
        self.area = 2 * pi * r * h + 2 * pi * (r**2)
        return (self.area)

    def V(self):
        r = self.radius
        h = self.height
        self.volume = pi * (r**2) * h
        return (self.volume)
