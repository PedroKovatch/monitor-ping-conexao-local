# Diagrama de Caso de Uso

## Objetivo

Este diagrama representa as principais interações entre o profissional de TI e o sistema Monitor de Conexão Local.

```mermaid
flowchart LR
    TI["Profissional de TI"]

    subgraph Sistema["Monitor de Conexão Local"]
        UC1(["Cadastrar filial e endereço IP"])
        UC2(["Visualizar lista de filiais"])
        UC3(["Consultar status de conectividade"])
    end

    TI --> UC1
    TI --> UC2
    TI --> UC3
```

## Interpretação

O profissional de TI é o usuário do sistema.

Ele poderá cadastrar filiais e seus respectivos endereços IP, visualizar a lista de filiais cadastradas e consultar o status de conectividade de cada uma delas.