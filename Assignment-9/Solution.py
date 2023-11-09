class _Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next


class Stack:
    def __init__(self) -> None:
        self.start = None

    def Item_count(self):
        count = None
        if (self.start == None):
            return count
        elif (self.start.next == None):
            return 1
        else:
            count = 0
            temp = self.start
            while temp.next is not None:
                temp = temp.next
                count = count+1
            return (count+1)

    def Is_empty(self):
        return self.start == None

    def Push(self, data):
        n = _Node(data, self.start)
        self.start = n

    def Pop(self):
        if self.start != None:
            n = self.start.item
            self.start = self.start.next
            return n
        else:
            raise IndexError("Pop from empty Stack!")

    def Peek(self):
        if self.start != None:
            return self.start.item
        else:
            raise IndexError("Peek from empty Stack!")

    def Size(self):
        return self.Item_count()


myStack = Stack()
myStack.Push(1)
myStack.Push(2)
myStack.Pop()
print(myStack.Size())
