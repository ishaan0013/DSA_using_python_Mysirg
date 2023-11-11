from Copy_of_assg3 import *


class Stack(SLL):
    def __init__(self) -> None:
        self.start = None
        self.count = 0

    def is_empty(self):
        return super().is_empty()

    def Push(self, data):
        self.Insert_start(data)
        self.count += 1

    def Pop(self):
        if (self.start != None):
            n = self.start.item
            self.Delete_first()
            self.count -= 1
            return n
        else:
            raise IndexError("Pop from empty Stack!")

    def Peek(self):
        if (self.start != None):
            return self.start.item
        else:
            raise IndexError("Peek from Empty Stack")

    def Size(self):
        return self.count


mystack = Stack()
mystack.Push(2)
mystack.Push(3)
mystack.Push(4)
mystack.Push(5)
print(mystack.Pop())
print(mystack.Size())
