from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ola/')
def ola():
    return '<h1>Olá usuário!</h1>'


app.run(debug=True)
