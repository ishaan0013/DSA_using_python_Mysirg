class priorityQueue:
    def __init__(self) -> None:
        self.lst = []

    def Is_empty(self):
        return (not self.lst)

    def Push(self, data, pri: int):
        self.lst.insert(pri-1, data)

    def Pop(self):
        if not self.Is_empty():
            return self.lst.pop(0)
        else:
            raise IndexError("Empty Queue!")

    def Size(self):
        return len(self.lst)


myQueue = priorityQueue()
myQueue.Push(12, 1)
myQueue.Push(13, 2)
myQueue.Push(14, 1)
myQueue.Push(15, 6)
print(myQueue.Size())
print(myQueue.Pop())
