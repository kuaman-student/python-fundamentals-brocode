#Magic methods: Dunder methods (double underscore) __init__, __str__, __eq__
# They are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages =num_pages

    def __str__(self):
        return f"{self.title} : {self.author} : {self.num_pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title or self.author

book1 = Book("A", "Author1", 12)
book2 = Book("B", "Author2", 123)
book3 = Book("C", "Author3", 1234)
book4 = Book("C", "Author3", 123334)
book5 = Book("C", "Author3", 1234)


print(book1)
print(book2)
print(book3)
print(book4)
print(book5)

print(book4 == book5)
print(book4 == book3)
print(book4 == book2)
print(book4 == book1)



print(book4 > book5)
print(book4 > book3)
print(book4 > book2)
print(book4 > book1)


print(book4 + book5)
print(book4 + book3)
print(book4 + book2)
print(book4 + book1)


print("C" in book3)
print("C" in book1)
print("C" in book4)
