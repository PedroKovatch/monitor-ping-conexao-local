# Padrões de Documentação

## 1. Objetivo

Este documento define os padrões de organização, formatação e revisão da documentação do projeto Monitor de Conexão Local.

O objetivo é manter todos os documentos claros, consistentes, fáceis de consultar e adequados para estudo e evolução do projeto.

## 2. Aplicação

Estes padrões devem ser utilizados em todos os documentos da pasta `docs/` e no `README.md`.

Cada documento pode possuir uma finalidade diferente, mas deve utilizar linguagem, estrutura e formatação compatíveis com este padrão.

## 3. Regras gerais de formatação

### 3.1 Títulos e seções

- Cada documento deve possuir apenas um título principal, utilizando `#`.
- As seções principais devem utilizar `##`.
- As subseções devem utilizar `###`.
- Documentos técnicos internos devem numerar as seções principais quando isso facilitar a consulta.
- O `README.md` pode utilizar seções sem numeração, por ser a apresentação pública do projeto.

### 3.2 Texto e listas

- Parágrafos devem ser curtos, objetivos e separados por uma linha em branco.
- Listas devem utilizar o marcador `-`.
- Termos técnicos, nomes de arquivos, funções, comandos e campos devem ser escritos entre crases, como `dados.py`, `testar_ping()` e `git status`.
- Destaques em negrito devem ser usados apenas para informações relevantes, sem excesso.

### 3.3 Tabelas

- Tabelas devem ser utilizadas para organizar informações comparáveis, como requisitos, responsabilidades, testes e incrementos.
- Os títulos das colunas devem ser claros e objetivos.
- Os códigos de requisitos, regras e testes devem seguir o padrão já definido: `RF`, `RNF`, `RB` e `CT`.

### 3.4 Blocos técnicos

- Código Python deve utilizar o identificador `python`.
- Exemplos de dados devem utilizar o identificador `json`.
- Estruturas de arquivos devem utilizar o identificador `text`.
- Diagramas devem utilizar o identificador `mermaid`.
- Todo bloco técnico deve ser aberto e fechado corretamente.

## 4. Estrutura por tipo de documento

### 4.1 Documentos técnicos

Exemplos: `arquitetura.md` e `modelo-desenvolvimento.md`.

Estrutura recomendada:

1. Objetivo.
2. Conteúdo técnico principal.
3. Tabelas, estruturas ou diagramas, quando necessários.
4. Decisões de arquitetura, justificativas ou conclusão.

### 4.2 Documento de requisitos

Arquivo: `requisitos.md`.

Estrutura recomendada:

1. Identificação.
2. Problema a ser resolvido.
3. Requisitos funcionais.
4. Requisitos não funcionais.
5. Escopo da versão.
6. Regras de negócio.
7. Critérios de aceitação.

### 4.3 Documento de testes

Arquivo: `testes.md`.

Estrutura recomendada:

1. Objetivo.
2. Tabela-resumo dos casos de teste.
3. Detalhamento de testes relevantes, utilizando subseções.
4. Conclusão.

Cada teste deve informar cenário, resultado esperado, resultado obtido e status.

### 4.4 Documentos de diagramas

Arquivos da pasta `docs/diagramas/`.

Estrutura recomendada:

1. Objetivo.
2. Diagrama em `mermaid`.
3. Interpretação do diagrama.

Os diagramas devem representar o modelo de dados e as regras atuais do sistema.

### 4.5 README

Arquivo: `README.md`.

O README deve apresentar o projeto de forma simples para quem acessa o repositório no GitHub.

Estrutura recomendada:

- Descrição.
- Objetivo.
- Tecnologias utilizadas.
- Status do projeto.
- Instruções de uso, quando o sistema estiver executável.

### 4.6 Anotações de estudo

Arquivo: `anotacoes-estudo.md`.

Esse documento registra explicações pessoais sobre conceitos aprendidos durante o projeto.

Cada assunto deve possuir:

1. Título do conceito.
2. Explicação em linguagem simples.
3. Exemplo prático relacionado ao projeto, quando aplicável.

## 5. Processo de atualização

Antes de alterar um documento existente, devem ser seguidas estas etapas:

1. Ler o conteúdo completo atual do arquivo.
2. Identificar onde a nova informação se encaixa.
3. Revisar o documento completo, preservando sua estrutura.
4. Conferir a visualização com o Markdown Preview do VS Code.
5. Salvar o arquivo.
6. Registrar a alteração no Git com um commit relacionado ao assunto.

Não devem ser adicionados trechos isolados sem considerar a estrutura atual do documento.

## 6. Termos padronizados do projeto

- **Filial:** unidade da empresa cadastrada no sistema.
- **Equipamento:** dispositivo ou ponto de conectividade monitorado dentro de uma filial.
- **Endereço IP:** identificação de rede associada a um equipamento.
- **Status de conectividade:** resultado do ping de cada equipamento.
- **Online:** equipamento cujo endereço IP respondeu ao ping.
- **Indisponível:** equipamento cujo endereço IP não respondeu ao ping.

Uma filial pode possuir um ou mais equipamentos. O status é associado ao equipamento e ao seu endereço IP, não à filial de forma genérica.

## 7. Revisão contínua

Sempre que uma decisão alterar o funcionamento, a estrutura de dados ou o escopo do projeto, os documentos relacionados devem ser revisados antes do commit.

Este arquivo deve ser consultado antes da criação ou atualização de qualquer documentação do projeto.