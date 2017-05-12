import math


# Problem 1
class Circle:
    def __init__(self, radius):
        self.r = radius

    def diameter(self):
        """This function will calculate the diameter of the circle using the input radius."""
        return 2 * self.r

    def circumference(self):
        """This function will calculate the circumference of the circle using the input radius."""
        return 2 * math.pi * self.r

    def area(self):
        """This function will calculate the area of the circle using the input radius."""
        return math.pi * (self.r ** 2)


def circle_create():
    """This function creates prompts the user for the radius and then performs the necessary calculations."""
    userR = int(input("Enter the radius of the circle:"))
    circle = Circle(userR)

    circum = circle.circumference()
    diam = circle.diameter()
    area = circle.area()

    print("The circumference of your circle is %d." % circum)
    print("The diameter of your circle is %d." % diam)
    print("The area of your circle is %d." % area)

if __name__ == "__main__":
    circle_create()
