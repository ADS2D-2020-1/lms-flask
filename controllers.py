from flask import redirect, render_template, request
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
    # erros = []
    erros = {}
    if request.method == 'POST':
        form = request.form

        nome = form.get('nome-completo')
        if len(nome.strip()) == 0:
            # erros.append('Nome completo é de preenchimento obrigatório')
            erros['nome-completo'] = ['Nome completo é de preenchimento obrigatório']

        email = form.get('email')
        if len(email.strip()) == 0:
            # erros.append('E-mail é de preenchimento obrigatório')
            erros['email'] = ['E-mail é de preenchimento obrigatório']

        assunto = form.get('assunto')
        if len(assunto.strip()) == 0:
            # erros.append('Assunto é de escolha obrigatória')
            erros['assunto'] = ['Assunto é de escolha obrigatória']
        else:
            if assunto == 'B':
                assunto = 'Bug'
            elif assunto == 'R':
                assunto = 'Reclamação'
            else:
                assunto = 'Sugestão'

        mensagem = form.get('mensagem')
        if len(mensagem.strip()) == 0:
            # erros.append('Mensagem é de preenchimento obrigatório')
            erros['mensagem'] = ['Mensagem é de preenchimento obrigatório']

        conheceu = form.getlist('conheceu')
        if len(conheceu) == 0:
            erros['conheceu'] = ['Ao menos uma opção é obrigatória']

        if len(erros) > 0:
            print(f'''
                Nome completo: {nome}
                E-mail: {email}
                Assunto: {assunto}
                Mensagem: {mensagem}
                Como Conheceu? {conheceu}
            ''')
            return redirect('/agradecimento/')
    else:
        print('Acesso por GET')

    return render_template('contato.html', erros=erros)


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
