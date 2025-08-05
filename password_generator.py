# Генератор безопасных паролей
# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку
# на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

# Составляющие проекта:

# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл for;
# Написание пользовательских функций;
# Работа с модулем random для генерации случайных чисел.

import secrets

# Наборы символов
binary = "01"
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""


# Функция проверки, является ли ввод числом
def is_valid_number(n):
    return n.isdigit()


# Функция получения согласия пользователя
def get_user_consent(question):
    answer = input(question).strip().lower()
    return answer in ("да", "д", "y", "yes", "1")


# Функция генерации пароля
def generate_password(length, chars):
    return "".join(secrets.choice(chars) for _ in range(length))


# Функция для получения числового ввода с проверкой
def get_numeric_input(prompt, min_value, max_value):
    while True:
        value = input(prompt)
        if not value:
            print("Вы не ввели число, попробуйте еще раз.")
            continue
        if is_valid_number(value) and min_value <= int(value) <= max_value:
            return int(value)
        print(
            f"Вы ввели некорректно, необходимо указать число от {min_value} до {max_value}."
        )


# функция исключаем неоднозначные символы
def exclude_ambiguous_characters(chars):
    # Список неоднозначных символов
    ambiguous_characters = set("O0l1I")

    # Проверяем, содержатся ли только цифры в chars
    if all(char.isdigit() for char in chars):
        return chars  # Возвращаем без изменений, если только цифры

    # Исключаем неоднозначные символы
    return [char for char in chars if char not in ambiguous_characters]


# Получение количества паролей и их длины
count = get_numeric_input(
    "Введите необходимое количество паролей от 1 до 100 штук: ", 1, 100
)
length = get_numeric_input("Введите длину пароля (от 8 до 256): ", 8, 256)

# Проверка выбора типов символов
is_binary = get_user_consent("Использовать бинарные символы? Y / N: ")
is_digit = get_user_consent("Использовать цифры? Y / N: ")
is_lowcase = get_user_consent("Использовать строчные буквы? Y / N: ")
is_upcase = get_user_consent("Использовать ПРОПИСНЫЕ буквы? Y / N: ")
is_symbol = get_user_consent("Использовать спецсимволы? Y / N: ")

if not (is_binary or is_digit or is_lowcase or is_upcase or is_symbol):
    print(
        "Вы не выбрали ни один тип символов для пароля. Пожалуйста, попробуйте снова."
    )
    exit()

# Добавляем символы в зависимости от выбора пользователя
if is_binary:
    chars += binary
if is_digit:
    chars += digits
if is_lowcase:
    chars += lowercase_letters
if is_upcase:
    chars += uppercase_letters
if is_symbol:
    chars += punctuation

# Исключение неоднозначных символов
is_ambiguous = get_user_consent(
    'Исключать ли неоднозначные символы "il1Lo0O" ? Y / N: '
)
if is_ambiguous:
    exclude_ambiguous_characters

# Генерация и вывод паролей
print("\nВарианты паролей:")
for i in range(1, count + 1):
    print(f"Вариант пароля номер {i}: {generate_password(length, chars)}")

print("Пароли сгенерированы успешно!")

# Безопасность: Пароли, сгенерированные вашим кодом, будут достаточно сильными, но для максимальной
# безопасности рекомендуется использовать более сложные алгоритмы генерации паролей и хранить их
# в надежном месте.
# Хранение: Никогда не храните пароли в незащищенном виде! Используйте менеджер паролей для их
# безопасного хранения.
# Надеюсь, эти дополнения помогут вам сделать ваш код для генерации паролей еще лучше!