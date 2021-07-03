from ..arrayAdvanceGame import array_advance

def test_array_advance_success():
    test_array = [3, 3, 1, 0, 2, 0, 1]
    assert array_advance(test_array)


def test_array_advance_unwinnable():
    test_array = [3, 2, 0, 0, 2, 0, 1]
    assert not array_advance(test_array)