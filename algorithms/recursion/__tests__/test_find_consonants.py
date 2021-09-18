from ..find_consoants import find_consonants_iterative, find_consonants_recursive


class TestFindConsonants:

    test_cases = [
        {
            "input_str": "abc de",
            "res": 3
        },
        {
            "input_str": "LuCiDPrograMMiNG",
            "res": 11
        },
    ]

    def test_find_consonants_iterative(self):
        for i in self.test_cases:
            assert find_consonants_iterative(i['input_str']) == i['res']

    def test_find_uppercase_recursive(self):
        for i in self.test_cases:
            assert find_consonants_recursive(i['input_str']) == i['res']
