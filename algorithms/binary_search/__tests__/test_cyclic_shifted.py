from ..cyclically_shifted_array import find

def test_cyclically_shifted_array():
    test_data = {
        4: [4, 5, 6, 7, 1, 2, 3],
        2: [6, 7, 1, 2, 3, 4, 5],
        1: [7, 1, 2, 3, 4, 5, 6],
        0: [1, 2, 3, 4, 5, 6, 7],
        5: [3, 4, 5, 6, 7, 1, 2],
        6: [2, 3, 4, 5, 6, 7, 1],
        3: [5, 6, 7, 1, 2, 3, 5],
    }

    for i in test_data:
        assert find(A=test_data[i]) == i