# Diagrama de Atividades — Monitoramento de Conectividade

## Objetivo

Este diagrama representa o fluxo automático de monitoramento dos endereços IP cadastrados no sistema.

```mermaid
flowchart TD
    Inicio([Início]) --> Carregar[Carregar filiais e endereços IP do arquivo JSON]
    Carregar --> Exibir[Exibir lista de filiais na interface]
    Exibir --> IniciarCiclo[Iniciar ciclo de monitoramento]

    IniciarCiclo --> Selecionar[Obter próxima filial da lista]
    Selecionar --> Ping[Enviar ping para o endereço IP]
    Ping --> Respondeu{O IP respondeu?}

    Respondeu -- Sim --> Verde[Exibir indicador verde]
    Respondeu -- Não --> Vermelho[Exibir indicador vermelho]

    Verde --> Restam{Existem outras filiais?}
    Vermelho --> Restam

    Restam -- Sim --> Selecionar
    Restam -- Não --> Aguardar[Aguardar intervalo de atualização]
    Aguardar --> Aberto{O programa continua aberto?}

    Aberto -- Sim --> IniciarCiclo
    Aberto -- Não --> Fim([Fim])
```

## Interpretação

Ao iniciar, o sistema carrega as filiais cadastradas no arquivo JSON e exibe a lista na interface.

Em seguida, realiza um ping para cada endereço IP. Caso o endereço responda, o sistema exibe o indicador verde. Caso não responda, exibe o indicador vermelho.

Após verificar todas as filiais, o sistema aguarda o intervalo definido e reinicia o monitoramento enquanto o programa estiver aberto.
