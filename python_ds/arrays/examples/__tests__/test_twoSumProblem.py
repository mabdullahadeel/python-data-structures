from ..twoSumProblem import TwoSumProblem


def test_two_sum_problem_brute_force():
    test_array = [-2, 1, 2, 4, 7, 11]

    # Positive Case
    target = 13
    tsp = TwoSumProblem(array=test_array, target=target)
    assert tsp.two_sum_brute_force()

    # Negative  Case
    target2 = 20
    tsp2 = TwoSumProblem(array=test_array, target=target2)
    assert not tsp2.two_sum_brute_force()


def test_two_sum_problem_hash_table():
    test_array = [-2, 1, 2, 4, 7, 11]
    target = 13
    tsp = TwoSumProblem(array=test_array, target=target)

    assert tsp.two_sum_hash_table()


def test_two_sum_problem_both_ways_track():
    test_array = [-2, 1, 2, 4, 7, 11]
    target = 13

    tsp = TwoSumProblem(array=test_array, target=target)
    assert tsp.two_sum_both_ways_track()
