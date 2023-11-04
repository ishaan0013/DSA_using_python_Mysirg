class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.prev = prev
        self.item = item
        self.next = next


class CDLL:
    def __init__(self, start=None) -> None:
        self.start = start

    def Is_empty(self):
        return (self.start == None)

    def Insert_start(self, data):
        if (self.start == None):
            n = Node(None, data, None)
            self.start = n
            n.next, n.prev = n, n
        else:
            n = Node(self.start.prev, data, self.start)
            self.start.prev.next = n
            self.start.prev = n
            self.start = n

    def Insert_last(self, data):
        if (self.start == None):
            n = Node(None, data, None)
            self.start = n
            n.next, n.prev = n, n
        else:
            n = Node(self.start.prev, data, self.start)
            self.start.prev.next = n
            self.start.prev = n

    def Search(self, data):
        if (self.start == None):
            print("List is empty!")
        elif (self.start.item == data):
            return self.start
        else:
            temp = self.start.next
            while temp is not self.start:
                if (temp.item == data):
                    return temp
                temp = temp.next
            return None

    def Insert_after(self, data, after):
        if (self.start == None):
            print("List is Empty!")
        elif (self.start.prev.item == after):
            n = Node(self.start.prev, data, self.start)
            self.start.prev.next = n
            self.start.prev = n
        else:
            key_node = self.Search(after)
            if (key_node is not None):
                n = Node(key_node, data, key_node.next)
                key_node.next.prev = n
                key_node.next = n
            else:
                print("Value not in list!")

    def Delete_first(self):
        if (self.start == None):
            print("List is empty!")
        elif (self.start.next == self.start):
            self.start = None
        else:
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next

    def Delete_last(self):
        if (self.start == None):
            print("List is empty!")
        elif (self.start.next == self.start):
            self.start = None
        else:
            self.start.prev.prev.next = self.start
            self.start.prev = self.start.prev.prev

    def Delete_item(self, data):
        if (self.start == None):
            print("List is empty!")
        else:
            key_node = self.Search(data)
            if (key_node is not None):
                if (self.start == key_node):
                    self.Delete_first()
                elif (self.start.prev == key_node):
                    self.Delete_last()
                else:
                    key_node.prev.next = key_node.next
                    key_node.next.prev = key_node.prev
            else:
                print("Value not in list!")

    def Print(self):
        if (self.start == None):
            print("Empty List!")
        else:
            temp = self.start
            while temp is not self.start.prev:
                print(f"{temp.item}", end=" ")
                temp = temp.next
            print(f"{temp.item}", end=" ")

    def __iter__(self):
        return CDLLIterator(self.start)


class CDLLIterator:
    def __init__(self, start) -> None:
        self.current = start
        self.temp = start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.current is None or self.current.next is self.temp):
            print(self.current.item)
            raise StopIteration
        else:
            data = self.current.item
            self.current = self.current.next
            return data


mylist = CDLL()
mylist.Insert_start(6)
mylist.Insert_start(5)
mylist.Insert_start(4)
mylist.Insert_start(7)
mylist.Insert_last(0)
mylist.Insert_last(12)
mylist.Insert_last(13)
mylist.Insert_last(1)
# mylist.Insert_after(14, 5)
# mylist.Delete_last()
# mylist.Delete_item(6)

# mylist.Print()

for data in mylist:
    print(data)
