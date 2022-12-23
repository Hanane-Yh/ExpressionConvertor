from expression_tree import *
from helper import infix, find_expression
from visualize import show_graph


def main():

    expression = input("Enter an expression: ")
    identifier = find_expression(expression)

    if identifier == "INFIX":
        root = in_tree(expression)
        print("Postfix: ", end="")
        postorder(root)
        print(" ")
        print("Prefix: ", end="")
        preorder(root)

    elif identifier == "PREFIX":
        infix_expression = infix(expression, identifier)
        root = in_tree(infix_expression)
        print("Infix: " + infix_expression)
        print("Postfix: ", end="")
        postorder(root)

    elif identifier == "POSTFIX":
        infix_expression = infix(expression, identifier)
        root = in_tree(infix_expression)
        print("Infix: " + infix_expression)
        print("Prefix: ", end="")
        preorder(root)

    print("\nYour expression: " + expression)
    print("Expression type: " + identifier)
    show_graph(root)


if __name__ == '__main__':
    main()
