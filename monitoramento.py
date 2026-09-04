import subprocess # Permite executar comandos do Windows pelo Python.


def testar_ping(ip):
    """
    Envia um único ping para o endereço IP informado.

    Parâmetro:
        ip (str): endereço IP que será testado.

    Retorno:
        bool: True se o IP responder; False se não responder.
    """
    # Executa um ping no Windows, aguardando no máximo 1 segundo.
    resultado = subprocess.run(
        ["ping", "-n", "1", "-w", "1000", ip],
        capture_output=True, # Guarda o texto retornado pelo comando.
        text=True
    )
    # O código 0 indica que o comando foi executado com sucesso.
    return resultado.returncode == 0


if __name__ == "__main__":
    # IP do próprio computador, usado apenas para validar a função.
    ip_teste = "192.0.2.1"

    if testar_ping(ip_teste):
        print("Ping respondido com sucesso.")
    else:
        print("Ping sem resposta.")