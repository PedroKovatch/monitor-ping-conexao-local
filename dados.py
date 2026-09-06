import json  # Permite ler e escrever arquivos no formato JSON.
from pathlib import Path  # Representa caminhos de arquivos de forma segura.


# Define o arquivo local que guarda as filiais cadastradas.
ARQUIVO_FILIAIS = Path("filiais.json")


def carregar_filiais():
    """
    Carrega as filiais cadastradas no arquivo local.

    Retorno:
        list: lista de filiais; retorna uma lista vazia se ainda não houver dados.
    """
    # Se o arquivo ainda não existir, o sistema começa sem filiais.
    if not ARQUIVO_FILIAIS.exists():
        return []

    # Abre o JSON para leitura e transforma seu conteúdo em uma lista Python.
    with ARQUIVO_FILIAIS.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_filiais(filiais):
    """
    Salva a lista de filiais no arquivo local.

    Parâmetro:
        filiais (list): lista de filiais que será gravada em JSON.
    """
    # Abre o arquivo para escrita e substitui o conteúdo anterior pela lista atual.
    with ARQUIVO_FILIAIS.open("w", encoding="utf-8") as arquivo:
        json.dump(filiais, arquivo, ensure_ascii=False, indent=4)

def adicionar_filial(nome):
    """
    Adiciona uma nova filial ao arquivo local.

    Parâmetro:
        nome (str): nome da filial que será cadastrada.

    Retorno:
        bool: True se a filial foi adicionada; False se o nome estiver vazio
        ou já existir uma filial com o mesmo nome.
    """
    # Remove espaços no início e no fim do nome informado.
    nome = nome.strip()

    # Não permite o cadastro de uma filial sem nome.
    if not nome:
        return False

    filiais = carregar_filiais()

    # Compara os nomes sem diferenciar letras maiúsculas e minúsculas.
    if any(filial["nome"].casefold() == nome.casefold() for filial in filiais):
        return False

    # Uma filial nova começa sem equipamentos cadastrados.
    filiais.append({
        "nome": nome,
        "equipamentos": []
    })

    salvar_filiais(filiais)
    return True
    

    