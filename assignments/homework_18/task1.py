class Email:
    def __init__(self, email):
        try:
            self.validate(email)
            self.email = email
            print("Email збережено успішно!")
        except ValueError as e:
            print(f"Помилка при створенні: {e}")

    @classmethod
    def validate(cls, email):
        if "@" not in email or "." not in email:
            raise ValueError("Некоректний формат: відсутня @ або крапка")


e1 = Email("my.cat.businka@gmail.com")
e2 = Email("bad_email@com")
e3 = Email("no_at_symbol.com")