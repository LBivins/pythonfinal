# Problem 2
def triangle():
    """This function prompts the user for 2 sides of a triangle. It then calculates the hypotenuse from those sides."""
    userA = 0
    userB = 0
    while userA == 0 or userA > 20:
        userA = int(input("Enter a side of your triangle that is 20 or less:"))
    while userB == 0 or userB > 20:
        userB = int(input("Enter another side of your triangle that is 20 or less:"))

    hypotenuse = ((userA ^ 2 + userB ^ 2) ^ 2)

    print("The hypotenuse of your triangle is %d" % hypotenuse)

if __name__ == "__main__":
    triangle()