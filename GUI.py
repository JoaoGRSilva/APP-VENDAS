from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt
import sys


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)
        
        # Widgets
        self.label_cpf = QLabel('Digite o CPF:')
        self.label_cpf.setAlignment(Qt.AlignBottom)
        self.input_cpf = QLineEdit()
        self.button_pesquisar = QPushButton('Pesquisar')
        self.button_limpar = QPushButton('Limpar')

        #Style
        self.setStyleSheet("background-color: #292929;")
        self.label_cpf.setStyleSheet("color: #ded953; font-size: 16px; font-weight: bold;")
        self.input_cpf.setStyleSheet("background-color: #ffffff; color: #333333; font-size: 14px; border-radius: 5px; width: 360px; height:20px;")
        self.button_pesquisar.setStyleSheet("background-color: #00C6CC; color: #333333; font-size: 14px; border-radius: 5px; padding: 5px 10px; width: 170px; font-weight: bold; height:20px;")
        self.button_limpar.setStyleSheet("background-color: #D3FF00; color: #333333; font-size: 14px; border-radius: 5px; padding: 5px 10px;font-weight: bold;")
        
        # Layout Cabeçalho
        layout.addWidget(self.label_cpf)
        layout.addWidget(self.input_cpf)
        
        # Layout Buttons
        h_layout = QHBoxLayout()
        h_layout.setSpacing(10)  # Espaçamento entre os botões
        h_layout.addWidget(self.button_pesquisar)
        h_layout.addWidget(self.button_limpar)
        layout.addLayout(h_layout)
        layout.addStretch(1)
        
        self.setLayout(layout)
        self.setWindowTitle('APP VENDAS')
        self.resize(300, 120)
        font = QtGui.QFont('Roboto', 10)
        self.setFont(font)

        # Logic
        self.button_pesquisar.clicked.connect(self.on_pesquisar)
        self.button_limpar.clicked.connect(self.on_limpar)
    
    def on_pesquisar(self):
        cpf_input = self.input_cpf.text()
        if cpf_input:
            print(f'Pesquisando CPF: {cpf_input}')
        else:
            print('Digite um CPF para pesquisar.')
    
    def on_limpar(self):
        self.input_cpf.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())