# Modelo de Desenvolvimento

## 1. Modelo escolhido

O modelo de desenvolvimento escolhido para o projeto Monitor de Conexão Local é o modelo Incremental.

## 2. Justificativa da escolha

O modelo Incremental permite desenvolver o sistema em pequenas entregas funcionais. Cada entrega adiciona uma nova capacidade ao projeto, possibilitando testar e validar o funcionamento antes de avançar.

Esse modelo é adequado ao projeto porque o sistema possui funcionalidades que podem ser construídas gradualmente, como ping, armazenamento local, cadastro de filiais e interface visual.

## 3. Incrementos planejados

| Incremento | Entrega | Objetivo |
|---|---|---|
| 1 | Verificação de ping | Criar e testar a lógica de ping para um endereço IP. |
| 2 | Cadastro e armazenamento local | Permitir cadastrar, editar e excluir filiais com nome e IP de um único roteador, mantendo os dados em JSON local. |
| 3 | Interface de monitoramento | Disponibilizar as ações de cadastro na interface e exibir uma lista com filial, IP e indicadores de aguardando, online e indisponível. |
| 4 | Atualização automática e testes | Implementar atualização manual e automática com agendamento a cada 10 segundos, impedir rodadas simultâneas, exibir o horário da última atualização e validar os requisitos. |

As funcionalidades dos quatro incrementos já possuem implementação, com testes básicos registrados em `testes.md`. A entrega permanece em revisão, com validações pendentes antes de ser considerada concluída.

## 4. Forma de trabalho

O desenvolvimento será realizado em etapas pequenas, com revisão do código e testes a cada alteração funcional.

A documentação será revisada em conjuntos coerentes de mudanças, seguindo `padroes-documentacao.md` e preservando a estrutura de cada arquivo.

Os resultados confirmados e as validações pendentes serão registrados em `testes.md`. Uma funcionalidade implementada não será considerada plenamente validada apenas por executar sem erro de sintaxe.

Os commits serão realizados após a revisão de um conjunto funcional de alterações. Não será necessário criar um commit para cada pequeno ajuste de código ou documentação.

Antes de enviar as alterações ao GitHub, serão conferidos os arquivos incluídos no commit, garantindo que os dados reais de `filiais.json` permaneçam fora do repositório.