from typing import List

def multiply_list(values: List[int]) -> int:
    """
    Multiplies all the values in a list together.
    Arguments:
        values: List of integers to be multiplied.
    Returns: The product of all the values.
    """
    product = 1
    for v in values:
        product *= v
    return product
