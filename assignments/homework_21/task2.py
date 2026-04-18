import unittest
import os

# Клас із завдання 1
class FileContextManager:
    counter = 0

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        FileContextManager.counter += 1
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # Не пригнічуємо помилки

# Тести для класу
class TestFileContextManager(unittest.TestCase):
    def setUp(self):
        self.filename = "test.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_positive_case(self):
        """Перевірка успішного запису та лічильника"""
        with FileContextManager(self.filename, "w") as f:
            f.write("test data")

        self.assertTrue(os.path.exists(self.filename))
        self.assertGreater(FileContextManager.counter, 0)

    def test_runtime_error_inside_with(self):
        """Перевірка, що файл закривається навіть при помилці всередині with"""
        try:
            with FileContextManager(self.filename, "w") as f:
                raise RuntimeError("Boom!")
        except RuntimeError:
            pass

        self.assertTrue(f.closed)

    def test_file_not_found(self):
        """Перевірка помилки, якщо файл не існує (режим читання)"""
        with self.assertRaises(FileNotFoundError):
            with FileContextManager("non_existent.txt", "r"):
                pass


if __name__ == "__main__":
    unittest.main()