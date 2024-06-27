import os

os.environ['QT_QPA_PLATFORM'] = 'xcb'

from PyQt5.QtWidgets import QApplication
from gui import BibliotecaApp  # Certifique-se de importar a classe BibliotecaApp corretamente
from biblioteca import Biblioteca
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Criando uma instância da biblioteca
    biblioteca = Biblioteca()

    # Criando uma instância da aplicação da biblioteca
    ex = BibliotecaApp(biblioteca)

    # Exibindo a aplicação da biblioteca
    ex.show()

    # Iniciando o loop principal do aplicativo
    sys.exit(app.exec_())
