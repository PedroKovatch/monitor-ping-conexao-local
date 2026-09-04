# Requisitos do Sistema

## 1. Identificação

- **Projeto:** Monitor de Conexão Local
- **Versão do documento:** 1.0
- **Data:** 04/09/2026
- **Responsável:** Pedro Kovatch
- **Status:** Em elaboração

## 2. Problema a ser resolvido

A equipe de TI precisa acompanhar a disponibilidade de equipamentos de rede das filiais. Atualmente, a verificação de conectividade é realizada manualmente por meio de comandos de ping, o que dificulta uma visualização rápida e centralizada do status de cada unidade.

O sistema Monitor de Conexão Local será uma aplicação desktop desenvolvida em Python. Ele permitirá cadastrar manualmente os endereços IP das filiais, armazená-los localmente e monitorar automaticamente a resposta de ping de cada endereço.

## 3. Requisitos funcionais

| Código | Requisito |
|---|---|
| RF01 | O sistema deve permitir o cadastro manual de uma filial, informando nome e endereço IP. |
| RF02 | O sistema deve armazenar os dados cadastrados localmente, para que permaneçam disponíveis quando o programa for aberto novamente. |
| RF03 | O sistema deve exibir uma lista vertical das filiais cadastradas e seus respectivos endereços IP. |
| RF04 | O sistema deve realizar verificações automáticas de ping nos endereços IP cadastrados enquanto estiver aberto. |
| RF05 | O sistema deve indicar o status de conectividade com uma bolinha verde quando o endereço IP responder ao ping. |
| RF06 | O sistema deve indicar o status de conectividade com uma bolinha vermelha quando o endereço IP não responder ao ping. |

## 4. Requisitos não funcionais

| Código | Requisito |
|---|---|
| RNF01 | O sistema deve ser executado localmente em computadores com sistema operacional Windows. |
| RNF02 | O sistema deve ser desenvolvido utilizando a linguagem Python. |
| RNF03 | A interface deve ser simples, com foco na visualização rápida do status das filiais. |
| RNF04 | Os dados das filiais devem ser armazenados em arquivo local no formato JSON, sem utilização de banco de dados. |
| RNF05 | Os endereços IP reais das filiais não devem ser enviados ao repositório do GitHub. |
| RNF06 | A atualização automática não deve travar a interface durante as verificações de ping. |

## 5. Escopo da primeira versão

A primeira versão do Monitor de Conexão Local terá como foco o cadastro local de filiais e o monitoramento visual automático da resposta de ping dos respectivos endereços IP.

Funcionalidades previstas nesta versão:

- Cadastro manual de nome da filial e endereço IP.
- Armazenamento local dos dados em arquivo JSON.
- Listagem das filiais cadastradas.
- Atualização automática do status de ping.
- Indicador visual verde para resposta e vermelho para erro.

Funcionalidades fora do escopo desta versão:

- Banco de dados.
- Sistema web.
- Login de usuários.
- Envio de e-mails, mensagens ou notificações externas.
- Relatórios avançados e gráficos.
- Integração com sistemas externos.

## 6. Regras de negócio

| Código | Regra |
|---|---|
| RB01 | Uma filial será considerada online quando o endereço IP responder à solicitação de ping. |
| RB02 | Uma filial será considerada indisponível quando o endereço IP não responder à solicitação de ping. |
| RB03 | O status online deve ser representado visualmente pela cor verde. |
| RB04 | O status indisponível deve ser representado visualmente pela cor vermelha. |
| RB05 | O monitoramento deve continuar sendo executado enquanto o programa estiver aberto. |
| RB06 | Os dados cadastrados devem ser carregados automaticamente ao iniciar o programa. |

## 7. Critérios de aceitação

A primeira versão será considerada aceita quando:

- For possível cadastrar uma filial informando nome e endereço IP.
- Os dados cadastrados continuarem disponíveis após fechar e abrir o programa.
- A lista de filiais for exibida na interface.
- O sistema atualizar automaticamente o status dos IPs enquanto estiver aberto.
- Um IP que responde ao ping for exibido com indicador verde.
- Um IP que não responde ao ping for exibido com indicador vermelho.
- O arquivo com os IPs reais não for enviado ao GitHub.