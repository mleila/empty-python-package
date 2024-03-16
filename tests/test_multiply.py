from src.mcalc.multipy import multiply_list


def test_multiply_list():
    assert multiply_list([1, 2, 3]) == 6

    assert multiply_list([10, 20]) == 200

    assert multiply_list([1, 0, 2]) == 0

    assert multiply_list([-3, 3]) == -9

    assert multiply_list([]) == 1