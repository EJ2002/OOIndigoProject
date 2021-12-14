from Formulas import Spheres, Cylinder, Cone, SquarePyramid, Rectangulartank, Cube, Torus, TriangularPrism, Ellipsoid
from Menus import menu1, menu2, menu3, menu4

try:
    menu1()
    while True:

        command = int(input("Select a Category: "))

        if command == 1:  # SHAPES WITH NO SIDES
            menu2()
            Nosides = int(input("Enter command: "))
            if Nosides == 1:
                r = int(input("Enter Radius of Sphere: "))
                s = Spheres(r)
                print("The Surface Area of the Sphere is: ", round(s.sa(), 2))
                print("The volume of the Sphere is: ", round(s.v(), 2))

            if Nosides == 2:
                r = int(input("Enter Major Radius of Torus: "))
                s = int(input('Enter Minor Radius of Torus:'))
                T = Torus(r, s)
                print("The Surface Area of the Torus is: ", round(T.sa(), 2))
                print("The volume of the Torus is: ", round(T.v(), 2))

            if Nosides == 3:
                r = int(input("Enter axis1 of Ellipsoid: "))
                s = int(input("Enter axis2 of Ellipsoid: "))
                x = int(input("Enter axis3 of Ellipsoid: "))
                E = Ellipsoid(r, s, x)
                print("The Surface Area of the Ellipsoid is: ", round(E.sa(), 2))
                print("The volume of the Ellipsoid is: ", round(E.v(), 2))
            if Nosides == 4:  # BACK TO MENU
                menu1()

        if command == 2:  # SHAPES WITH SIDES
            menu3()
            Withsides = int(input("Enter command: "))
            if Withsides == 1:
                a = int(input('Enter Base Edge of the Square Pyramid: '))
                h = int(input('Enter the Height of the Square Pyramid: '))
                Sp = SquarePyramid(a, h)
                print("The Surface area of the Square Pyramid is: ", round(Sp.sa(), 2))
                print("The volume of the Square Pyramid is: ", round(Sp.v(), 2))

            if Withsides == 2:
                l = int(input('Enter length of the Rectangular Tank: '))
                w = int(input('Enter width of the Rectangular Tank: '))
                h = int(input('Enter Height of the Rectangular Tank: '))
                a = 0
                Rt = Rectangulartank(w, h, l, a)
                print("The Surface area of the Rectangular Tank is: ", round(Rt.sa(), 2))
                print("The volume of the Rectangular Tank is: ", round(Rt.v(), 2))

            if Withsides == 3:
                a = int(input('Enter Edge Length of Cube: '))
                h = 0
                c = Cube(a, h)
                print("The Surface area of the Cube is: ", round(c.sa(), 2))
                print("The volume of the Cube is: ", round(c.v(), 2))

            if Withsides == 4:
                a = int(input('Enter base1 of the Triangular Prism: '))
                b = int(input('Enter base2 of the Triangular Prism: '))
                c = int(input('Enter base3 of the Triangular Prism: '))
                h = int(input('Enter Height of the Triangular Prism: '))
                Tp = TriangularPrism(a, b, c, h)
                print("The Surface area of the Triangular Prism is: ", round(Tp.sa(), 2))
                print("The volume of the Triangular Prism is: ", round(Tp.v(), 2))

            elif Withsides == 5:
                menu1()

        if command == 3:  # CIRCULAR BASE
            menu4()
            Circbase = int(input("Enter command: "))
            if Circbase == 1:
                r = int(input('Enter Radius of Cylinder: '))
                h = int(input("Enter Height of Cylinder: "))
                c = Cylinder(r, h)
                print("The Surface area of the Cylinder is: ", round(c.sa(), 2))
                print("The volume of the Cylinder is: ", round(c.v(), 2))

            if Circbase == 2:
                r = int(input('Enter Base Radius of the Cone: '))
                h = int(input('Enter the Height of the Cone: '))
                c = Cone(r, h)
                print("The Surface area of the Cone is: ", round(c.sa(), 2))
                print("The volume of the Cone is: ", round(c.v(), 2))

            if Circbase == 3:
                menu1()

        if command == 4:
            menu1()

        if command == 5:
            print("Thank you for using the program.")
            break

        elif command >= 6 or command == 0:
            print("Please Enter a value from the --MENU--")


except ValueError:

    print("ERROR!!! You have entered a non-numeral value.", "\n"
          "PROGRAM WILL TERMINATE.")

except ZeroDivisionError:
    print("ERROR!!! Divisor is equal to 000. ", "\n"
          "PROGRAM WILL TERMINATE.")

    
