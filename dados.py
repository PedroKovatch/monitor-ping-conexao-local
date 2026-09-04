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


    