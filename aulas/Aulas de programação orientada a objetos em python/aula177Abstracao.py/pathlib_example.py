from pathlib import Path
from shutil import rmtree

# # #manipulação de caminhos
# # caminho_projeto = Path()
# # print(caminho_projeto) #caminho relativo, retorna "."
# # print(caminho_projeto.absolute()) #caminho até a pasta do projeto
 
# # caminho_arquivo = Path(__file__)
# # print(caminho_arquivo) #caminho até o atual arquivo
# # print(caminho_arquivo.parent) #caminho da pasta mãe
# # print(caminho_arquivo.parent.parent) #caminho da pasta mãe da pasta mãe e assim 
# # # por diante

# # #criação de caminhos
# # ideias = caminho_arquivo.parent / 'ideias'
# # print(ideias / 'arquivo.txt')  

# # print(Path.home() / 'OneDrive' / 'Área de Trabalho') #criando o caminho "desktop" a partir da home

# # arquivo = Path.home() / 'OneDrive' / 'Área de Trabalho' / 'arquivo1.txt'

# #maneira 1 de abrir um arquivo

# # arquivo.touch() #criou arquivo "arquivo1.txt"
# # print(arquivo)
# # arquivo.write_text('Olá') #escreveu um texto
# # arquivo.write_text('Olá de nv') #substitui o texto anterior
# # print(arquivo.read_text()) #ler no terminal o que está escrito
# # arquivo.unlink() #apagou arquivo "arquivo1.txt"

# #maneira 2 de abrir um arquivo

# # with arquivo.open('a+') as file:
# #     file.write('Olá\n')
# #     file.write('mundo\n')

# # print(arquivo.read_text())

pasta = Path.home() / 'OneDrive' / 'Área de Trabalho' / 'NovaPasta'

# #maneira 1 de abrir uma pasta

# # pasta.mkdir() # cria a pasta, se executar de novo, dará erro, pois falará que a pasta
# #já existe
pasta.mkdir(exist_ok=True) # Para não dá erro que a pasta já existe. Não duplica
# # pasta.rmdir() # se a pasta estiver vazia, conseguirá deletar, mas caso tenha
# #arquivo ou outras coisas dentro, dará erro

# #Criando pastas dentro da pasta mãe

files = pasta / 'files'
files.mkdir(exist_ok=True) #files = nome do diretório

# #criando arquivos dentro da pasta

for i in range(10):
    file = files / f'file{i}.txt' #file = arquivo

#     # if file.is_file() # Bool se for um arquivo
#     # if file.is_dir() # Bool se for um diretório
    if file.exists(): # Se ele existe
        file.unlink()
    else:
        file.touch() #atualiza

    with file.open('a+') as text_file:
        text_file.write('Olá, você está\n')
        text_file.write(f'no arquivo{i}')

# rmtree(pasta) #apaga a pasta mesmo tendo arquivos dentro
#funções recursivas: se chamam de volta, resolve problemas grandes que 
    #podem ser quebrados, como fatorial (5*4*3*2*1=120)

#Ex 1
# def fatorial(n: int) -> int:
#     #Caso base, onde a função não faz mais recursão
#     if n == 1:
#         return 1
#     #Caso recursivo
#     return n * fatorial(n - 1)
# fat5 = fatorial(5)

# # import sys 
# # sys.setrecursionlimit(5000) #Aqui é perigoso, pois você pode ajustar o limit
# # fat1000 = fatorial(1000) # mil é o limite máximo, passou disso, erro

# print(fat5)

#Ex 2
# from collections import namedtuple
# from typing import List

# Caixa = namedtuple('Caixa', 'Tem_chave')

# def encontrar_chave(Caixas: List[Caixa], index: int = 0) -> Caixa:
#     #caso base
#     if len(Caixas) <= index:
#         return Caixa(False)
    
#     caixa = Caixas[index]

#     print(f'Buscando chave na caixa {index} -> {caixa}')

#     #caso base
#     if caixa.Tem_chave:
#         return Caixa
    
#     #caso recursivo
#     index += 1

#     return encontrar_chave(Caixas, index)
                     
# Caixas:  List[Caixa] = [
#     Caixa(False), Caixa(False), Caixa(False),
#     Caixa(False), Caixa(False), Caixa(False),
#     Caixa(False), Caixa(False), Caixa(False)
#     ]
# print(Caixas)
# print(encontrar_chave(Caixas))

def rmtree(root: Path, remove_root=True): #root seria a pasta mãe
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ',file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ',file)
            file.unlink()
    
    if remove_root:
        root.rmdir()
        
rmtree(pasta)