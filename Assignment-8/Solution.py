class Stack(list):
    def Is_empty(self):
        return len(self) == 0

    def Push(self, data):
        self.append(data)

    def Pop(self):
        if not self.Is_empty():
            return super().pop()
        else:
            raise IndexError("Pop from empty stack!")

    def Peek(self):
        if not self.Is_empty():
            return self[-1]
        else:
            raise IndexError("Peek from empty stack!")

    def Size(self):
        return len(self)

    def insert(self, idx, data):
        raise AttributeError("Can not insert in Stack")


s1 = Stack()
s1.Push(12)
s1.Push(13)
s1.Push(14)
# s1.insert()
print(s1.Size())
