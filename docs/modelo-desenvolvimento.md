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
| 2 | Cadastro e armazenamento local | Permitir cadastrar filiais e salvar os dados em arquivo JSON. |
| 3 | Interface de monitoramento | Exibir as filiais em lista e indicar o status com as cores verde e vermelha. |
| 4 | Atualização automática e testes | Atualizar os status periodicamente, validar os requisitos e registrar os testes. |

## 4. Forma de trabalho

Cada incremento será desenvolvido, testado e documentado antes do início do próximo.

Ao finalizar um incremento, as alterações serão registradas em um commit no Git e enviadas ao GitHub.