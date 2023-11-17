# Using previous SLL class through Inheritance
from Copy_of_assign3 import *


class Queue(SLL):
    def __init__(self, start=None) -> None:
        self.count = 0
        super().__init__(start)

    def Enqueue(self, data):
        super().Insert_start(data)
        self.count += 1

    def Dequeue(self):
        if not super().is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            a = temp.item
            super().Delete_last()
            self.count -= 1
            return a
        else:
            raise IndexError("Empty Queue!")

    def Get_rear(self):
        if not super().is_empty():
            return self.start.item
        else:
            raise IndexError("Empty Queue!")

    def Get_front(self):
        if not super().is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            raise IndexError("Empty Queue")

    def Size(self):
        return self.count


myQueue = Queue()
myQueue.Enqueue(1)
myQueue.Enqueue(2)
myQueue.Enqueue(3)
myQueue.Enqueue(4)
myQueue.Enqueue(5)
print(myQueue.Size())
print(myQueue.Dequeue())
print(myQueue.Size())
