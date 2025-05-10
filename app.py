from flask import Flask

# Создаем объект приложения Flask
app = Flask(__name__)

# Главная страница
@app.route('/')
def hello_flask():
    return "Hello, Flask!"


# Задание 1: Простые маршруты
@app.route('/hello')
def hello():
    return "Hello, world!"

@app.route('/info')
def info():
    return "This is an informational page."


# Задание 2: Сумма чисел
@app.route('/calc/<a>/<b>')
def calc(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        return f"The sum of {num1} and {num2} is {num1 + num2}."
    except ValueError:
        return "Error: Please provide two valid integers."


# Задание 3: Переворот текста
@app.route('/reverse/<text>')
def reverse(text):
    if len(text.strip()) == 0:
        return "Error: Text must contain at least one character."
    return text[::-1]


# Задание 4: Приветствие с возрастом
@app.route('/user/<name>/<age>')
def user(name, age):
    try:
        age_num = int(age)
        if age_num < 0:
            return "Error: Age cannot be negative."
        return f"Hello, {name}. You are {age_num} years old."
    except ValueError:
        return "Error: Age must be a number."

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)

# Проверка заданий :)
#
# http://127.0.0.1:5000/ → "Hello, Flask!"
#
# http://127.0.0.1:5000/hello → "Hello, world!"
#
# http://127.0.0.1:5000/info → "This is an informational page."
#
# http://127.0.0.1:5000/calc/3/5 → "The sum of 3 and 5 is 8."
#
# http://127.0.0.1:5000/calc/a/b → покажет ошибку, укажите два допустимых целых числа.
#
# http://127.0.0.1:5000/reverse/hello → "olleh"
#
# http://127.0.0.1:5000/reverse/ → покажет ошибку, потому что пустой текст
#
# http://127.0.0.1:5000/user/Anna/25 → "Hello, Anna. You are 25 years old."
#
# http://127.0.0.1:5000/user/John/-5 → покажет ошибку, потому что возраст не может быть отрицательным.