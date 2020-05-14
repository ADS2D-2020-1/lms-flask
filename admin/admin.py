import curso_dao
from flask import Blueprint, render_template, request, redirect


admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/admin/'
)


@admin_bp.route('/')
def home():
    return render_template('home.html')


@admin_bp.route('/cursos/')
def cursos_lista():
    cursos = curso_dao.listar_todos_cursos()
    return render_template(
        'cursos_lista.html',
        cursos=cursos
    )


@admin_bp.route('/cursos/novo/', methods=['GET', 'POST'])
def curso_novo():
    erros = {}

    if request.method == 'POST':
        form = request.form

        nome = form.get('nome')
        if len(nome.strip()) == 0:
            erros['nome'] = ['Campo obrigatório']

        sigla = form.get('sigla')
        tipo = form.get('tipo')
        coordenador = form.get('coordenador')
        duracao = form.get('duracao')
        sobre = form.get('sobre')

        if len(erros) == 0:
            curso_dao.inserir_curso(
                nome,
                sigla,
                tipo,
                coordenador,
                duracao,
                None,
                None,
                sobre
            )
            return redirect('/admin/cursos/')

    return render_template(
        'cursos_form.html',
        erros=erros,
        titulo_form='Incluindo novo Curso'
    )


@admin_bp.route('/cursos/alterar/<curso_id>/', methods=['GET', 'POST'])
def curso_alterar(curso_id):
    erros = {}
    curso = curso_dao.obter_curso(id=curso_id)
    
    if request.method == 'POST':
        pass

    return render_template(
        'cursos_form.html',
        erros=erros,
        titulo_form='Alterando Curso',
        curso=curso
    )
