from ..find_first_ent_with_duplicates import find_first_ent_with_duplicates


def test_find_first_element_with_duplicate():
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 108

    assert find_first_ent_with_duplicates(array=A, target=target) == 3