# Registro de Testes

## 1. Objetivo

Este documento registra os testes realizados durante o desenvolvimento do Monitor de Conexão Local.

## 2. Testes executados

| ID | Componente | Cenário | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|---|---|
| CT01 | `testar_ping()` | Ping para `127.0.0.1` | A função deve retornar `True`. | O programa exibiu “Ping respondido com sucesso.” | Aprovado |
| CT02 | `testar_ping()` | Ping para o gateway padrão local | A função deve retornar `True` quando o roteador responder. | O programa exibiu “Ping respondido com sucesso.” | Aprovado |
| CT03 | `testar_ping()` | Ping para `192.0.2.1` | A função deve retornar `False` quando não houver resposta. | O programa exibiu “Ping sem resposta.” | Aprovado |
| CT04 | `dados.py` | Persistência local em JSON | Salvar e carregar dados fictícios; após limpeza, retornar `[]`. | Funcionou conforme esperado. | Aprovado |

### CT04 — Persistência local de filiais

**Objetivo:** validar a leitura e a gravação dos dados locais em JSON.

**Procedimento:**

1. Salvar uma filial fictícia usando `salvar_filiais()`.
2. Carregar novamente os dados usando `carregar_filiais()`.
3. Confirmar que a filial fictícia foi retornada.
4. Limpar o arquivo `filiais.json`, deixando uma lista vazia (`[]`).
5. Importar `carregar_filiais()` pelo terminal e confirmar o retorno `[]`.

**Resultado:** aprovado. As funções de leitura e gravação funcionaram como esperado.

**Observação:** o arquivo `filiais.json` permanece apenas na máquina local e é ignorado pelo Git.

## 3. Conclusão

A função `testar_ping()` foi validada nos dois cenários principais: resposta positiva e ausência de resposta.

As funções `carregar_filiais()` e `salvar_filiais()` também foram validadas, confirmando que os dados podem ser armazenados localmente em JSON.

Os testes confirmam que a lógica inicial de monitoramento e persistência está funcionando corretamente.