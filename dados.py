import json  # Permite ler e escrever arquivos no formato JSON.
from pathlib import Path  # Representa caminhos de arquivos de forma segura.


# Define a pasta em que os arquivos do projeto estão localizados.
PASTA_PROJETO = Path(__file__).resolve().parent

# Mantém o arquivo de filiais sempre dentro da pasta do projeto.
ARQUIVO_FILIAIS = PASTA_PROJETO / "filiais.json"


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


def adicionar_filial(nome, ip):
    """
    Adiciona uma filial e o endereço IP de seu roteador ao arquivo local.

    Parâmetros:
        nome (str): nome da filial que será cadastrada.
        ip (str): endereço IP do roteador da filial.

    Retorno:
        bool: True se a filial foi adicionada; False se algum campo estiver vazio
        ou já existir uma filial com o mesmo nome.
    """
    # Remove espaços no início e no fim dos dados informados.
    nome = nome.strip()
    ip = ip.strip()

    # Não permite cadastro com nome ou endereço IP vazios.
    if not nome or not ip:
        return False

    filiais = carregar_filiais()

    # Não permite duas filiais com o mesmo nome.
    if any(filial["nome"].casefold() == nome.casefold() for filial in filiais):
        return False

    # Cada filial possui um único roteador nesta primeira versão.
    filiais.append({
        "nome": nome,
        "ip": ip
    })

    salvar_filiais(filiais)
    return True


def excluir_filial(nome):
    """
    Exclui uma filial cadastrada no arquivo local.

    Parâmetro:
        nome (str): nome da filial que será excluída.

    Retorno:
        bool: True se a filial foi excluída; False se ela não foi encontrada.
    """
    nome = nome.strip()
    filiais = carregar_filiais()

    # Mantém apenas as filiais que possuem um nome diferente do informado.
    filiais_atualizadas = [
        filial
        for filial in filiais
        if filial["nome"].casefold() != nome.casefold()
    ]

    # Nenhuma filial foi removida quando as listas possuem o mesmo tamanho.
    if len(filiais_atualizadas) == len(filiais):
        return False

    salvar_filiais(filiais_atualizadas)
    return True


def editar_filial(nome_atual, novo_nome, novo_ip):
    """
    Atualiza o nome e o endereço IP de uma filial cadastrada.

    Parâmetros:
        nome_atual (str): nome usado para localizar a filial.
        novo_nome (str): novo nome da filial.
        novo_ip (str): novo endereço IP do roteador.

    Retorno:
        bool: True se a filial foi atualizada; False se os dados forem inválidos,
        a filial não for encontrada ou o novo nome já estiver em uso.
    """
    nome_atual = nome_atual.strip()
    novo_nome = novo_nome.strip()
    novo_ip = novo_ip.strip()

    if not nome_atual or not novo_nome or not novo_ip:
        return False

    filiais = carregar_filiais()

    # Procura a posição da filial que será editada.
    indice_filial = next(
        (
            indice
            for indice, filial in enumerate(filiais)
            if filial["nome"].casefold() == nome_atual.casefold()
        ),
        None
    )

    if indice_filial is None:
        return False

    # Não permite utilizar o nome de outra filial já cadastrada.
    nome_duplicado = any(
        indice != indice_filial
        and filial["nome"].casefold() == novo_nome.casefold()
        for indice, filial in enumerate(filiais)
    )

    if nome_duplicado:
        return False

    filiais[indice_filial] = {
        "nome": novo_nome,
        "ip": novo_ip
    }

    salvar_filiais(filiais)
    return True