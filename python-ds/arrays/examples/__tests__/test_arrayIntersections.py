from ..arrayIntersection import intersect_soted_arrays


def test_array_intersections():
    array1 = [2, 3, 3, 5, 7, 11]
    array2 = [3, 3, 7, 15, 31]
    output_expect = [3, 7]

    assert intersect_soted_arrays(array1=array1, array2=array2) == output_expect