#!/usr/bin/env python3

class CountedIterator:
    """
    An iterator wrapper that keeps track of the number of items iterated.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and a counter.
        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the current count of iterated items."""
        return self.count

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the counter.
        Raises StopIteration if no more items are available.
        """
        try:
            # Orijinal iteratordan növbəti elementi alırıq
            item = next(self.iterator)
            # Əgər element varsa (StopIteration baş vermədisə), sayğacı artırırıq
            self.count += 1
            return item
        except StopIteration:
            # Əgər element bitibsə, StopIteration xətasını olduğu kimi ötürürük
            raise StopIteration

    def __iter__(self):
        """Ensures the CountedIterator itself is also an iterable."""
        return self
