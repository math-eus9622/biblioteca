import sqlite3


class Livro:
    def __init__(self, titulo, isbn, autor_id, ano_publicacao):
        self.titulo = titulo
        self.isbn = isbn
        self.autor_id = autor_id
        self.ano_publicacao = ano_publicacao


class Autor:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento


class Biblioteca:
    def __init__(self, db_name='biblioteca.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS autores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    data_nascimento TEXT
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    isbn TEXT UNIQUE NOT NULL,
                    autor_id INTEGER,
                    ano_publicacao INTEGER,
                    FOREIGN KEY (autor_id) REFERENCES autores (id)
                )
            ''')

    def adicionar_autor(self, autor):
        with self.conn:
            cursor = self.conn.execute('''
                INSERT INTO autores (nome, data_nascimento) VALUES (?, ?)
            ''', (autor.nome, autor.data_nascimento))
        return cursor.lastrowid

    def adicionar_livro(self, livro):
        with self.conn:
            self.conn.execute('''
                INSERT INTO livros (titulo, isbn, autor_id, ano_publicacao) VALUES (?, ?, ?, ?)
            ''', (livro.titulo, livro.isbn, livro.autor_id, livro.ano_publicacao))

    def buscar_livro_por_titulo(self, titulo):
        cursor = self.conn.execute('''
            SELECT * FROM livros WHERE titulo LIKE ?
        ''', ('%' + titulo + '%',))
        return cursor.fetchall()

    def remover_livro(self, livro_id):
        with self.conn:
            self.conn.execute('''
                DELETE FROM livros WHERE id = ?
            ''', (livro_id,))
