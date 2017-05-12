import random


# Problem 3
def gen_numbers():
    """This function will generate 2 random numbers and multiply them together.
        It will then prompt the user to guess what the product of those numbers is."""
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = x + y
    user_guess = 0

    while user_guess != z:
        print("What is the result of %d * %d?" % (x, y))
        user_guess = int(input("Answer: "))
        if user_guess != z:
            print("That is not correct.")
    return print("You are correct.")

if __name__ == "__main__":
    gen_numbers()
