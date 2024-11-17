from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summarize')
def summarize():
    return render_template('ytpage.html')


def any_commands_example(a):
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
</html>
'''



@app.route('/submit-link', methods=['POST'])
def submit_link():

    youtube_link = request.form.get('youtube_link')
    if youtube_link:
        print(f"ссылка получена: {youtube_link}")
        return any_commands_example(youtube_link)

    else:
        print(f"ссылка не получена")
        return "No link provided!", 400


if __name__ == '__main__':
    app.run(debug=True)
