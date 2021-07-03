"""
    The function here solves the given problem:

    Assign tasks to workers so that the time it takes to
    complete all the tasks is minimized given a count of
    workers and an array where each element indicates the
    duration of a task.

    Assumptions:
        - We wish to determine the optimal way in which
        to assign tasks to some workers. Each worker must
        work on exactly two tasks. Tasks are independent
        of each other, and each task takes a certain amount
        of time
        - Each worker can at most take two tasks

    APPROACH:
        I this algorithm, the greedy approach has been taken
        which states that:
            - Pais the longest taking task to the shortest one
"""


def optimal_task_assignment(tasks_time_array):
    tasks_time_array = sorted(tasks_time_array)
    res_list = list()
    for i in range(len(tasks_time_array)//2):
        res_list.append((tasks_time_array[i], tasks_time_array[~i]))

    return res_list