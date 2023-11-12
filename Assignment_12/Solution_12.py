class Queue:
    def __init__(self) -> None:
        self.lst = []

    def Is_empty(self):
        return (not self.lst)

    def Enqueue(self, data):
        self.lst.insert(0, data)

    def Dequeue(self):
        if not self.Is_empty():
            return self.lst.pop()
        else:
            raise IndexError("Dequeue from empty Queue!")

    def Get_front(self):
        if not self.Is_empty():
            return self.lst[-1]
        else:
            raise IndexError("Empty Queue!")

    def Get_rear(self):
        if not self.Is_empty():
            return self.lst[0]
        else:
            raise IndexError("Empty Queue!")

    def Size(self):
        return len(self.lst)


myQueue = Queue()
myQueue.Enqueue(12)
myQueue.Enqueue(13)
myQueue.Enqueue(14)
myQueue.Enqueue(15)
print(myQueue.Dequeue())
print(myQueue.Size())
print(myQueue.Get_rear())
print(myQueue.Get_front())
print(myQueue.Is_empty())
