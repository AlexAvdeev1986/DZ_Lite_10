# Упражнение 2: Функция с валидацией входных данных

def validate_user_input(data):
    try:
        if not isinstance(data, dict):
            raise TypeError("Входные данные должны быть словарём.")

        if "name" not in data or not isinstance(data["name"], str):
            raise ValueError("Ключ 'name' отсутствует или его значение не является строкой.")

        if "age" not in data or not isinstance(data["age"], (int, float)) or data["age"] <= 0:
            raise ValueError("Ключ 'age' отсутствует или его значение не является положительным числом.")

        print("Данные пользователя корректны.")
    except (TypeError, ValueError) as e:
        print(f"Ошибка валидации данных: {e}")

# Проверка функции
validate_user_input({"name": "Alice", "age": 30})  # Ожидается успешная валидация
validate_user_input({"name": "Alice"})  # Отсутствует ключ 'age'
validate_user_input({"name": 123, "age": 30})  # Некорректное значение для 'name'
validate_user_input({"name": "Alice", "age": -10})  # Некорректное значение для 'age'
validate_user_input("Некорректный тип данных")  # Некорректный тип входных данных

