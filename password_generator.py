# password_generator.py

import random
import string

# Указываем версию программы
__version__ = "1.1.0"

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    """
    Генерирует случайный пароль на основе заданных параметров.

    Args:
        length (int): Длина пароля (по умолчанию 12).
        include_uppercase (bool): Включать ли заглавные буквы (по умолчанию True).
        include_numbers (bool): Включать ли цифры (по умолчанию True).
        include_symbols (bool): Включать ли специальные символы (по умолчанию True).

    Returns:
        str: Сгенерированный пароль.
        str: Сообщение об ошибке, если не выбраны никакие наборы символов.
    """
    characters = ''
    if length < 8: # Минимальная длина для безопасности
        return "Ошибка: Длина пароля должна быть не менее 8 символов.", None

    # Собираем все возможные символы
    characters += string.ascii_lowercase # Строчные буквы
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        # Можно выбрать набор символов или определить свой
        characters += string.punctuation # Стандартный набор пунктуации

    # Проверка, что хотя бы один тип символов выбран
    if not (include_uppercase or include_numbers or include_symbols):
        return "Ошибка: Выберите хотя бы один тип символов (заглавные, цифры, символы).", None

    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    return password, None # Возвращаем пароль и None для ошибки

# Пример использования (можно закомментировать или удалить, когда это будет частью веб-приложения)
if __name__ == "__main__":
    print(f"Текущая версия генератора: {__version__}")
    password, error = generate_password(length=16, include_symbols=False)
    if error:
        print(error)
    else:
        print(f"Случайный пароль: {password}")
