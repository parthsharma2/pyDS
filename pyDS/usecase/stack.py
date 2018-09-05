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
