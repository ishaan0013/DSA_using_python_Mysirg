class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next


class CLL:
    def __init__(self, last=None) -> None:
        self.last = last

    def Is_empty(self):
        return (self.last == None)

    def Insert_start(self, data):
        if (self.last == None):
            n = Node(data, None)
            self.last = n
            n.next = n
        else:
            n = Node(data, self.last.next)
            self.last.next = n

    def Insert_last(self, data):
        if (self.last == None):
            n = Node(data, None)
            self.last = n
            n.next = n
        else:
            n = Node(data, self.last.next)
            self.last.next = n
            self.last = n

    def Search(self, data):
        if (self.last == None):
            print("List is empty!")
        elif (self.last.item == data):
            return self.last
        else:
            temp = self.last.next
            while temp is not self.last:
                if (temp.item == data):
                    return temp
                temp = temp.next
            return None

    def Insert_after(self, data, after):
        if (self.last == None):
            print("List is empty!")
        elif (self.last.next == self.last):
            if (self.last.item == after):
                n = Node(data, self.last)
                self.last.next = n
                self.last = n
            else:
                print("Item not in list!")
        else:
            key_node = self.Search(after)
            if (key_node == None):
                print("Item not in list!")
            else:
                if (self.last.item == after):
                    n = Node(data, self.last.next)
                    self.last.next = n
                    self.last = n
                else:
                    n = Node(data, key_node.next)
                    key_node.next = n

    def Delete_first(self):
        if (self.last == None):
            print('List is empty!')
        elif (self.last.next == self.last):
            self.last = None
        else:
            temp = self.last
            temp.next = temp.next.next

    def Delete_last(self):
        if (self.last == None):
            print("List is empty!")
        elif (self.last.next == self.last):
            self.last = None
        else:
            temp = self.last.next
            while temp.next is not self.last:
                temp = temp.next
            temp.next = self.last.next
            self.last = temp

    def Delete_item(self, data):
        if (self.last == None):
            print("List is empty!")
        elif (self.last.next == self.last):
            if (self.last.item == data):
                self.last = None
        else:
            key_node = self.Search(data)
            if (self.last == key_node):
                temp = self.last.next
                while temp.next is not key_node:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp
            elif (self.last.next == key_node):
                self.last.next = self.last.next.next
            else:
                if (key_node is not None):
                    temp = self.last.next
                    while temp.next is not key_node:
                        temp = temp.next
                    temp.next = temp.next.next
                else:
                    print("Item not in list!")

    def Print(self):
        if (self.last == None):
            print("List is empty!")
        elif (self.last.next == self.last):
            print(self.last.item)
        else:
            temp = self.last.next
            while temp is not self.last:
                print(f"{temp.item}", end=" ")
                temp = temp.next
            print(f"{temp.item}", end=" ")

    def __iter__(self):
        if self.last == None:
            return CLLIteration(None)
        return CLLIteration(self.last.next)


class CLLIteration:
    def __init__(self, start) -> None:
        self.current = start
        self.first = start
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (not self.current):
            raise StopIteration
        if (self.current == self.first and self.count == 1):
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data


mylist = CLL()
mylist.Insert_last(2)
mylist.Insert_last(1)
mylist.Insert_last(3)
mylist.Insert_last(4)
mylist.Insert_start(5)
# mylist.Delete_item(20)

for data in mylist:
    print(data)
