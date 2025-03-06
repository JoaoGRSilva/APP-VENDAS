import pandas as pd
import time
from PySide6.QtWidgets import QMessageBox

try:
    df = pd.read_parquet('dados.parquet')
except FileNotFoundError:
    df = pd.DataFrame()


def search(cpf):
    global df

    if df.empty:
        dialog = QMessageBox()
        dialog.setText("Base de dados não carregada")
        dialog.setWindowTitle("Erro!")
        return  dialog
    
    colunas_requeridas = ['CPF', 'SEGURO', 'STATUS_SEGURO']
    for coluna in colunas_requeridas:
        if coluna not in colunas_requeridas:
            QMessageBox.critical(None, 'Erro', f'A coluna {coluna} não foi encontrada')
            return