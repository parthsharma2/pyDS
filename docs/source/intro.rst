Intro
================================

pyDS is a python module consisting of various data structure and algorithm
implementations.

Usage::

  from pyDS.stack import Stack
  from pyDS.usecase.stack import bracketBalanced, decimalBaseConvert

  stack = Stack()

  stack.push(2)
  stack.push(5)

  print(stack)
  # 2 5

  print(stack.peek())
  # 5

  print(stack.pop())
  # 5

  print(stack.peek())
  # 2
