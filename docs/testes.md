# Registro de Testes

## 1. Objetivo

Este documento registra os testes realizados durante o desenvolvimento do Monitor de Conexão Local.

## 2. Testes executados

| ID | Componente | Cenário | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|---|---|
| CT01 | `testar_ping()` | Ping para `127.0.0.1` | A função deve retornar `True`. | O programa exibiu “Ping respondido com sucesso.” | Aprovado |
| CT02 | `testar_ping()` | Ping para o gateway padrão local | A função deve retornar `True` quando o roteador responder. | O programa exibiu “Ping respondido com sucesso.” | Aprovado |
| CT03 | `testar_ping()` | Ping para `192.0.2.1` | A função deve retornar `False` quando não houver resposta. | O programa exibiu “Ping sem resposta.” | Aprovado |

## 3. Conclusão

A função `testar_ping()` foi validada nos dois cenários principais: resposta positiva e ausência de resposta.

Os testes confirmam que a lógica inicial de monitoramento está funcionando corretamente.