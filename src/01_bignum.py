# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE


#print(2**65536)

def bignum(x: int = 2, y: int = 65536) -> int:
    """
    Prints out x to the y power

    Args:
      x: 2
      y: 65536

    Returns:
      int: x ** y

    Raises:
      None

    """
    return x ** y

print(bignum())

assert bignum() == 2 ** 65536
