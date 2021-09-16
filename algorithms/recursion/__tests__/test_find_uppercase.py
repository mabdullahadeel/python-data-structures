from ..find_uppercase import find_uppercase_recusive, find_uppercase_iterative


class TestFindUpperCase(object):

    test_inputs = [
            {
                "input_str":"thIs is some test string",
                "exp_result": ("I", 2)
            },
            {
                "input_str":"nothing",
                "exp_result": (None, None)
            },
            {
                "input_str":"Test",
                "exp_result": ("T", 0)
            },
        ]

    def test_find_uppercase_recursive(self):
        for test_input in self.test_inputs:
            assert find_uppercase_recusive(test_input["input_str"]) == test_input["exp_result"]
    
    
    def test_find_uppercase_iterative(self):
        for test_input in self.test_inputs:
            assert find_uppercase_iterative(test_input["input_str"]) == test_input["exp_result"]