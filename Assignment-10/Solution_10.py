from Copy_of_assg3 import *


class Stack:
    def __init__(self) -> None:
        self.myStack = SLL()
        self.count = 0

    def Is_empty(self):
        return self.myStack.is_empty()

    def push(self, data):
        self.myStack.Insert_start(data)
        self.count += 1

    def pop(self):
        if self.myStack.is_empty():
            raise IndexError("Pop from empty Stack!")
        else:
            n = self.myStack.start.item
            self.myStack.Delete_first()
            self.count -= 1
            return n

    def Peek(self):
        if self.myStack.is_empty():
            raise IndexError("Peek from empty Stack!")
        else:
            return (self.myStack.start.item)

    def Size(self):
        return self.count


my_stack = Stack()
my_stack.push(3)
# my_stack.push(4)
my_stack.push(5)
# my_stack.push(6)
print(my_stack.pop())
print(my_stack.Size())
print(my_stack.Peek())
