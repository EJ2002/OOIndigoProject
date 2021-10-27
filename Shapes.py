from Formulas import Spheres, Cylinder

def menu():

    print(
                """
                VOLUME AND AREA CALCULATOR
                1. Sphere
                2. Cylinder
                3. Call menu
                4. Quit
                """
            )

try:
    menu()
    while True:

        command = int(input("Enter command: "))

        if command == 1:
            r = int(input("Enter radius of Sphere: "))
            s = Spheres(r)
            print("The Surface area of the Sphere is: ", round(s.SA(), 2))
            print("The Volume of the Sphere is: ", round(s.V(), 2))
        elif command == 2:
            r = int(input('Enter radius of Cylinder: '))
            h = int(input("Enter height of Cylinder: "))
            c = Cylinder(r, h)
            print("The Surface area of the Cylinder is: ", round(c.SA(), 2))
            print("The Volume of the Cylinder is: ", round(c.V(), 2))
        elif command == 3:
            menu()
        elif command == 4:
            print("Thank you for using the program.")
            break
        else:
            print("Please enter a valid command.")
except ValueError:
    print("You have entered a non-numeral value.")
