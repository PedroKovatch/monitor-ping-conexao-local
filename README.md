# Monitor de Conexão Local

## Descrição

O Monitor de Conexão Local é uma aplicação desktop desenvolvida em Python para acompanhar a resposta de ping dos roteadores das filiais.

A primeira versão permite cadastrar, editar e excluir filiais, informando nome e endereço IP de um único roteador por filial. Os dados são armazenados localmente em JSON.

A interface possui tema escuro, atualização manual e monitoramento automático, com agendamento a cada 10 segundos.

## Objetivo

Facilitar a visualização centralizada da resposta de ping dos roteadores, indicando quais endereços responderam à última verificação.

O resultado do ping não comprova, isoladamente, o funcionamento da internet ou de todos os serviços de uma filial.

## Tecnologias utilizadas

- Python
- Tkinter
- JSON
- Git
- GitHub

## Status do projeto

Primeira versão funcional em revisão e validação.

Funcionalidades implementadas:

- Cadastro de filial com nome e IP do roteador.
- Edição e exclusão de cadastros, com confirmação antes da exclusão.
- Persistência local dos dados em JSON.
- Atualização manual dos status.
- Monitoramento automático com agendamento a cada 10 segundos.
- Proteção contra verificações simultâneas.
- Indicadores Aguardando, Online e Indisponível.
- Exibição do horário da última atualização concluída.

Os testes realizados e as validações pendentes estão registrados em [Registro de Testes](docs/testes.md).

## Instruções de uso

### Requisitos para execução

- Windows.
- Python instalado com Tkinter disponível.
- Acesso de rede aos roteadores que serão monitorados.
- Permissão de ping nos equipamentos e firewalls envolvidos.

O projeto utiliza a biblioteca padrão do Python e não exige a instalação de pacotes externos por `pip`.

### Como iniciar

Abra o terminal na pasta do projeto e execute:

```powershell
python interface.py
```

Atualmente, `interface.py` é o ponto de entrada da aplicação. O arquivo `main.py` permanece previsto na arquitetura, mas ainda não foi implementado.

### Como utilizar

- Preencha o nome da filial e o IP do roteador e clique em Adicionar filial.
- Aguarde a verificação automática ou clique em Atualizar status.
- Para editar, selecione uma linha, clique em Editar filial, altere os campos e clique em Salvar edição.
- Para excluir, selecione uma linha, clique em Excluir filial e confirme a operação.
- Feche a janela para encerrar o programa.

O monitoramento automático começa ao abrir a aplicação e permanece ativo enquanto a janela estiver aberta.

### Indicadores de conectividade

| Indicador | Significado |
|---|---|
| Aguardando | Não há resultado de ping disponível para o registro apresentado. |
| Online — verde | O endereço IP respondeu à verificação de ping. |
| Indisponível — vermelho | O endereço IP não respondeu à verificação de ping. |

A ausência de resposta pode estar relacionada ao equipamento, ao caminho de rede ou ao bloqueio de ping. O programa não identifica automaticamente a causa.

### Armazenamento dos dados

Os cadastros são gravados em `filiais.json`, na mesma pasta de `dados.py`. Se o arquivo ainda não existir, a aplicação começa sem cadastros e o cria ao salvar os dados.

O arquivo `filiais.json` deve permanecer ignorado pelo Git. Não inclua endereços reais em documentação, exemplos ou imagens publicadas no repositório.

O arquivo `filiais.exemplo.json` apresenta somente o formato esperado, com dados fictícios. Ele não é carregado automaticamente pela aplicação.

### Limitações da primeira versão

- Cada filial possui um único roteador cadastrado.
- O monitoramento verifica apenas a resposta ao ping.
- Os pings são executados sequencialmente.
- Uma rodada pode durar mais de 10 segundos. Solicitações recebidas enquanto outra rodada estiver em andamento são ignoradas.
- A validação no computador do técnico e com os roteadores autorizados ainda está pendente.