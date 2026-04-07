class MySmartData:
    def __init__(self, data):
        self._data = list(data)
        self._cursor = 0

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        self._cursor = 0
        return self

    def __next__(self):
        if self._cursor >= len(self._data):
            raise StopIteration

        value = self._data[self._cursor]
        self._cursor += 1
        return value


#Перевірка

my_collection = MySmartData(["Python", "SQL", "Pandas"])
print(f"Останній елемент: {my_collection[-1]}")
print("Перебір усіх елементів:")
for item in my_collection:
    print(f"-> {item}")