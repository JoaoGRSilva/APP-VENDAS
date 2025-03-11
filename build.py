import PyInstaller.__main__

# Rodar o PyInstaller com a configuração desejada
PyInstaller.__main__.run([
    'main.py',  # seu arquivo principal (modifique o nome se necessário)
    '--onefile',  # cria um único executável
    '--noconsole',  # não mostra o console ao executar
    '--name=Consulta_de_Seguros',  # nome do executável
    '--windowed',  # aplicação com interface gráfica (sem terminal)
])
