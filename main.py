import os

def renomear_arquivos(pasta, prefixo, sufixo, caracteres_a_excluir):
    # Obtém o caminho absoluto da pasta
    pasta = os.path.abspath(pasta)

    # Lista todos os arquivos na pasta usando os.scandir()
    with os.scandir(pasta) as arquivos:
        for arquivo in arquivos:
            if arquivo.is_file():
                # Ignora arquivos ocultos
                if not arquivo.name.startswith('.'):
                    # Remove os caracteres a serem excluídos do nome do arquivo
                    nome = arquivo.name
                    for char in caracteres_a_excluir:
                        nome = nome.replace(char, '')

                    # Separa o nome e a extensão do arquivo
                    nome, extensao = os.path.splitext(nome)

                    # Monta o novo nome do arquivo com o prefixo e sufixo
                    novo_nome = f"{prefixo}{nome}{sufixo}{extensao}"

                    # Obtém o caminho completo do arquivo
                    caminho_antigo = os.path.join(pasta, arquivo.name)
                    caminho_novo = os.path.join(pasta, novo_nome)

                    # Renomeia o arquivo
                    os.rename(caminho_antigo, caminho_novo)

if __name__ == "__main__":
    pasta_alvo = "files"  # Substitua pelo caminho da pasta desejada
    prefixo_novo = ""  # Substitua pelo prefixo que deseja adicionar ao nome
    sufixo_novo = ""  # Substitua pelo sufixo que deseja adicionar ao nome
    caracteres_excluir = ['FE_','_']  # SuSbstitua pela lista de caracteres que deseja excluir

    renomear_arquivos(pasta_alvo, prefixo_novo, sufixo_novo, caracteres_excluir)
