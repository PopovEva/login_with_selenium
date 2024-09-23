from flask import Flask, render_template, request, redirect, url_for, send_file

app = Flask(__name__)

# Данные для авторизации (например, логин и пароль)
valid_username = "eva"
valid_password = "123"

# Главная страница с формой входа
@app.route('/')
def login():
    return send_file('index.html')

# Обработка формы логина
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    # Проверка данных
    if username == valid_username and password == valid_password:
        return "<h2>Welcome!</h2><p>You have successfully logged in.</p>"
    else:
        return "<h2>Invalid credentials</h2><p>The username or password you entered is incorrect. Please try again.</p>"

if __name__ == '__main__':
    app.run(debug=True)
