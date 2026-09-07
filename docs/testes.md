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
| CT05 | `adicionar_filial()` | Cadastro e tentativa de duplicidade no modelo anterior | Cadastrar uma filial nova e bloquear outro cadastro com o mesmo nome. | A filial foi adicionada; a tentativa duplicada retornou `False`. | Aprovado na versão testada |
| CT06 | `interface.py` e `dados.py` | Cadastro pela interface | Salvar uma filial com nome e IP e apresentá-la novamente após reiniciar. | O cadastro apareceu na tabela e permaneceu após reabrir o programa. | Aprovado |
| CT07 | `interface.py` e `monitoramento.py` | Atualização manual dos status | Exibir resposta positiva em verde e ausência de resposta em vermelho. | Os registros de teste apresentaram Online e Indisponível conforme esperado. | Aprovado |
| CT08 | `interface.py` e `monitoramento.py` | Mudança de conectividade de um roteador local | Atualizar o status conforme a resposta ao ping após ligar ou desligar o roteador. | O roteador apareceu online quando ligado e indisponível após ser desligado e realizada nova atualização. | Aprovado |
| CT09 | `interface.py` | Continuidade da atualização automática | Executar novos ciclos sem clicar no botão e atualizar o horário exibido. | O horário da última atualização mudou automaticamente em ciclos sucessivos. | Aprovado |
| CT10 | `interface.py` e `excluir_filial()` | Exclusão e persistência | Remover o cadastro confirmado e mantê-lo excluído após reiniciar. | O cadastro foi removido e não reapareceu após reabrir o programa. | Aprovado |
| CT11 | `interface.py` e `editar_filial()` | Edição de nome pelo botão | Atualizar o nome e preservar a alteração após reiniciar. | A alteração foi exibida e permaneceu salva. | Aprovado |
| CT12 | `confirmar_formulario()` | Salvar edição com Enter | Atualizar o cadastro em edição sem criar outro registro. | A edição foi salva com Enter, sem duplicação do cadastro. | Aprovado |
| CT13 | `interface.py` e `dados.py` | Lista vazia após excluir os registros de teste | Reabrir com tabela vazia e continuar atualizando o horário sem erro. | A tabela permaneceu vazia e o horário continuou mudando automaticamente. | Aprovado |
| CT14 | `excluir_filial()` e `editar_filial()` | Filial inexistente | Retornar `False` quando a filial procurada não existir. | As duas funções retornaram `False` nos testes realizados. | Aprovado |
| CT15 | `dados.py` | Resolução do caminho de armazenamento | Apresentar o caminho absoluto de `filiais.json` na pasta do projeto. | O comando de consulta exibiu o caminho absoluto esperado. | Aprovado |

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

### CT05 — Cadastro de filial e controle de duplicidade

**Objetivo:** validar o cadastro de uma filial e a regra que impede nomes duplicados.

**Procedimento:**

1. Cadastrar a filial fictícia `Filial de Teste` usando `adicionar_filial()`.
2. Confirmar o retorno `True`.
3. Carregar os dados e confirmar que a filial foi salva com a lista `equipamentos` vazia.
4. Tentar cadastrar `filial de teste`, utilizando o mesmo nome em letras minúsculas.
5. Confirmar o retorno `False`.
6. Limpar o arquivo `filiais.json`, deixando uma lista vazia (`[]`).
7. Carregar os dados e confirmar o retorno `[]`.

**Resultado:** aprovado na versão testada. O cadastro de uma filial nova funcionou e a tentativa de cadastrar o mesmo nome com letras minúsculas retornou `False`.

**Observação:** a comparação não diferencia letras maiúsculas e minúsculas. Portanto, `Filial de Teste` e `filial de teste` são considerados o mesmo nome.

Este teste registra o modelo anterior, no qual a filial possuía uma lista `equipamentos`. A primeira versão atual utiliza os campos `nome` e `ip`. O registro histórico foi preservado, mas não substitui a validação das regras no modelo atual.

## 3. Conclusão

Os testes realizados confirmaram os fluxos básicos de cadastro, persistência, edição de nome e exclusão, além da apresentação dos resultados de ping na interface.

A continuidade do monitoramento automático foi observada pela mudança do horário da última atualização. Também foi realizado um teste com um roteador local, observando a mudança de status após sua desconexão.

Os resultados correspondem às versões e aos cenários efetivamente testados. Eles não representam a validação completa de todos os requisitos.

### 3.1 Validações pendentes

- Revalidar campos vazios e nomes duplicados no cadastro e na edição do modelo atual.
- Testar especificamente a alteração do endereço IP e sua persistência.
- Confirmar separadamente o cancelamento da exclusão e a tentativa de excluir sem seleção.
- Testar a limpeza do estado de edição após excluir um cadastro, depois do ajuste realizado na revisão técnica.
- Verificar a proteção contra rodadas simultâneas com uma evidência além da aparência da interface.
- Testar a abertura do programa a partir de outro diretório.
- Testar o fechamento da janela durante uma verificação.
- Validar a duração das rodadas e a responsividade com a quantidade prevista de filiais.
- Executar os testes de conectividade no computador do técnico com os roteadores autorizados.
- Confirmar antes do commit que `filiais.json` está ignorado e não está sendo rastreado pelo Git.

### 3.2 Cuidados com os dados de teste

Os endereços reais utilizados nos testes devem permanecer apenas no arquivo local `filiais.json`. Não devem ser incluídos neste documento, no arquivo de exemplo ou nas evidências públicas do repositório.

O teste de sintaxe com `python -m py_compile` verifica se os arquivos podem ser compilados, mas não comprova, sozinho, o funcionamento das regras ou da interface.