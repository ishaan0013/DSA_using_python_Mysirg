class Stack:
    def __init__(self) -> None:
        self.stk = []

    def Is_empty(self):
        if not self.stk:
            return True
        return False

    def Push(self, data):
        self.stk.append(data)

    def Pop(self):
        if (len(self.stk) != 0):
            return self.stk.pop()
        else:
            raise IndexError("Pop from empty stack")

    def Peek(self):
        if (len(self.stk) != 0):
            print(self.stk[-1])
        else:
            raise IndexError("Peek from empty stack")

    def Size(self):
        print(len(self.stk))


my_stack = Stack()
# print(my_stack.Is_empty())
my_stack.Push(12)
my_stack.Size()
my_stack.Peek()
