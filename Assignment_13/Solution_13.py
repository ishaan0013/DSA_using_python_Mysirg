class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.start = None
        self.count = 0

    def Is_empty(self):
        return (self.start == None)

    def Enqueue(self, data):
        n = Node(data, self.start)
        self.start = n
        self.count += 1

    def Dequeue(self):
        if not self.Is_empty():
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            self.count -= 1
        else:
            raise IndexError("Empty Queue!")

    def get_rear(self):
        if not self.Is_empty():
            return self.start.item
        else:
            raise IndexError("Empty Queue!")

    def get_front(self):
        if not self.Is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            raise IndexError("Empty Queue!")

    def Size(self):
        return self.count


myQueue = Queue()
myQueue.Enqueue(1)
myQueue.Enqueue(2)
myQueue.Enqueue(3)
myQueue.Enqueue(4)
myQueue.Enqueue(5)
myQueue.Dequeue()
print(myQueue.get_front())
print(myQueue.get_rear())
print(myQueue.Size())
