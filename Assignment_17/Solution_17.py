class Node:
    def __init__(self, item=None, next=None, priority=0) -> None:
        self.item = item
        self.next = next
        self.priority = priority


class PriorityQueue:
    def __init__(self) -> None:
        self.start = None
        self.count = 0

    def Is_empty(self):
        return (self.start == None)

    def Push(self, data, pri):
        self.count += 1
        n = Node(data, None, pri)
        if not self.start or (self.start.priority > pri):
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= pri:
                temp = temp.next
            n.next = temp.next
            temp.next = n

    def Pop(self):
        if self.Is_empty():
            raise IndexError("Queue is Empty!")
        else:
            a = self.start.item
            self.start = self.start.next
            self.count -= 1
            return a

    def Size(self):
        return self.count


myQueue = PriorityQueue()
# print(myQueue.Is_empty())
myQueue.Push(13, 7)
myQueue.Push(15, 3)
myQueue.Push(18, 5)
myQueue.Push(1, 12)
myQueue.Push(23, 1)
myQueue.Push(67, 19)
myQueue.Push(89, 11)
myQueue.Push(90, 6)
myQueue.Push(1, 10)
print(myQueue.Pop())
print(myQueue.Pop())
print(myQueue.Pop())
print(myQueue.Pop())
print(myQueue.Is_empty())
print(myQueue.Size())
# print(myQueue.Pop())
# print(myQueue.Size())
# print(myQueue.Pop())
