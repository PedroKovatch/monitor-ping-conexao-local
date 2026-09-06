# Requisitos do Sistema

## 1. Identificação

- **Projeto:** Monitor de Conexão Local
- **Versão do documento:** 1.2
- **Data:** 04/09/2026
- **Responsável:** Pedro Kovatch
- **Status:** Em elaboração

## 2. Problema a ser resolvido

A equipe de TI precisa acompanhar a disponibilidade de equipamentos de rede das filiais. Atualmente, a verificação de conectividade é realizada manualmente por meio de comandos de ping, o que dificulta uma visualização rápida e centralizada do status de cada equipamento.

O sistema Monitor de Conexão Local será uma aplicação desktop desenvolvida em Python. Ele permitirá cadastrar manualmente filiais, seus equipamentos e respectivos endereços IP, armazená-los localmente e monitorar automaticamente a resposta de ping de cada endereço.

## 3. Requisitos funcionais

| Código | Requisito |
|---|---|
| RF01 | O sistema deve permitir o cadastro manual de uma filial, informando seu nome. |
| RF02 | O sistema deve permitir o cadastro de um ou mais equipamentos para cada filial, informando nome e endereço IP. |
| RF03 | O sistema deve armazenar os dados cadastrados localmente, para que permaneçam disponíveis quando o programa for aberto novamente. |
| RF04 | O sistema deve exibir uma lista vertical das filiais, equipamentos e respectivos endereços IP cadastrados. |
| RF05 | O sistema deve realizar verificações automáticas de ping nos endereços IP cadastrados enquanto estiver aberto. |
| RF06 | O sistema deve indicar o status de conectividade com um indicador visual verde quando o endereço IP responder ao ping. |
| RF07 | O sistema deve indicar o status de conectividade com um indicador visual vermelho quando o endereço IP não responder ao ping. |

## 4. Requisitos não funcionais

| Código | Requisito |
|---|---|
| RNF01 | O sistema deve ser executado localmente em computadores com sistema operacional Windows. |
| RNF02 | O sistema deve ser desenvolvido utilizando a linguagem Python. |
| RNF03 | A interface deve ser simples, com foco na visualização rápida do status das filiais e equipamentos. |
| RNF04 | Os dados das filiais devem ser armazenados em arquivo local no formato JSON, sem utilização de banco de dados. |
| RNF05 | Os endereços IP reais das filiais não devem ser enviados ao repositório do GitHub. |
| RNF06 | A atualização automática não deve travar a interface durante as verificações de ping. |

## 5. Escopo da primeira versão

A primeira versão do Monitor de Conexão Local terá como foco o cadastro local de filiais e equipamentos, além do monitoramento visual automático da resposta de ping dos respectivos endereços IP.

### 5.1 Funcionalidades previstas

- Cadastro manual de filiais.
- Cadastro Cadastro manual de um ou mais equipamentos por filial.
- Armazenamento local dos dados em arquivo JSON.
- Listagem das filiais, equipamentos e endereços IP cadastrados.
- Atualização automática do status de ping.
- Indicador visual verde para resposta e vermelho para erro.

### 5.2 Funcionalidades fora do escopo

- Banco de dados.
- Sistema web.
- Login de usuários.
- Envio de e-mails, mensagens ou notificações externas.
- Relatórios avançados e gráficos.
- Integração com sistemas externos.

## 6. Regras de negócio

| Código | Regra |
|---|---|
| RB01 | Um equipamento será considerado online quando seu endereço IP responder à solicitação de ping. |
| RB02 | Um equipamento será considerado indisponível quando seu endereço IP não responder à solicitação de ping. |
| RB03 | O status online deve ser representado visualmente pela cor verde. |
| RB04 | O status indisponível deve ser representado visualmente pela cor vermelha. |
| RB05 | O monitoramento deve continuar sendo executado enquanto o programa estiver aberto. |
| RB06 | Os dados cadastrados devem ser carregados automaticamente ao iniciar o programa. |
| RB07 | Uma filial pode possuir um ou mais equipamentos monitorados. |
| RB08 | O sistema não deve permitir o cadastro de duas filiais com o mesmo nome, sem diferenciar letras maiúsculas e minúsculas. |

## 7. Critérios de aceitação

A primeira versão será considerada aceita quando:

- For possível cadastrar uma filial.
- Não for possível cadastrar uma segunda filial com o mesmo nome.
- For possível cadastrar um ou mais equipamentos com nome e endereço IP para cada filial.
- Os dados cadastrados continuarem disponíveis após fechar e abrir o programa.
- A lista de filiais, equipamentos e IPs for exibida na interface.
- O sistema atualizar automaticamente o status dos IPs enquanto estiver aberto.
- Um IP que responde ao ping for exibido com indicador verde.
- Um IP que não responde ao ping for exibido com indicador vermelho.
- O arquivo com os IPs reais não for enviado ao GitHub.