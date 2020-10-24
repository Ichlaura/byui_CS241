"""
File: Week 6 - Team Activity
By: Lewis Lockhart
"""


class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def prompt_for_point(self):
        self.x = input("Enter x: ")
        self.y = input("Enter y: ")

    def display(self):
        print("({}, {})".format(self.x, self.y))


class Circle(Point):
    def __init__(self):
        self.radius = 0.0
        super().__init__()

    def prompt_for_circle(self):
        self.prompt_for_point()
        self.radius = input("Enter radius: ")

    def display_circ(self):
        print("Center:")
        self.display()
        print("Radius: {}".format(self.radius))


def main():
    c = Circle()
    c.prompt_for_circle()
    print('')
    c.display_circ()


if __name__ == '__main__':
    main()
