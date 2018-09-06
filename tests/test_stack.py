from pyDS.stack import Stack
import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_empty_stack(self):
        self.assertTrue(self.stack.isEmpty())

    def test_stack_push(self):
        self.stack.push(2)
        self.assertEqual(self.stack._items, [2])

    def test_non_empty_stack(self):
        self.stack.push(5)
        self.assertFalse(self.stack.isEmpty())

    def test_stack_length(self):
        self.stack.push(2)
        self.assertEqual(len(self.stack), 1)

    def test_stack_peek(self):
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)

    def test_stack_pop(self):
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)

    def test_empty_stack_pop(self):
        with self.assertRaises(ValueError):
            self.stack.pop()

    def test_empty_stack_peek(self):
        with self.assertRaises(ValueError):
            self.stack.peek()

    def test_stack_str_representation(self):
        self.stack.push(2)
        self.stack.push(4)
        self.assertEqual(str(self.stack),"2 4")
