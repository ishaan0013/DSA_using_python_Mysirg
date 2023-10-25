class Book:
    def __init__(self, a, b, c) -> None:
        self.bookid = a
        self.title = b
        self.price = c

    def Show(self):
        print(
            f"The book {self.title} having ID {self.bookid} with price {self.price}")


bok = Book(123, "ABC", 344)
bok.Show()
