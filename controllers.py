from flask import render_template, request
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')


@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        print('Isso foi um POST na página Contato')
    else:
        print('Isso foi um GET na página contato')

    return render_template('contato.html')


@app.route('/agradecimento/')
def agradecimento():
    return render_template('agradecimento.html')
