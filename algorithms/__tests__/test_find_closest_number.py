from ..find_closest_number import find_closest_num


def test_find_closes_number():
    A1 = [1, 2, 4, 5, 6, 6, 8, 9]
    A2 = [2, 5, 6, 7, 8, 8, 9]
    A3 = []
    A4 = [4]

    assert find_closest_num(A3, 78) == None
    assert find_closest_num(A4, 4) == A4[0]
    assert find_closest_num(A1, 11) == 9
    assert find_closest_num(A2, 4) == 5
