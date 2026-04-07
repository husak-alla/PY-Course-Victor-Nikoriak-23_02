def with_index(iterable, start=0):
    count = start

    for item in iterable:
        yield count, item
        count += 1

books = ["Танці з кістками", "Терапія", "Гра в хованки"]

for index, book in with_index(books, start=1):
    print(f"{index}. {book}")