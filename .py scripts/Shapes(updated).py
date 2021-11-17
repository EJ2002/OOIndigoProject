from Formulas import Spheres, Cylinder

def menu():

    print(
                """
                VOLUME AND AREA CALCULATOR
                1. Sphere
                2. Cylinder
                3. Cone
                4. Square Pyramid
                5. Rectangular Tank
                6. Cube
                7. Call menu
                8. Quit
                """
            )

try:
    menu()
    while True:

        command = int(input("Enter command: "))

        if command == 1:
            r = int(input("Enter Radius of Sphere: "))
            s = Spheres(r)
            print("The Surface Area of the Sphere is: ", round(s.SA(), 2))
            print("The Volume of the Sphere is: ", round(s.V(), 2))

        elif command == 2:
            r = int(input('Enter Radius of Cylinder: '))
            h = int(input("Enter Height of Cylinder: "))
            c = Cylinder(r, h)
            print("The Surface area of the Cylinder is: ", round(c.SA(), 2))
            print("The Volume of the Cylinder is: ", round(c.V(), 2))

        elif command == 3:
            r = int(input('Enter Base Radius of the Cone: '))
            h = int(input('Enter the Height of the Cone: '))

        elif command == 4:
            b = int(input('Enter Base Edge of the Square Pyramid'))
        elif command == 5:
            l = int(input('Enter length of the Rectangular Tank'))
            w = int(input('Enter width of the Rectangular Tank'))
            h = int(input('Enter Height of the Rectangular Tank'))
        elif command == 6:
            el = int(input('Enter Edge Length of Cube: '))
            break
        elif command == 7:
            menu()
        elif command == 8:
            print("Thank you for using the program.")
            break
        else:
            print("Please enter a valid command.")
except ValueError:
    print("You have entered a non-numeral value.")
