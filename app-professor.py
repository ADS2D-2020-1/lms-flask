from flask import Flask


app = Flask('minha-app')


@app.route('/')
def index():
    return 'Olá Mundo!'


@app.route('/ola/')
def ola():
    return 'Olá usuário!'


app.run(debug=True)
