from helper import is_operator, get_precedence
from structure.node import Node
from structure.stack import Stack


def in_tree(infix: str) -> Node:
    """function to make expression tree of an infix expression"""

    char_stack = Stack()
    node_stack = Stack()
    unique_ID = 0
    print("Tree: ")
    for char in infix:
        # push ( to the char stack
        if char == '(':
            char_stack.push(char)

        # push operand to the node stack
        elif char.isalpha():
            unique_ID += 1
            node_stack.push(Node(char, id=unique_ID))

        # push operator to char stack if it hasz higher precedence than the last element in char stack
        elif is_operator(char) and get_precedence(char) > 0:
            while not char_stack.is_empty() and char_stack.peek() != '(' and (
                    (char != '^' and get_precedence(char_stack.peek()) >= get_precedence(char)) or
                    (char == '^' and get_precedence(char_stack.peek()) > get_precedence(char))):
                unique_ID += 1
                right = node_stack.pop()
                left = node_stack.pop()
                node = Node(char_stack.pop(), left, right, id=unique_ID)
                node_stack.push(node)

                print("parent is: " + str(node.data) + " left child is: " + str(left) + " right child is: " + str(
                    right))

            char_stack.push(char)

        # pop 2 elements from node stack and make new node with the last element in char stack
        elif char == ')':
            while not char_stack.is_empty() and (char_stack.peek() != '('):
                right = node_stack.pop()
                left = node_stack.pop()

                unique_ID += 1
                node = Node(char_stack.pop(), left, right, id=unique_ID)

                print("parent is: " + str(node.data) + " left child is: " + str(left) + " right child is: " + str(
                    right))

                node_stack.push(node)
            char_stack.pop()

    # empty the char stack if it has operators in it
    while not char_stack.is_empty():
        right = node_stack.pop()
        left = node_stack.pop()

        unique_ID += 1
        node = Node(char_stack.pop(), left, right, id=unique_ID)
        node_stack.push(node)
        print("parent is: " + str(node.data) + " left child is: " + str(left) + " right child is: " + str(
            right))

    print(" ")
    return node_stack.pop()


def postorder(root: Node) -> None:
    """function to write the postfix expression of a tree"""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end="")


def preorder(root: Node) -> None:
    """function to write the prefix expression of a tree"""
    if root:
        print(root.data, end=""),
        preorder(root.left)
        preorder(root.right)


def inorder(root: Node) -> None:
    """inorder traversal of a tree to get infix expression"""
    if root:
        inorder(root.left)
        print(root.data),
        inorder(root.right)
