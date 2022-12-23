class Stack:
    def __init__(self) -> None:
        self.stack = []

    def __iter__(self):
        return self

    def is_empty(self) -> bool:
        """checks if stack is empty"""
        return len(self.stack) == 0

    def get_length(self) -> int:
        """returns the length of the stack"""
        return len(self.stack)

    def push(self, item):
        """appends the given item to the end of the stack"""
        self.stack.append(item)

    def pop(self):
        """removes the item at the end of the stack"""
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        """returns the item in the last index"""
        if not self.is_empty():
            return self.stack[-1]

    def reverse(self):
        """reverses the stack"""
        return self.stack[::-1]

    def next(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise StopIteration
