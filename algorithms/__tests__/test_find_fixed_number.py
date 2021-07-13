from ..find_fixed_number import find_fixed_point, find_fixed_point_iterative


def test_find_fixed_number():
    A1 = [-10, -5, 0, 3, 7]
    A2 = [0, 2, 5, 8, 17]
    A3 = [-10, -5, 3, 4, 7, 9]

    assert find_fixed_point(A1) == 3
    assert find_fixed_point(A2) == 0
    assert find_fixed_point(A3) is None

    assert find_fixed_point_iterative(A1) == 3
    assert find_fixed_point_iterative(A2) == 0
    assert find_fixed_point_iterative(A3) is None