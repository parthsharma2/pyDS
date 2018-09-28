
class Node():
    """Building Block of Linked List."""

    def __init__(self, data):
        """Initialize Node.

        Args:
            data: The data to be stored.

        """
        self.data = data
        self.next = None

    def __str__(self):
        """String representation of Node."""
        return "({}, {})".format(self.data, self.next)

    def __repr__(self):
        """Representation of Node."""
        return "pyDS.linked_list.Node({}, {})".format(self.data, self.next)


class LinkedList():
    """An implementation of the Linked List data structure."""

    def __init__(self):
        """Initialize Linked List."""
        self.head = None

    def __repr__(self):
        """Representation of Linked List."""
        return "pyDS.linked_list.LinkedList({})".format(self.head)

    def __iter__(self):
        """Iterate through the Linked List.

        Returns:
            Generator object.

        """
        ptr = self.head
        while (ptr):
            yield ptr.data
            ptr = ptr.next

    def __reversed__(self):
        """Reverse the Linked List."""
        self.reverse()

    def push(self, item):
        """Add item to the front of the Linked List.

        Args:
            item: The item to be inserted.

        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def append(self, item):
        """Add item to the end of the Linked List.

        Args:
            item: The item to be inserted.

        """
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            return

        ptr = self.head
        while (ptr.next):
            ptr = ptr.next

        ptr.next = new_node

    def delete(self, item):
        """Delete an item from the Linked List."""
        if self.head is None:
            raise IndexError('Empty Linked List')
        elif self.head.data == item:
            self.head = self.head.next
            return

        temp = self.head
        prev = None

        while (temp):
            if temp.data == item:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            raise ValueError('Item {} not in Linked List'.format(item))
        else:
            prev.next = temp.next

    def reverse(self):
        """Reverse the items of the Linked List."""
        current_ptr = self.head
        prev_ptr = None
        while current_ptr:
            next_ptr = current_ptr.next
            current_ptr.next = prev_ptr
            prev_ptr = current_ptr
            current_ptr = next_ptr
        self.head = prev_ptr
