from ..queue import Queue


class TestQueue:
    def test_enqueue(self):
        queue = Queue()
        test_samples = [1, 2, 3]
        for i in test_samples:
            queue.enqueue(i)

        assert queue.items == test_samples[::-1]


    def test_dequeue(self):
        queue = Queue()
        test_samples = [1, 2, 3]
        for i in test_samples:
            queue.enqueue(i)

        queue.dequeue()

        assert queue.items == test_samples[::-1][:-1]


    def test_is_empty(self):
        queue = Queue()
        test_samples = [1, 2, 3]

        for i in test_samples:
            queue.enqueue(i)

        assert not queue.is_empty()

        for _ in range(queue.size()):
            queue.dequeue()
        print(queue.items)
        assert queue.is_empty()


    def test_peek(self):
        queue = Queue()
        test_samples = [1, 2, 3]

        for i in test_samples:
            queue.enqueue(i)

        assert queue.peek() == test_samples[0]


    def test_size(self):
        queue = Queue()
        test_samples = [1, 2, 3]

        for i in test_samples:
            queue.enqueue(i)

        assert queue.size() == len(test_samples)