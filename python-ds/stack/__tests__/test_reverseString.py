from ..reverseString import reverse_string

def test_reverse_string():
    test_str = "Hello Stack"
    res = reverse_string(test_str)
    assert res == test_str[::-1]