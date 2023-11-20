class Deque:
    def __init__(self) -> None:
        self.lst = []

    def Is_empty(self):
        return (not self.lst)

    def Insert_front(self, data):
        self.lst.append(data)

    def Insert_rear(self, data):
        self.lst.insert(0, data)

    def Delete_front(self):
        if not self.Is_empty():
            self.lst.pop()
        else:
            raise IndexError("Empty Deque!")

    def Delete_rear(self):
        if not self.Is_empty():
            self.lst.pop(0)
        else:
            raise IndexError("Empty Deque!")

    def Get_front(self):
        if not self.Is_empty():
            return self.lst[-1]
        else:
            raise IndexError("Empty Deque!")

    def Get_rear(self):
        if not self.Is_empty():
            return self.lst[0]
        else:
            raise IndexError("Empty Deque!")

    def Size(self):
        return len(self.lst)


myDeque = Deque()
# print(myDeque.Is_empty())
print(myDeque.Size())
myDeque.Insert_rear(12)
myDeque.Insert_front(100)
myDeque.Insert_rear(13)
myDeque.Insert_rear(14)
myDeque.Insert_rear(15)
print(myDeque.Get_front())
print(myDeque.Get_rear())
print(myDeque.Size())
