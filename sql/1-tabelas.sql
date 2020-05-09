DROP TABLE IF EXISTS curriculo;
DROP TABLE IF EXISTS disciplinas;
DROP TABLE IF EXISTS cursos;

CREATE TABLE IF NOT EXISTS cursos (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nome        VARCHAR(50) NOT NULL UNIQUE,
    sigla       VARCHAR(5) NOT NULL UNIQUE,
    sobre       TEXT NULL,
    tipo        VARCHAR(15) NOT NULL,
    coordenador VARCHAR(50) NULL,
    duracao     SMALLINT NOT NULL,
    matutino    BOOLEAN,
    noturno     BOOLEAN
);

CREATE TABLE IF NOT EXISTS disciplinas (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nome            VARCHAR(50) NOT NULL UNIQUE,
    carga_horaria   INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS curriculo (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    curso_id        INTEGER NOT NULL,
    disciplina_id   INTEGER NOT NULL,
    semestre        SMALLINT NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos (id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas (id)
);