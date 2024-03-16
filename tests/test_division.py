from mcalc.division import divide

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3
    assert divide(25, 5) == 5
    try:
        divide(0, 0)
        raise AssertionError("Did not raise ValueError")
    except ValueError:
        pass
    try:
        divide(10, 0)
        raise AssertionError("Did not raise ValueError")
    except ValueError:
        pass