from flask import g


def listar_todos_cursos():
    rv = g.query_db('SELECT * FROM cursos')
    return rv


def listar_disciplinas():
    rv = g.query_db('SELECT * FROM disciplinas')
    return rv


def obter_curso(sigla='', id=''):
    if sigla:
        curso = g.query_db(
            'SELECT * FROM cursos WHERE sigla = ?',
            [sigla],
            one=True
        )
    else:
        curso = g.query_db(
            'SELECT * FROM cursos WHERE id = ?',
            [id],
            one=True
        )
    curso['grade'] = listar_disciplinas_curso(curso['id'])
    return curso


def listar_disciplinas_curso(curso_id):
    disciplinas = g.query_db(
        '''
            SELECT c.semestre, d.*
              FROM disciplinas d
              JOIN curriculo c ON c.disciplina_id = d.id
             WHERE c.curso_id = ?
        ''',
        [curso_id]
    )
    grade = {}
    for d in disciplinas:
        semestre = d['semestre']
        if semestre not in grade:
            grade[semestre] = [d]
        else:
            grade[semestre].append(d)
    return grade


def inserir_curso(nome, sigla, tipo, coordenador, duracao, matutino, noturno, sobre):
    g.execute_db(
        '''
        INSERT INTO cursos
        (nome, sigla, tipo, coordenador, duracao, matutino, noturno, sobre)
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (nome, sigla, tipo, coordenador, duracao, matutino, noturno, sobre)
    )


def alterar_curso(curso_id, nome, sigla, tipo, coordenador, duracao, matutino, noturno, sobre):
    g.execute_db(
        '''
        UPDATE cursos
           SET nome = ?,
               sigla = ?,
               tipo = ?,
               coordenador = ?,
               duracao = ?,
               matutino = ?,
               noturno = ?,
               sobre = ?
         WHERE id = ?
        ''',
        (nome, sigla, tipo, coordenador, duracao, matutino, noturno, sobre, curso_id)
    )


def remover_curso(curso_id):
    g.execute_db(
        '''
        DELETE FROM cursos
         WHERE id = ?
        ''',
        (curso_id)
    )
