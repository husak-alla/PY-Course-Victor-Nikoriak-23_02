class FileContextManager:
    counter = 0

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        FileContextManager.counter += 1
        print(f"Відкриваю: {self.filename} (Запуск №{FileContextManager.counter})")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Закриваю: {self.filename}")
        self.file.close()

#Перевірка
with FileContextManager("test.txt", "w") as f:
    f.write("Hello World!")

with FileContextManager("test.txt", "r") as f:
    print(f.read())