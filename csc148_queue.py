"""
queue implementation
"""


class Queue:
    """
    A first-in, first-out (FIFO) queue.
    """

    def __init__(self) -> None:
        """
        Create and initialize new Queue self.

        >>> q = Queue()
        """
        self._queue = []

    def add(self, obj: object) -> None:
        """
        Add object at the back of Queue self.

        >>> q = Queue()
        >>> q.add(7)
        """
        self._queue.append(obj)

    def remove(self) -> object:
        """
        Remove and return front object from Queue self.

        Queue self must not be empty.

        >>> q = Queue()
        >>> q.add(3)
        >>> q.add(5)
        >>> q.remove()
        3
        """
        return self._queue.pop(0)

    def is_empty(self) -> bool:
        """
        Return whether Queue self is empty

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        >>> q.remove()
        5
        >>> q.is_empty()
        True
        """
        return len(self._queue) == 0

    def __str__(self) -> str:
        """
        Return a string representation of Stack self that has the top most
        item
        >>> s = Queue()
        >>> s.add(5)
        >>> s.add(7)

        >>> print(s)
        Top element is 5
        """
        return 'Top element is {}'.format(self._queue[0])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
