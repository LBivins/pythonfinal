import random


# Problem 4
def dupe_list():
    """This function will generate a random list and cycle through that list.
        It will then identify if the number read is a duplicate of the previous number."""
    randlist = []
    i = 0
    prev = 0
    duplicates = 0
    duplicatelist = []
    while i < 30:
        randlist.append(random.randint(0, 50))
        i += 1

    for num in randlist:
        if num == prev:
            print("%d is a duplicate of the previous number." % num)
            duplicatelist.append(num)
            duplicates += 1
        prev = num

    if duplicates > 1:
        print("There are %d duplicates in the list." % duplicates)
    elif duplicates == 1:
        print("There is %d duplicate in the list." % duplicates)
    else:
        print("There are no duplicates in the list.")

    if duplicates > 0:
        for num in duplicatelist:
            print("%d " % num, end='')

if __name__ == "__main__":
    dupe_list()
