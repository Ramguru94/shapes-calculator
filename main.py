import argparse
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle

def cmd():
    parser = argparse.ArgumentParser(description="Shape Calculator")

    parser.add_argument("--circle", action="store_true", help="Calculate circle area and perimeter")
    parser.add_argument("--rectangle", action="store_true", help="Calculate rectangle area and perimeter")
    parser.add_argument("--square", action="store_true", help="Calculate square area and perimeter")
    parser.add_argument("--triangle", action="store_true", help="Calculate triangle area and perimeter")
    parser.add_argument("--radius", nargs=1, type=float, help="Radius of the circle")
    parser.add_argument("--length", nargs=1, type=float, help="Length of the rectangle")
    parser.add_argument("--width", nargs=1, type=float, help="Width of the rectangle")
    parser.add_argument("--side", nargs=1, type=float, help="Side of the square")
    parser.add_argument("--side1", nargs=1, type=float, help="Side1 of the triangle")
    parser.add_argument("--side2", nargs=1, type=float, help="Side2 of the triangle")
    parser.add_argument("--side3", nargs=1, type=float, help="Side3 of the triangle")
    parser.add_argument("--storage-account", type=str, required=False, default="fooaccount", help="The storage account that contains the event queues for this operation")

    return parser.parse_args()

def calculate_circle(args):
    if args.radius is None:
        raise ValueError("Radius is required for circle")
    shape = Circle(args.radius[0])
    print("Circle:")
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

def calculate_rectangle(args):
    if args.length is None or args.width is None:
        raise ValueError("Length and width are required for rectangle")
    shape = Rectangle(args.length[0], args.width[0])
    print("Rectangle:")
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

def calculate_square(args):
    if args.side is None:
        raise ValueError("Side is required for square")
    shape = Square(args.side[0])
    print("Square:")
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

def calculate_triangle(args):
    if args.side1 is None or args.side2 is None or args.side3 is None:
        raise ValueError("Side1, side2, and side3 are required for triangle")
    shape = Triangle(args.side1[0], args.side2[0], args.side3[0])
    print("Triangle:")
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

def main():
    args = cmd()
    if args.circle:
        if args.radius is None:
            print("Error: --radius parameter is required for circle")
        else:
            calculate_circle(args)
    elif args.rectangle:
        try:
            calculate_rectangle(args)
        except ValueError as e:
            print("Error:", e)
    elif args.square:
        try:
            calculate_square(args)
        except ValueError as e:
            print("Error:", e)
    elif args.triangle:
        try:
            calculate_triangle(args)
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
