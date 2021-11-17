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


class Cone:
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
        self.area =  pi * r * ( r + math.sqrt(h**2 + r**2))
        return (self.area)

    def V(self):
        r = self.radius
        h = self.height
        self.volume = pi * (r**2) * (h / 3)
        return (self.volume)


class SquarePyramid:
    def __init__(self, a, h):
        self.base = a
        self.height = h
        self.area = 0
        self.volume = 0

    def Base(self):
        return self.base

    def Height(self):
        return self.height

    def SA(self):
        a = self.base
        h = self.height
        self.area =  a**2 + (2*a) * math.sqrt((a**2/4) + h**2)
        return (self.area)

    def V(self):
        a = self.base
        h = self.height
        self.volume = a**2 * ( h / 3)
        return (self.volume)

class Rectangulartank:
    def __init__(self, w, h, l):
        self.width = w
        self.height = h
        self.length = l
        self.area = 0
        self.volume = 0

    def Width(self):
        return self.width

    def Height(self):
        return self.height

    def Length(self):
        return self.length

    def SA(self):
        w = self.width
        h = self.height
        l = self.length
        self.area = (2 * l * w) + (2 * l * h) + (2 * w * h)
        return (self.area)

    def V(self):
        w = self.width
        h = self.height
        l = self.length
        self.volume = w * h * l
        return (self.volume)


class Cube:
    def __init__(self, a):
        self.base = a
        self.area = 0
        self.volume = 0

    def Base(self):
        return self.base

    def SA(self):
        a = self.base
        self.area = 6 * a**2
        return (self.area)

    def V(self):
        a = self.base
        self.volume = a**3
        return (self.volume)
