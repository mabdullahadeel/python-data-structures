from ..optimalTaskAssignment import optimal_task_assignment


def test_optimal_task_assignment():
    test_array = [6, 3, 2, 7, 5, 5]
    test_output = [(2, 7), (3, 6), (5, 5)]
    assert optimal_task_assignment(tasks_time_array=test_array) == test_output