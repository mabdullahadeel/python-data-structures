from ..balancedBracketAlgo import are_parenthesis_balanced


def test_brackets_are_balanced():
	test_paren_str = "{({([])})}"

	assert are_parenthesis_balanced(test_paren_str) == True


def test_brackets_are_not_balanced():
	test_paren_str = "{({)})}"

	assert are_parenthesis_balanced(test_paren_str) == False