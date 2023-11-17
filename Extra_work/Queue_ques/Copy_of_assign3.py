class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None) -> None:
        self.start = start

    def is_empty(self):
        return (self.start == None)

    def Insert_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def Insert_last(self, data):
        n = Node(data)
        if (self.is_empty()):
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def Insert_after(self, data, ref):
        if ref is not None:
            n = Node(data, ref.next)
            ref.next = n

    def Search(self, data):
        temp = self.start
        while temp is not None:
            if (temp.item == data):
                return temp
            temp = temp.next
        return None

    def print_list(self):
        if (self.is_empty()):
            return None
        else:
            temp = self.start
            while temp is not None:
                print(f"{temp.item}", end=" ")
                temp = temp.next

    def Delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def Delete_last(self):
        if self.start is None:
            pass
        elif (self.start.next is None):
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def Delete_item(self, data):
        if (self.start == None):
            print("List is empty!")
        else:
            if (self.start.next == None):
                if (self.start.item == data):
                    self.start = None
            elif (self.start.item == data):
                self.start = self.start.next
            else:
                temp = self.start
                while temp.next is not None:
                    if (temp.next.item == data):
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def __iter__(self):
        return SLLIterator(self.start)


class SLLIterator:
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


if __name__ == "__main__":
    mylist = SLL()
    mylist.Insert_start(1)
    mylist.Insert_start(2)
    mylist.Insert_start(-3)
    mylist.Insert_last(4)
    mylist.Insert_last(5)
    mylist.Insert_last(6)
    mylist.Insert_after(7, mylist.Search(-3))
    mylist.Delete_item(5)
    for item in mylist:
        print(item)
