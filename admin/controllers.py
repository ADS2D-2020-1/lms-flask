import curso_dao
from flask import Blueprint, redirect, render_template, request


admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/admin'
)


@admin_bp.route('/')
def home_admin():
    return render_template(
        'home.html',
        titulo='Administração'
    )


@admin_bp.route('/cursos/')
def cursos_lista():
    cursos = curso_dao.listar_todos_cursos()
    return render_template(
        'cursos_lista.html',
        titulo='Controle de Cursos',
        cursos=cursos
    )


@admin_bp.route('/cursos/novo/', methods=['GET', 'POST'])
def cursos_incluir():
    erros = {}

    if request.method == 'POST':
        form = request.form

        nome = form.get('nome')
        sigla = form.get('sigla')
        tipo = form.get('tipo')
        coordenador = form.get('coordenador')
        duracao = form.get('duracao')
        sobre = form.get('sobre')

        periodo = form.getlist('periodo')

        if 'M' in periodo:
            matutino = 1
        else:
            matutino = 0

        noturno = 1 if 'N' in periodo else 0

        curso_dao.inserir_curso(
            nome,
            sigla,
            tipo,
            coordenador,
            duracao,
            matutino,
            noturno,
            sobre
        )
        return redirect('/admin/cursos/')

    return render_template(
        'cursos_form.html',
        titulo='Novo Curso',
        h1='Incluir Novo Curso',
        erros=erros
    )


@admin_bp.route('/cursos/alterar/<curso_id>/', methods=['GET', 'POST'])
def cursos_alterar(curso_id):
    erros = {}

    if request.method == 'POST':
        form = request.form

        nome = form.get('nome')
        sigla = form.get('sigla')
        tipo = form.get('tipo')
        coordenador = form.get('coordenador')
        duracao = form.get('duracao')
        sobre = form.get('sobre')

        periodo = form.getlist('periodo')

        if 'M' in periodo:
            matutino = 1
        else:
            matutino = 0

        noturno = 1 if 'N' in periodo else 0

        curso_dao.alterar_curso(
            curso_id,
            nome,
            sigla,
            tipo,
            coordenador,
            duracao,
            matutino,
            noturno,
            sobre
        )
        return redirect('/admin/cursos/')

    curso = curso_dao.obter_curso(id=curso_id)
    return render_template(
        'cursos_form.html',
        titulo='Alteração de Curso',
        h1=curso['nome'],
        erros=erros,
        curso=curso
    )


@admin_bp.route('/cursos/remover/<curso_id>/')
def cursos_remover(curso_id):
    curso_dao.remover_curso(curso_id)
    return redirect('/admin/cursos/')
