from ..integer_square_root import integer_square_root

def test_integer_square_root():
    test_data = {
        300: 17,
        12: 3,
        1000: 31,
        625: 25
    }

    for i in test_data:
        assert integer_square_root(k=i) == test_data[i]