def divide(a: int, b: int) -> float:
    """Divides a by b and returns the quotient.\n\n    Args:\n        a: Integer, numerator.\n        b: Integer, denominator.\n\n    Returns:\n        Float, the result of the division.\n    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b