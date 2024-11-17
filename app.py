from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Главная страница
@app.route('/')
def index():
    return render_template('index.html')


# Страница для ввода ссылки
@app.route('/summarize')
def summarize():
    return render_template('ytpage.html')


def any_commands(a):
    s = str(a)
    return f'''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Link Length</title>
</head>
<body>
    <h1>В ссылке {len(s)} символов</h1>
</body>
</html>'''



# Обработка отправленных данных
@app.route('/submit-link', methods=['POST'])
def submit_link():
    # Получение ссылки из формы
    youtube_link = request.form.get('youtube_link')
    print("aboba")
    if youtube_link:
        return any_commands(youtube_link)

    else:
        return "No link provided!", 400


if __name__ == '__main__':
    app.run(debug=True)

