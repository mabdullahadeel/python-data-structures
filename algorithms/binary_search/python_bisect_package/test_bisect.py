import bisect

class TestBisect:
    def test_bisect_left(self):
        A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        # -10 is at index 1
        assert bisect.bisect_left(A, -10) == 1
        # First occurrence of 285 is at index 6
        assert bisect.bisect_left(A, 285) == 6

    def test_bisect_right(self):
        A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        # Index position to right of -10 is 2.
        assert bisect.bisect_right(A, -10) == 2

        # Index position after last occurrence of 285 is 9.
        assert bisect.bisect_right(A, 285) == 9

    def test_bisect(self):
        A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        # Index position to right of -10 is 2.
        assert bisect.bisect(A, -10) == 2

        # Index position after last occurrence of 285 is 9.
        assert bisect.bisect(A, 285) == 9

    def test_insort_left(self):
        """
            functions same as `bisect_left` except it insert at the index positions
        """
        A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        # operation
        bisect.insort_left(A, 108)
        assert  A == [-14, -10, 2, 108, 108, 108, 243, 285, 285, 285, 401]

        # operation
        bisect.insort_right(A, 108)
        assert A == [-14, -10, 2, 108, 108, 108, 108, 243, 285, 285, 285, 401]
