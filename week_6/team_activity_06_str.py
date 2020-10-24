"""
File: Week 6 - Team Activity - Stretch
By: Lewis Lockhart
"""

"""
Discuss with your team the pros and cons of the IS-A vs HAS-A approach 
to this problem. Determine which approach you feel is best and why. 

IS-A - this seems to require less coding but looking at the class, 
    it is a little harder to see what is happening.
    
HAS-A - this requires more code but the origin of the methods is far
    more clear. Allows for more than one instance of Point.
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


class Circle:
    def __init__(self):
        self.radius = 0.0
        self.center = Point()

    def prompt_for_circle(self):
        self.center.prompt_for_point()
        self.radius = input("Enter radius: ")

    def display_circ(self):
        print("Center:")
        self.center.display()
        print("Radius: {}".format(self.radius))


def main():
    c = Circle()
    c.prompt_for_circle()
    print('')
    c.display_circ()


if __name__ == '__main__':
    main()
