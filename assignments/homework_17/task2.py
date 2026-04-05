class Author:
    def __init__(self, name, country,birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
    def __str__(self):
        return f"{self.name} ({self.country})"
    def __repr__(self):
        return f"Author(name='{self.name}')"

class Book:
    total_books = 0
    def __init__(self, name, year,author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1
    def __str__(self):
        return f"'{self.name}' ({self.year}) by {self.author.name}"
    def __repr__(self):
        return f"Book('{self.name}', {self.year})"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year,author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book
    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]
    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]
    def __str__(self):
        return f"Library: {self.name}"
    def __repr__(self):
        return f"Library(name='{self.name}', total_books={len(self.books)})"


# 1. Створюємо автора
author1 = Author("Stephen King", "USA", "1947")

# 2. Створюємо бібліотеку
my_library = Library("City Central Library")

# 3. Додаємо книги через бібліотеку
my_library.new_book("The Shining", 1977, author1)
my_library.new_book("It", 1986, author1)
my_library.new_book("Misery", 1987, author1)

# 4. Перевіряємо групування за роком
print(f"Books from 1986: {my_library.group_by_year(1986)}")

# 5. Перевіряємо загальний лічильник книг у класі Book
print(f"Total books created: {Book.total_books}")