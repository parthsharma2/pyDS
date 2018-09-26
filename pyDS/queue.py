
class Queue:
    """An implementation of the Queue data strucutre."""

    def __init__(self):
        self._items = []

    def __repr__(self):
        return "pyDS.queue.Queue({})".format(self._items)

    def __str__(self):
        return str(self._items)

    def __len__(self):
        return len(self._items)

    def is_empty(self):
        """Check queue is empty.

        Returns:
            True if Queue is empty, False otherwise.

        """
        return self._items == []

    def enqueue(self, item):
        """Add item to Queue.

        Args:
            item: The item to be inserted.

        """
        self._items.append(item)

    def dequeue(self):
        """Remove item from queue.

        Returns:
            The first item from the Queue. Raises IndexError if Queue empty.

        """
        if not self.is_empty():
            return self._items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        """Return the first Queue item.

        Returns:
            The first item from the Queue. Raises IndexError if Queue empty.

        """
        if not self.is_empty():
            return self._items[0]
        else:
            return IndexError("Queue is empty")

    def rear(self):
        """Return the last Queue item.

        Returns:
            The last item from the Queue. Raises IndexError if Queue empty.

        """
        if not self.is_empty():
            return self._items[-1]
        else:
            return IndexError("Queue is empty")
