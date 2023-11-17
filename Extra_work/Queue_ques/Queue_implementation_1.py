# By Extending "List" Class
class Queue(list):
    def __init__(self):
        self.myList = []
        self.count = 0

    def Is_empty(self):
        return (not self.myList)

    def Enqueue(self, data):
        self.myList.insert(0, data)
        self.count += 1

    def Dequeue(self):
        if not self.Is_empty():
            self.count -= 1
            return self.myList.pop()
        else:
            raise IndexError("Empty Queue!")

    def Get_front(self):
        if not self.Is_empty():
            return self.myList[-1]
        else:
            raise IndexError("Empty Queue!")

    def Get_rear(self):
        if not self.Is_empty():
            return self.myList[0]
        else:
            raise IndexError('Queue Empty!')

    def Size(self):
        return self.count


MyQueue = Queue()
MyQueue.Enqueue(1)
MyQueue.Enqueue(2)
MyQueue.Enqueue(3)
MyQueue.Enqueue(4)
print(MyQueue.Size())
print(MyQueue.Dequeue())
print(MyQueue.Size())
