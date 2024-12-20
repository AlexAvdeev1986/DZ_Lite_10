# Упражнение 3: Класс собственного исключения и его использование

class NegativeNumberError(Exception):
    def __init__(self, value, message="Число не должно быть отрицательным"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.value}"

def check_positive_number(number):
    try:
        if number < 0:
            raise NegativeNumberError(number)
        print(f"Число положительное: {number}")
    except NegativeNumberError as e:
        print(f"Ошибка: {e}")

# Проверка функции
check_positive_number(10)  # Ожидается успешное выполнение
check_positive_number(-5)  # Ожидается генерация NegativeNumberError
