class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.item = item
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self, start=None) -> None:
        self.start = start

    def Is_empty(self):
        return (self.start == None)

    def Insert_start(self, data):
        n = Node(None, data, self.start)
        if (self.start == None):
            self.start = n
        else:
            self.start.prev = n
            self.start = n

    def Insert_last(self, data):
        if (self.start == None):
            n = Node(None, data, None)
            self.start = n
        else:
            temp = self.start
            while temp is not None:
                ref = temp
                temp = temp.next
            n = Node(ref, data, None)
            ref.next = n

    def Search(self, data):
        temp = self.start
        while temp is not None:
            if (temp.item == data):
                return temp
            temp = temp.next
        return None

    def Insert_after(self, data, after):
        if (self.Search(after) == None):
            print("Either list is empty or the value is not in list!")
        else:
            temp = self.Search(after)
            if (temp.next == None):
                n = Node(temp, data, None)
                temp.next = n
            else:
                n = Node(temp, data, temp.next)
                temp.next.prev = n
                temp.next = n

    def Delete_first(self):
        if (self.start == None):
            print("List is empty!")
        elif (self.start.next == None):
            self.start = None
        else:
            self.start = self.start.next
            self.start.prev = None

    def Delete_last(self):
        if (self.start == None):
            print('List is empty!')
        elif (self.start.next == None):
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def Delete_item(self, data):
        if (self.Search(data) == None):
            print("Item not in list or list is empty!")
        else:
            if (self.start.item == data):
                self.start = None
            else:
                key_node = self.Search(data)
                if (key_node.next == None):
                    key_node.prev.next = None
                else:
                    key_node.prev.next = key_node.next
                    key_node.next.prev = key_node.prev

    def Print_list(self):
        if (self.start == None):
            print("List is empty!")
        else:
            temp = self.start
            while temp is not None:
                print(f"{temp.item}", end=" ")
                temp = temp.next

    def __iter__(self):
        return DLLIteration(self.start)


class DLLIteration:
    def __init__(self, start) -> None:
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


mylist = DLL()
mylist.Insert_start(10)
mylist.Insert_start(4)
mylist.Insert_start(5)
mylist.Insert_start(6)
mylist.Insert_after(45, 10)
mylist.Delete_item(4)


for data in mylist:
    print(data)
