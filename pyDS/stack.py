class Stack:
    """An implementation of the stack data structure."""

    def __init__(self):
        """Initialize the Stack."""
        self._items = []

    def __len__(self):
        """Return the size of the Stack."""
        return len(self._items)

    def __str__(self):
        """Return the string representation of the Stack."""
        return ' '.join(self._items)

    def isEmpty(self):
        """Return whether the stack is empty."""
        return self._items == []

    def push(self, item):
        """Add an item to the stack."""
        self._items.append(item)

    def pop(self):
        """Remove an item from the Stack."""
        return self._items.pop()

    def peek(self):
        """Return the top item from the Stack."""
        return self._items[len(self._items) - 1]