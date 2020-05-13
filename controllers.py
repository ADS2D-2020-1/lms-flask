from flask import render_template, request
from app import app
from curso_dao import listar_todos_cursos, obter_curso


@app.route('/')
def index():
    return render_template(
        'index.html',
        titulo='Página Inicial',
        batata='FIT - Faculdade Impacta',
        idade=18
    )


@app.route('/sobre-a-faculdade/')
def sobre():
    return render_template(
        'sobre.html'
    )


@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        print('Acesso por POST')
    else:
        print('Acesso por GET')

    return render_template('contato.html')


@app.route('/agradecimento/')
def agradecimento():
    return render_template('agradecimento.html')


@app.route('/cursos/<sigla>/')
def curso(sigla):
    curso = obter_curso(sigla.upper())
    return render_template(
        'curso.html',
        curso=curso,
        titulo=curso['nome']
    )


@app.context_processor
def lista_cursos():
    return {
        'cursos': listar_todos_cursos()
    }
