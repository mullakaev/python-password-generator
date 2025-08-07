# app.py

from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import password_generator # Импортируем наш скрипт

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here' # Нужен для безопасности, можно придумать любую строку

# Получаем путь к директории, где находится app.py
# Это нужно, чтобы Flask знал, где искать index.html
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    """
    Отдает пользователю главную страницу (index.html).
    """
    return render_template('index.html') # Flask автоматически ищет файлы в папке 'templates'

@app.route('/generate_password', methods=['POST'])
def handle_generate_password():
    """
    Принимает POST-запрос с параметрами генерации, вызывает
    password_generator.py и возвращает результат.
    """
    try:
        data = request.get_json() # Получаем JSON из запроса
        length = data.get('length', 12)
        include_uppercase = data.get('include_uppercase', True)
        include_numbers = data.get('include_numbers', True)
        include_symbols = data.get('include_symbols', True)

        # Валидация длины (можно вынести в password_generator.py, но для простоты здесь)
        if not isinstance(length, int) or length < 8 or length > 256:
            return jsonify({"error": "Длина пароля должна быть числом от 8 до 256."}), 400 # Bad Request

        # Вызываем функцию генерации из нашего модуля
        password, error = password_generator.generate_password(
            length=length,
            include_uppercase=include_uppercase,
            include_numbers=include_numbers,
            include_symbols=include_symbols
        )

        if error:
            # Если есть ошибка от генератора
            return jsonify({"error": error}), 400 # Bad Request

        # Если все успешно
        return jsonify({"password": password}), 200 # OK

    except Exception as e:
        # Обработка непредвиденных ошибок
        print(f"Ошибка в /generate_password: {e}")
        return jsonify({"error": "Произошла внутренняя ошибка сервера."}), 500 # Internal Server Error

# --- Дополнительно: отдаем статические файлы (CSS, JS) ---
# Flask обычно ищет их в папке 'static'.
# Если вы хотите, чтобы index.html сам брал CSS/JS,
# вам нужно будет поместить их в папку 'static'
# и изменить пути в <head> и перед </body> в index.html.
# Пока оставим CSS внутри <style> для простоты.

if __name__ == '__main__':
    # Создаем папку templates, если она не существует
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # Перемещаем index.html в папку templates
    # Это важно, так как render_template ищет файлы там
    if os.path.exists('index.html'):
        os.rename('index.html', os.path.join('templates', 'index.html'))
        print("Файл index.html перемещен в папку 'templates'.")
    else:
        print("Ошибка: Файл index.html не найден! Создайте его в корневой директории.")

    # Запускаем Flask-приложение
    # debug=True позволяет автоматически перезапускать сервер при изменениях кода
    # host='0.0.0.0' делает сервер доступным извне (не только с localhost)
    app.run(debug=True, host='0.0.0.0', port=5000)