class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.prev = prev
        self.item = item
        self.next = next


class Deque:
    def __init__(self) -> None:
        self.start = None
        self.count = 0

    def Is_empty(self):
        return (self.start == None)

    def Insert_rear(self, data):
        self.count += 1
        if not self.Is_empty():
            n = Node(None, data, self.start)
            self.start.prev = n
        else:
            n = Node(None, data, None)
        self.start = n

    def Insert_front(self, data):
        self.count += 1
        if not self.Is_empty():
            if (self.start.next == None):
                n = Node(self.start, data, None)
                self.start.next = n
            else:
                temp = self.start
                while temp.next is not None:
                    temp = temp.next
                n = Node(temp, data, None)
                temp.next = n
        else:
            n = Node(None, data, None)
            self.start = n

    def Delete_rear(self):
        if not self.Is_empty():
            if (self.start.next == None):
                self.start = None
            else:
                self.start.next.prev = None
                self.start = self.start.next
            self.count -= 1
        else:
            raise IndexError("Empty Deque!")

    def Delete_front(self):
        if not self.Is_empty():
            if (self.start.next == None):
                self.start = None
            else:
                temp = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None
            self.count -= 1
        else:
            raise IndexError("Empty Deque!")

    def Get_rear(self):
        if not self.Is_empty():
            return (self.start.item)
        else:
            raise IndexError("Empty Deque!")

    def Get_front(self):
        if not self.Is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return (temp.item)
        else:
            raise IndexError("Empty Deque!")

    def Size(self):
        return self.count


myDeque = Deque()
print(myDeque.Size())
myDeque.Insert_front(12)
myDeque.Insert_front(13)
myDeque.Insert_front(14)
myDeque.Insert_rear(15)
myDeque.Insert_rear(16)
myDeque.Insert_rear(17)
print(myDeque.Size())
print(myDeque.Get_front())
print(myDeque.Get_rear())

myDeque.Delete_front()
myDeque.Delete_rear()

print(myDeque.Get_rear())
print(myDeque.Get_front())
