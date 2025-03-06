from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QHBoxLayout, QFrame, QMessageBox
from PySide6.QtCore import Qt
from logica import buscar_dados_no_parquet

class QHLine(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setStyleSheet("background-color: white; height: 2px;")

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

        # Criando os quadros individuais para usar nas verificações
        self.square_prot = QFrame()
        self.square_acid = QFrame()
        self.square_tranq = QFrame()
        self.square_resid = QFrame()
        self.square_dental = QFrame()

        # Criando os dicionários com os mesmos quadros
        self.seguros = {
            'SEGURO PROTEÇÃO COMPLETA': self.square_prot,
            'ACIDENTE PESSOAL COMPLETO': self.square_acid,
            'TRANQUILIDADE PREMIADA': self.square_tranq,
        }

        self.labels_seguros = {
            'SEGURO PROTEÇÃO COMPLETA': QLabel('SEGURO PROTEÇÃO COMPLETA'),
            'ACIDENTE PESSOAL COMPLETO': QLabel('ACIDENTE PESSOAL COMPLETO'),
            'TRANQUILIDADE PREMIADA': QLabel('TRANQUILIDADE PREMIADA'),
        }

        # Criando os quadrados e rótulos ASSISTÊNCIAS
        self.assistencias = {
            'RESIDENCIAL/EMPRESA': self.square_resid,
            'SOS DENTAL': self.square_dental,
        }

        self.labels_assist = {
            'RESIDENCIAL/EMPRESA': QLabel('RESIDENCIAL/EMPRESA'),
            'SOS DENTAL': QLabel('SOS DENTAL'),
        }

        # Configuração dos quadrados
        for frame in list(self.seguros.values()) + list(self.assistencias.values()):
            frame.setFixedSize(25, 25)
            frame.setStyleSheet("background-color: #ffffff; border: 2px solid black;")

        # Estilos gerais
        self.setStyleSheet("background-color: #292929;")
        self.label_cpf.setStyleSheet("color: #ffffff; font-size: 20px; font-weight: bold;")
        self.input_cpf.setStyleSheet("background-color: #ffffff; color: #333333; font-size: 14px; border-radius: 5px; width: 360px; height:20px;")
        self.button_pesquisar.setStyleSheet("background-color: #00C6CC; color: #333333; font-size: 14px; border-radius: 5px; padding: 5px 10px; width: 170px; font-weight: bold; height:20px;")
        self.button_limpar.setStyleSheet("background-color: #D3FF00; color: #333333; font-size: 14px; border-radius: 5px; padding: 5px 10px;font-weight: bold;")
        self.label_seguros.setStyleSheet("color: #ffffff; font-size: 20px; font-weight: bold;")
        self.label_assist.setStyleSheet("color: #ffffff; font-size: 20px; font-weight: bold;")

        # Layout Cabeçalho
        layout.addWidget(self.label_cpf)
        layout.addSpacing(10)
        layout.addWidget(self.input_cpf)
        layout.addSpacing(5)

        # Layout dos botões
        h_layout = QHBoxLayout()
        h_layout.setSpacing(10)
        h_layout.addWidget(self.button_pesquisar)
        h_layout.addWidget(self.button_limpar)

        layout.addLayout(h_layout)
        layout.addSpacing(10)
        layout.addWidget(QHLine())
        layout.addWidget(self.label_seguros)
        layout.addSpacing(3)

        # Layout dos seguros (SEPARADOS)
        for nome, frame in self.seguros.items():
            s_layout = QHBoxLayout()
            s_layout.setSpacing(10)
            s_layout.addWidget(frame)
            s_layout.addWidget(self.labels_seguros[nome])
            layout.addLayout(s_layout)
            layout.addSpacing(3)

        layout.addSpacing(10)
        layout.addWidget(QHLine())
        layout.addWidget(self.label_assist)
        layout.addSpacing(10)

        # Layout das assistências (SEPARADAS)
        for nome, frame in self.assistencias.items():
            a_layout = QHBoxLayout()
            a_layout.setSpacing(10)
            a_layout.addWidget(frame)
            a_layout.addWidget(self.labels_assist[nome])
            layout.addLayout(a_layout)
            layout.addSpacing(3)

        self.setLayout(layout)
        self.setWindowTitle('APP VENDAS')
        self.setFixedSize(430, 350)
        font = QtGui.QFont('Geist-Regular', 10)
        self.setFont(font)

        # Eventos dos botões
        self.button_pesquisar.clicked.connect(self.on_pesquisar)
        self.button_limpar.clicked.connect(self.on_limpar)

    def on_pesquisar(self):
        cpf_input = self.input_cpf.text().strip()
        
        if not cpf_input:
            QMessageBox.warning(self, 'Aviso', 'Digite um CPF para pesquisar!')
            return

        resultado = buscar_dados_no_parquet(cpf_input)

        # Reseta todas as cores antes de aplicar novas
        self.resetar_cores()

        if resultado is not None:
            for _, row in resultado.iterrows():
                seguro = row['SEGURO']
                status = row['STATUS_SEGURO']

                cor = "green" if status.lower() == "ativo" else "red"

                if "PROTEÇÃO COMPLETA" in seguro:
                    self.square_prot.setStyleSheet(f"background-color: {cor}; border: 2px solid black;")
                elif "ACIDENTE PESSOAL" in seguro:
                    self.square_acid.setStyleSheet(f"background-color: {cor}; border: 2px solid black;")
                elif "TRANQUILIDADE PREMIADA" in seguro:
                    self.square_tranq.setStyleSheet(f"background-color: {cor}; border: 2px solid black;")
                elif "RESIDENCIAL" in seguro:
                    self.square_resid.setStyleSheet(f"background-color: {cor}; border: 2px solid black;")
                elif "DENTAL" in seguro:
                    self.square_dental.setStyleSheet(f"background-color: {cor}; border: 2px solid black;")

    def resetar_cores(self):
        """Reseta a cor dos quadrados para branco"""
        estilo_padrao = "background-color: white; border: 2px solid black;"
        
        for frame in list(self.seguros.values()) + list(self.assistencias.values()):
            frame.setStyleSheet(estilo_padrao)

    def on_limpar(self):
        self.input_cpf.clear()
        self.resetar_cores()