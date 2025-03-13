import PyInstaller.__main__

# Rodar o PyInstaller com a configuração desejada
PyInstaller.__main__.run([
    'main.py',  # seu arquivo principal (modifique o nome se necessário)
    '--onefile',  # cria um único executável
    '--noconsole',  # não mostra o console ao executar
    '--name=Consulta de Seguros',  # nome do executável
    '--windowed',  # aplicação com interface gráfica (sem terminal)
    '--icon=icone.ico',  # Caminho para o ícone do seu aplicativo
    '--hidden-import=PySide6.QtCore',
    '--hidden-import=PySide6.QtGui',
    '--hidden-import=PySide6.QtWidgets',
])
