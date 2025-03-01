from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QHBoxLayout, QFrame
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
        self.label_seguros = QLabel('Seguros')
        self.label_assist = QLabel('Assistências')


        self.square_prot = QFrame()
        self.square_prot.setFixedSize(25,25)
        self.label_prot_completa = QLabel('SEGURO PROTEÇÃO COMPLETA')

        self.square_acid = QFrame()
        self.square_acid.setFixedSize(25,25)
        self.label_aci_pessoal = QLabel('ACIDENTE PESSOAL COMPLETO')

        self.square_tranq = QFrame()
        self.square_tranq.setFixedSize(25,25)
        self.label_tranq = QLabel('TRANQUILIDADE PREMIADA')

        self.square_resid = QFrame()
        self.square_resid.setFixedSize(25,25)
        self.label_resid = QLabel('RESIDENCIAL/EMPRESA')

        self.square_dental = QFrame()
        self.square_dental.setFixedSize(25,25)
        self.label_dental = QLabel('SOS DENTAL')


        #Style
        self.setStyleSheet("background-color: #292929;")
        self.label_cpf.setStyleSheet("color: #ffffff; font-size: 20px; font-weight: bold;")
        self.input_cpf.setStyleSheet("background-color: #ffffff; color: #333333; font-size: 14px; border-radius: 5px; width: 360px; height:20px;")
        self.button_pesquisar.setStyleSheet("background-color: #00C6CC; color: #333333; font-size: 14px; border-radius: 5px; padding: 5px 10px; width: 170px; font-weight: bold; height:20px;")
        self.button_limpar.setStyleSheet("background-color: #D3FF00; color: #333333; font-size: 14px; border-radius: 5px; padding: 5px 10px;font-weight: bold;")
        self.label_seguros.setStyleSheet("color: #ffffff; font-size: 20px; font-weight: bold;")
        self.label_assist.setStyleSheet("color: #ffffff; font-size: 20px; font-weight: bold;")
        self.square_prot.setStyleSheet("background-color: white; border: 2px solid black;")
        self.square_acid.setStyleSheet("background-color: white; border: 2px solid black;")        
        self.square_tranq.setStyleSheet("background-color: white; border: 2px solid black;")   
        self.square_resid.setStyleSheet("background-color: white; border: 2px solid black;")
        self.square_dental.setStyleSheet("background-color: white; border: 2px solid black;")   

        # Layout Cabeçalho
        layout.addWidget(self.label_cpf)
        layout.addSpacing(10)
        layout.addWidget(self.input_cpf)
        layout.addSpacing(5)

        # Layout Buttons
        h_layout = QHBoxLayout()
        h_layout.setSpacing(10) 
        h_layout.addWidget(self.button_pesquisar)
        h_layout.addWidget(self.button_limpar)

        #layout protecao
        s_layout = QHBoxLayout()
        s_layout.setSpacing(10)
        s_layout.addWidget(self.square_prot)
        s_layout.addWidget(self.label_prot_completa)

        #layout acidente
        s1_layout = QHBoxLayout()
        s1_layout.setSpacing(10)
        s1_layout.addWidget(self.square_acid)
        s1_layout.addWidget(self.label_aci_pessoal)

        #layout tranq
        s2_layout = QHBoxLayout()
        s2_layout.setSpacing(10)
        s2_layout.addWidget(self.square_tranq)
        s2_layout.addWidget(self.label_tranq)

        #layout resid
        a_layout = QHBoxLayout()
        a_layout.setSpacing(10)
        a_layout.addWidget(self.square_resid)
        a_layout.addWidget(self.label_resid)

        #layout resid
        a1_layout = QHBoxLayout()
        a1_layout.setSpacing(10)
        a1_layout.addWidget(self.square_dental)
        a1_layout.addWidget(self.label_dental)

        layout.addLayout(h_layout)
        layout.addSpacing(10)
        layout.addWidget(QHLine())
        layout.addWidget(self.label_seguros)
        layout.addSpacing(3)
        layout.addLayout(s_layout)
        layout.addSpacing(3)
        layout.addLayout(s1_layout)
        layout.addSpacing(3)
        layout.addLayout(s2_layout)
        layout.addSpacing(10)
        layout.addWidget(QHLine())
        layout.addWidget(self.label_assist)
        layout.addSpacing(3)
        layout.addLayout(a_layout)
        layout.addSpacing(3)
        layout.addLayout(a1_layout)
        layout.addSpacing(10)


        
        self.setLayout(layout)
        self.setWindowTitle('APP VENDAS')
        self.setFixedSize(430, 350)
        font = QtGui.QFont('Geist-Regular', 10)
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

class QHLine(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet("background-color: white; height: 2px;")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())