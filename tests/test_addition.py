from mcalc.addition import add

def test_add():
    assert add(0, 0) == 0
    assert add(2, 3) == 5
    assert add(-3, 3) == 0
    assert add(-7, 7) == -14