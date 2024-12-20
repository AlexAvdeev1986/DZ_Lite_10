# Упражнение 1: Функция для преобразования строки в число

def convert_to_int(value):
    try:
        result = int(value)
        print(f"Преобразование успешно: {result}")
        return result
    except ValueError:
        print("Ошибка: Невозможно преобразовать строку в число.")
    except Exception as e:
        print(f"Неожиданная ошибка: {type(e).__name__}: {e}")
    finally:
        print("Попытка преобразования завершена.")

# Проверка функции
convert_to_int("123")  # Ожидается успешное преобразование
convert_to_int("abc")  # Ожидается ошибка ValueError
convert_to_int([1, 2, 3])  # Ожидается обработка неожиданной ошибки
