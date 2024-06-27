from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from biblioteca import Biblioteca, Livro

class BibliotecaApp(QWidget):
    def __init__(self, biblioteca):
        super().__init__()
        self.biblioteca = biblioteca
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gerenciamento de Biblioteca')

        layout = QVBoxLayout()

        self.lbl_titulo = QLabel('Título do Livro')
        layout.addWidget(self.lbl_titulo)
        self.entry_titulo = QLineEdit()
        layout.addWidget(self.entry_titulo)

        self.lbl_isbn = QLabel('ISBN')
        layout.addWidget(self.lbl_isbn)
        self.entry_isbn = QLineEdit()
        layout.addWidget(self.entry_isbn)

        self.lbl_autor = QLabel('Autor ID')
        layout.addWidget(self.lbl_autor)
        self.entry_autor = QLineEdit()
        layout.addWidget(self.entry_autor)

        self.lbl_ano = QLabel('Ano de Publicação')
        layout.addWidget(self.lbl_ano)
        self.entry_ano = QLineEdit()
        layout.addWidget(self.entry_ano)

        self.btn_adicionar = QPushButton('Adicionar Livro')
        self.btn_adicionar.clicked.connect(self.adicionar_livro)
        layout.addWidget(self.btn_adicionar)

        self.setLayout(layout)

    def adicionar_livro(self):
        titulo = self.entry_titulo.text()
        isbn = self.entry_isbn.text()
        autor_id = int(self.entry_autor.text())
        ano_publicacao = int(self.entry_ano.text())

        livro = Livro(titulo, isbn, autor_id, ano_publicacao)
        self.biblioteca.adicionar_livro(livro)
        QMessageBox.information(self, 'Sucesso', 'Livro adicionado com sucesso!')
