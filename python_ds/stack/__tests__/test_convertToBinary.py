from ..convertToBinary import convert_to_binary

def test_func_give_valid_binary_output():
    test_int = 60
    result = convert_to_binary(test_int)
    assert result == 111100