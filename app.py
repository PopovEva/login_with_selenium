from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# Данные для авторизации
valid_username = "eva"
valid_password = "123"

# Главная страница с формой входа
@app.route('/')
def index():
    # Отправляем файл index.html из текущей директории
    return send_file('index.html')

# Обработка формы логина
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    # Проверка данных
    if username == valid_username and password == valid_password:
        return jsonify({'success': True, 'message': f'Welcome, {username}!'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials. Please try again.'})

if __name__ == '__main__':
    app.run(debug=True)
