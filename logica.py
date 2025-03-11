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

    # Validar e padronizar CPF
    cpf_limpo = ''.join(filter(str.isdigit, str(cpf)))
    
    if len(cpf_limpo) < 11:
        cpf_limpo = cpf_limpo.zfill(11)
    elif len(cpf_limpo) > 11:
        QMessageBox.critical(None, 'Erro', 'O CPF inserido tem mais de 11 dígitos!')
        return None
    
    # Busca com CPF completo (11 dígitos)
    try:
        cpf_int = int(cpf_limpo)
        seguros_cliente = df[df['CPF'] == cpf_int]
        
        if seguros_cliente.empty:
            cpf_sem_zeros = int(cpf_limpo.lstrip('0'))
            seguros_cliente = df[df['CPF'] == cpf_sem_zeros]
            
        if seguros_cliente.empty:
            QMessageBox.information(None, 'Aviso', 'CPF não encontrado na base de dados.')
            return None
            
        return seguros_cliente
        
    except ValueError:
        QMessageBox.critical(None, 'Erro', 'O CPF inserido é inválido!')
        return None