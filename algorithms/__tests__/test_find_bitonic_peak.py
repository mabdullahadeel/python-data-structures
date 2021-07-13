from ..find_bitonic_peak import find_bitonic_peak

def test_find_bitonic_peak():
    A1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    A2 = [1, 6, 5, 4, 3, 2, 1]
    A3 = [1, 2, 3, 4, 5]
    A4 = [5, 4, 3, 2, 1]

    assert find_bitonic_peak(A1) == 5
    assert find_bitonic_peak(A2) == 6
    assert find_bitonic_peak(A3) is None
    assert find_bitonic_peak(A4) == 5