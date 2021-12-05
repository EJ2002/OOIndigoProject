import math
pi = math.pi


class Nosides_parameter:
    def __init__(self, r):
        self.radius = r
        self.area = 0
        self.volume = 0

    def radius(self):
        return self.radius


class Withsides_parameters:
    def __init__(self, a, h):
        self.base = a
        self.height = h
        self.area = 0
        self.volume = 0

    def base(self):
        return self.base

    def height(self):
        return self.height

class Circbase:
    def __init__(self, r, h):
        self.radius = r
        self.height = h
        self.area = 0
        self.volume = 0

    def radius(self):
        return self.radius

    def height(self):
        return self.height


class Spheres(Nosides_parameter):
    def SA(self):
        r = self.radius
        self.area = 4 * pi * (r**2)
        return (self.area)

    def V(self):
        r = self.radius
        self.volume = (4/3) * pi * (r**3)
        return (self.volume)


class Torus(Nosides_parameter):
    def __init__(self, r, s):
        self.smallradius = s
        Nosides_parameter.__init__(self, r)


    def SA(self):
        r = self.radius
        s = self.smallradius
        self.area = (2 * pi * r) * (2 * pi * s)
        return (self.area)

    def V(self):
        r = self.radius
        s = self.smallradius
        self.volume = (pi * s**2) * (2 * pi * r)
        return (self.volume)

class Ellipsoid(Nosides_parameter):
    def __init__(self, r, s, x):
        self.radius2 = s
        self.radius3 = x
        Nosides_parameter.__init__(self, r)
    def SA(self):
        r = self.radius
        s = self.radius2
        x = self.radius3
        self.area = 4 * pi * (((r*s)**1.6)/3 + ((r*x)**1.6)/3 + ((s*x)**1.6)/3)**(1/1.6)
        return (self.area)

    def V(self):
        r = self.radius
        s = self.radius2
        x = self.radius3
        self.volume = 4/3 * pi * r * s * x
        return (self.volume)


class Cylinder(Circbase):
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


class Cone(Circbase):
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


class SquarePyramid(Withsides_parameters):

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


class Rectangulartank(Withsides_parameters):
    def __init__(self, w, h, l, a):
        self.width = w
        self.length = l
        Withsides_parameters.__init__(self, a, h)

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


class Cube(Withsides_parameters):
    def SA(self):
        a = self.base
        self.area = 6 * a**2
        return (self.area)

    def V(self):
        a = self.base
        self.volume = a**3
        return (self.volume)


class TriangularPrism(Withsides_parameters):
    def __init__(self, b, h, c, a):
        self.base2 = b
        self.base3 = c
        Withsides_parameters.__init__(self, a, h)
    def SA(self):
        a = self.base
        b = self.base2
        c = self.base3
        h = self.height
        self.area = (a*h) + (b*h) + (c*h) + 1/2 * math.sqrt(-a**4 + 2 *(a*b)**2 + 2 *(a*c)**2 - b**4 + 2 *(c*b)**2 - c**4)
        return (self.area)

    def V(self):
        a = self.base
        b = self.base2
        c = self.base3
        h = self.height
        self.volume = 1/4 * h * math.sqrt(-(a**4) + 2 *(a*b)**2 + 2 *(a*c)**2 - (b**4 )+ 2 *(c*b)**2 -(c**4))
        return (self.volume)
