# Arquitetura do Sistema

## 1. Objetivo

A arquitetura do Monitor de Conexão Local foi planejada para manter o código simples, organizado e fácil de evoluir.

Cada arquivo terá uma responsabilidade específica, evitando concentrar toda a lógica em um único arquivo.

## 2. Estrutura planejada

```text
MonitorPing/
├── main.py
├── interface.py
├── monitoramento.py
├── dados.py
├── filiais.json
├── filiais.exemplo.json
├── .gitignore
├── README.md
└── docs/
```

## 3. Responsabilidades dos arquivos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Iniciar o programa e organizar a execução principal. |
| `interface.py` | Criar a interface gráfica usando Tkinter. |
| `monitoramento.py` | Realizar o ping dos endereços IP e retornar o status de conectividade. |
| `dados.py` | Ler e salvar as filiais e seus equipamentos cadastrados no arquivo JSON. |
| `filiais.json` | Armazenar localmente os dados reais das filiais. Esse arquivo não será enviado ao GitHub. |
| `filiais.exemplo.json` | Apresentar um exemplo de estrutura de dados sem utilizar IPs reais. |

## 4. Relação entre os componentes

```mermaid
flowchart TD
    Usuario["Profissional de TI"] --> Interface["interface.py"]
    Interface --> Principal["main.py"]
    Principal --> Monitoramento["monitoramento.py"]
    Principal --> Dados["dados.py"]
    Dados --> JSON["filiais.json"]
```

## 5. Decisão de arquitetura

A estrutura foi mantida pequena porque a primeira versão será uma aplicação local em Python.

Caso o projeto cresça no futuro, será possível adicionar novos arquivos e funcionalidades sem precisar reescrever toda a aplicação.

## 6. Modelo de dados

Cada filial será registrada com seu nome e uma lista de equipamentos monitorados. Cada equipamento terá um nome de identificação e um endereço IP.

```json
[
  {
    "nome": "Filial Exemplo",
    "equipamentos": [
      {
        "nome": "Roteador principal",
        "ip": "192.0.2.10"
      },
      {
        "nome": "Link de internet",
        "ip": "192.0.2.11"
      }
    ]
  }
]
```

Essa estrutura permite monitorar mais de um endereço IP por filial, mantendo a identificação de cada equipamento.

O status de conectividade será associado individualmente a cada equipamento. Na interface, cada equipamento poderá aparecer em uma linha com filial, nome, IP e indicador de status.

O arquivo `filiais.json` conterá os dados reais apenas na máquina local e continuará ignorado pelo Git. O arquivo `filiais.exemplo.json` servirá como modelo público e seguro no repositório.