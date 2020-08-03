# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num: int) -> bool:
    """
    Function to determing if number is even

    Args:
        int: A number

    Returns:
        bool: True if even, False if not

    """
    if num % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def print_even(num: int):
    """
    Function to print out "even!" if the
    number is even. Otherwise print "odd".

    args:


    Returns:


    """
    if is_even(num) == True:
        print("Even!")
    else:
        print("Odd")


print(print_even(num))
