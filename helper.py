from structure.stack import Stack


def find_expression(exp: str) -> str:
    """determines the type of given expression"""
    if exp[0].isalpha() and is_operator(exp[-1]):
        return "POSTFIX"
    elif is_operator(exp[0]) and exp[-1].isalpha():
        return "PREFIX"
    else:
        return "INFIX"


def is_operator(c: str) -> bool:
    """function to check if the given char is an operator"""
    return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'


def get_precedence(c: str) -> int:
    """function to set each operator's precedence"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, ')': 0}
    return precedence.get(c)


def infix(exp: str, identifier: str) -> str:
    """converts expression from either postfix or prefix to infix (using the expression itself)"""
    stack = Stack()
    if identifier == "PREFIX":
        for i in exp[::-1]:
            if i.isalpha():
                stack.push(i)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.push('(' + val1 + i + val2 + ')')
    elif identifier == "POSTFIX":
        for i in exp:
            if i.isalpha():
                stack.push(i)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.push('(' + val2 + i + val1 + ')')
    return stack.pop()
