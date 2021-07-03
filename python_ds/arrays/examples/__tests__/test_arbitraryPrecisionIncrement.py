from ..arbitraryPrecisionIncrement import plus_one


def test_plus_one():
    test_num_array = [1, 4, 9]
    test_output = [1, 5, 0]

    assert plus_one(test_num_array) == test_output