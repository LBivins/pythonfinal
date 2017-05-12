# Problem 5
class Rectangle:
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def perim(self):
        """This function will calculate the perimeter of the Rectangle using the user given values."""
        return (2 * self.l) + (2 * self.w)

    def area(self):
        """This function will calculate the area of the Rectangle using the user given values."""
        return self.l * self.w

    def is_square(self):
        """This function checks if the Rectangle is actually a square based upon the length and width."""
        return self.l == self.w


def rectangle_create():
    """This function creates prompts the user for the length and width of the Rectangle.
        It then performs the necessary calculations and prints the results out to the screen."""
    userX = int(input("Enter the length of the rectangle:"))
    userY = int(input("Enter the width of the rectangle:"))
    rect = Rectangle(userX, userY)
    print("Rectangle's Area: " + str(rect.area()))
    print("Rectangle's Perimeter: " + str(rect.perim()))
    square = rect.is_square()
    if square:
        print("Rectangle is actually a square.")
    else:
        print("Rectangle is not a square.")

if __name__ == "__main__":
    rectangle_create()
