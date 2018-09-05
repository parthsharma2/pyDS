from ..stack import Stack


def bracketBalanced(expression):
    """Check if an expression is balanced.

    An expression is balanced if all the opening brackets(i.e. '(, {, [') have
    a corresponding closing bracket(i.e. '), }, ]').

    Args:
        expression (str) : The expression to be checked.

    Returns:
        bool: True if expression is balanced. False if not balanced.

    """
    bracket_dict = {'(': ')', '{': '}', '[': ']'}

    stack = Stack()

    for i in range(len(expression)):
        if expression[i] in bracket_dict.keys():
            stack.push(expression[i])
        elif expression[i] in bracket_dict.values():
            if stack.isEmpty() or expression[i] != bracket_dict[stack.peek()]:
                return False
            else:
                stack.pop()

    if stack.isEmpty():
        return True
    else:
        return False


def decimalBaseConvert(number, base=2):
    """Convert decimal numbers.

    Convert the base of a decimal number to another base.

    Args:
        number (int): The number to be converted.
        base (int, optional): The base to convert the number to.
            Defaults to 2. Minimum value 2. Maximum value 16.

    Returns:
        str: The string representation of the converted number.

    """
    if base < 2 or base > 16:
        raise ValueError("Invalid Base Value: Expected value between 2 and 16")

    if number == 0:
        return '0'

    stack = Stack()

    digits = "0123456879ABCDEF"

    while number > 0:
        stack.push(number % base)
        number = number // base

    converted_number = ""
    while not stack.isEmpty():
        converted_number += digits[stack.pop()]

    return converted_number
