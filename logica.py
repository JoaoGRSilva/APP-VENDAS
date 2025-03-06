import pandas as pd
from PySide6.QtWidgets import QMessageBox

def buscar_dados_no_parquet(cpf):
    try:
        df = pd.read_parquet('dados.parquet')
    except FileNotFoundError:
        QMessageBox.critical(None, 'Erro', 'Base de dados não encontrada!')
        return None

    # Verificar se as colunas necessárias existem
    colunas_requeridas = ['CPF', 'SEGURO', 'STATUS_SEGURO']
    for coluna in colunas_requeridas:
        if coluna not in df.columns:
            QMessageBox.critical(None, 'Erro', f'A coluna {coluna} não foi encontrada na base de dados!')
            return None

    # Validar CPF como número
    try:
        cpf = int(cpf)
    except ValueError:
        QMessageBox.critical(None, 'Erro', 'O CPF inserido é inválido!')
        return None

    # Buscar dados no DataFrame
    seguros_cliente = df[df['CPF'] == cpf]

    if seguros_cliente.empty:
        QMessageBox.information(None, 'Aviso', 'CPF não encontrado na base de dados.')
        return None

    return seguros_cliente