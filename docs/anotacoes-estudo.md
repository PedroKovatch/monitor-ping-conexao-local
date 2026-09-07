# Anotações de Estudo

## 1. Objetivo

Este documento reúne explicações sobre as ferramentas e os conceitos utilizados no desenvolvimento do Monitor de Conexão Local.

O objetivo é facilitar a revisão do que foi praticado e apoiar o estudo do código. Utilizar um recurso durante o projeto não significa que ele já foi completamente compreendido.

## 2. Principais ferramentas utilizadas

| Ferramenta | Para que serve | Uso no projeto |
|---|---|---|
| Python | Linguagem utilizada para escrever e executar a lógica do programa. | Cadastro, persistência, verificação de ping e interface. |
| VS Code | Editor utilizado para organizar e modificar arquivos de código e documentação. | Edição dos arquivos Python, JSON e Markdown. |
| PowerShell | Terminal que permite executar comandos no Windows. | Iniciar o programa, consultar arquivos, verificar sintaxe e executar comandos Git. |
| Git | Sistema de controle de versão que registra alterações em arquivos. | Consultar diferenças e criar pontos de referência no histórico do projeto. |
| GitHub | Plataforma que hospeda repositórios Git e permite compartilhar o projeto. | Armazenamento remoto do código e da documentação versionados. |

O VS Code é o editor, enquanto o Python executa o programa. Git e GitHub também possuem funções diferentes: o Git controla o histórico e o GitHub hospeda uma cópia remota do repositório.

## 3. Bibliotecas e recursos do Python

Os recursos abaixo fazem parte da biblioteca padrão do Python. A disponibilidade do Tkinter depende de como o Python foi instalado.

| Recurso | Para que serve | Uso no projeto |
|---|---|---|
| `tkinter` | Criar interfaces gráficas. | Janela principal e variáveis ligadas aos campos. |
| `ttk` | Disponibilizar componentes de interface com estilos configuráveis. | Botões, campos, quadros e tabela. |
| `messagebox` | Exibir caixas de diálogo. | Avisos e confirmação de exclusão. |
| `json` | Ler e escrever dados no formato JSON. | Persistência dos cadastros. |
| `pathlib.Path` | Representar e manipular caminhos de arquivos. | Localização de `filiais.json`. |
| `subprocess` | Executar programas externos. | Chamada ao comando `ping` do Windows. |
| `threading.Thread` | Executar uma tarefa em uma thread separada. | Realização dos pings enquanto a janela continua atendendo às interações. |
| `datetime` | Trabalhar com datas e horários. | Exibição do horário da última atualização. |

## 4. Organização dos arquivos

| Arquivo | Responsabilidade atual |
|---|---|
| `interface.py` | Criar a janela, receber ações do usuário e coordenar o monitoramento. |
| `dados.py` | Carregar, salvar, cadastrar, editar e excluir filiais. |
| `monitoramento.py` | Executar a verificação de ping de um endereço IP. |
| `filiais.json` | Guardar os cadastros locais utilizados pelo programa. |
| `filiais.exemplo.json` | Apresentar o modelo de dados com informações fictícias. |
| `.gitignore` | Definir arquivos e pastas que o Git deve ignorar quando ainda não são rastreados. |
| `README.md` | Apresentar o projeto e explicar como executá-lo. |
| `docs/` | Reunir requisitos, arquitetura, diagramas, testes e anotações. |

O arquivo `main.py` está previsto na arquitetura, mas ainda não foi implementado. Atualmente, a execução começa por `interface.py`.

## 5. Conceitos de Python aplicados

### 5.1 Importações

O comando `import` permite utilizar recursos de uma biblioteca ou de outro arquivo Python.

```python
import json
from pathlib import Path
from dados import carregar_filiais
```

Nesse exemplo:

- `json` disponibiliza recursos para trabalhar com JSON.
- `Path` é importado da biblioteca `pathlib`.
- `carregar_filiais` é uma função definida no arquivo `dados.py`.

As importações da biblioteca padrão ficam agrupadas e separadas por uma linha em branco das importações dos arquivos do projeto.

### 5.2 Funções, parâmetros e retorno

A palavra `def` define uma função: um bloco de código que pode ser chamado para executar uma tarefa.

Exemplo de chamada:

```python
filiais = carregar_filiais()
```

A função é executada e seu retorno é atribuído à variável `filiais`.

Parâmetros são informações recebidas pela função. Na função `testar_ping(ip)`, o parâmetro `ip` informa qual endereço será verificado.

O comando `return` devolve um resultado e encerra aquela execução da função.

### 5.3 Valores booleanos e condições

Os valores `True` e `False` representam verdadeiro e falso.

O comando `if` permite escolher um comportamento conforme uma condição.

```python
if testar_ping(ip):
    print("Ping respondido com sucesso.")
else:
    print("Ping sem resposta.")
```

Esse exemplo depende de uma variável `ip` definida anteriormente. Ele ilustra a decisão tomada a partir do resultado da função.

### 5.4 Listas e dicionários

Uma lista reúne vários elementos. Um dicionário organiza informações por chaves e valores.

No modelo atual, cada filial é um dicionário, e o conjunto de filiais é uma lista:

```python
filiais = [
    {
        "nome": "Filial Exemplo",
        "ip": "192.0.2.10"
    }
]
```

A expressão `filiais[0]` acessa o primeiro cadastro. A expressão `filiais[0]["nome"]` acessa seu nome.

Os índices de uma lista começam em zero.

### 5.5 Repetição com for

O comando `for` percorre elementos de uma coleção.

```python
for filial in filiais:
    print(filial["nome"])
```

No monitoramento, esse recurso permite verificar o roteador de cada filial, um por vez.

### 5.6 Tratamento de texto

Dois métodos são utilizados nas regras de cadastro:

- `strip()` remove espaços no início e no fim do texto.
- `casefold()` permite comparar textos sem diferenciar letras maiúsculas e minúsculas.

```python
nome = "  Filial Exemplo  ".strip()
mesmo_nome = nome.casefold() == "filial exemplo".casefold()
```

Nesse exemplo, `mesmo_nome` recebe `True`.

### 5.7 Constantes

Nomes em letras maiúsculas indicam, por convenção, valores de configuração que não devem mudar durante a execução.

```python
INTERVALO_ATUALIZACAO = 10000
```

Essa configuração representa 10.000 milissegundos, equivalentes a 10 segundos.

O Python não impede que esse valor seja redefinido. Por isso, a configuração deve aparecer apenas uma vez no arquivo.

### 5.8 Indentação

A indentação é o recuo usado para indicar quais linhas pertencem a uma função, condição ou repetição.

No projeto, utilizamos quatro espaços por nível.

```python
if nome:
    print(nome)
```

A linha `print(nome)` pertence ao bloco do `if` porque está recuada.

Linhas em branco ajudam na organização visual, mas não substituem a indentação.

### 5.9 Comentários e docstrings

Comentários começam com `#` e explicam uma decisão ou trecho do código.

Docstrings ficam entre aspas triplas, no início de uma função, e descrevem seu objetivo, parâmetros e retorno.

No projeto, as anotações devem ajudar a entender a lógica sem repetir desnecessariamente tudo que o código já expressa.

### 5.10 Escopo e nonlocal

Uma variável criada dentro de uma função pertence ao seu escopo local.

No `interface.py`, algumas funções estão dentro de `iniciar_interface()` e precisam alterar variáveis criadas por ela.

```python
nonlocal monitoramento_em_andamento
```

O comando `nonlocal` indica que a atribuição deve modificar a variável da função externa, em vez de criar outra variável local com o mesmo nome.

Esse recurso é utilizado no controle do monitoramento e no estado de edição.

### 5.11 Execução direta de um arquivo

O bloco abaixo diferencia a execução direta de uma importação:

```python
if __name__ == "__main__":
    iniciar_interface()
```

Ao executar `python interface.py`, a condição é verdadeira e a interface é iniciada.

Ao importar esse arquivo como módulo, esse bloco não é executado.

### 5.12 Recursos para localizar e comparar cadastros

A função de edição utiliza:

- `enumerate()`: percorre uma lista fornecendo a posição e o elemento.
- `next()`: obtém o próximo resultado de uma busca, podendo retornar um valor padrão quando não encontra nenhum.
- `any()`: retorna `True` se pelo menos uma das condições verificadas for verdadeira.

Esses recursos permitem localizar a filial original e verificar se o novo nome pertence a outro cadastro.

São conceitos que merecem uma revisão prática com exemplos menores.

## 6. Interface gráfica com Tkinter

### 6.1 Janela e componentes

| Componente | Função |
|---|---|
| `tk.Tk()` | Criar a janela principal. |
| `ttk.Frame` | Agrupar componentes. |
| `ttk.Label` | Exibir textos. |
| `ttk.Entry` | Receber texto digitado pelo usuário. |
| `ttk.Button` | Acionar uma função por meio de um botão. |
| `ttk.Treeview` | Exibir os cadastros em uma tabela. |
| `tk.StringVar()` | Manter um valor de texto associado a componentes da interface. |

O tema escuro é definido por cores e estilos configurados no próprio código.

### 6.2 Posicionamento com pack e grid

O método `pack()` organiza componentes por posição, como lado esquerdo, topo ou preenchimento da área disponível.

O método `grid()` organiza componentes em linhas e colunas.

No projeto, os dois são utilizados em contêineres diferentes. Não devemos misturar `pack()` e `grid()` para posicionar componentes que possuem o mesmo contêiner pai.

### 6.3 Eventos e funções dos botões

O parâmetro `command` associa um botão a uma função.

```python
command=atualizar_status
```

A ausência de parênteses é importante: o botão recebe a função para executá-la quando for acionado.

O método `bind()` associa eventos, como pressionar Enter, a uma ação. No projeto, Enter pode cadastrar uma filial ou salvar a edição em andamento.

### 6.4 mainloop e after

O método `mainloop()` mantém a janela processando eventos, como cliques, digitação e tarefas agendadas.

O método `after()` agenda uma chamada para execução posterior pelo ciclo de eventos da interface.

```python
janela.after(
    INTERVALO_ATUALIZACAO,
    executar_monitoramento_automatico
)
```

O agendamento não garante execução no instante exato: depende de a interface estar disponível para processar a chamada.

O método `after()` não cria uma thread nem torna automaticamente uma tarefa demorada mais rápida.

### 6.5 Estado de edição

A variável `filial_em_edicao` guarda o nome original do cadastro que está sendo alterado.

Isso permite localizar o registro mesmo quando o usuário modifica o nome nos campos.

Ao concluir a edição, o estado precisa ser limpo. A exclusão também deve encerrar corretamente uma edição pendente.

## 7. Monitoramento e execução em segundo plano

### 7.1 O que o ping verifica

O ping utiliza mensagens ICMP para verificar se um endereço responde a partir do computador que executa o teste.

Uma resposta positiva indica alcance por ping naquele momento. Ela não comprova que a internet ou todos os serviços da filial estejam funcionando.

A ausência de resposta pode estar relacionada ao equipamento, ao caminho de rede ou a bloqueios de ICMP.

### 7.2 Comando utilizado

O programa executa o equivalente a:

```powershell
ping -n 1 -w 1000 192.0.2.10
```

Nesse comando:

- `-n 1` solicita um único ping.
- `-w 1000` configura a espera pela resposta em milissegundos.
- O último argumento é o endereço de destino.

Esse comportamento é diferente de `ping -t`, que mantém as solicitações contínuas até ser interrompido.

A opção `-w` não é um limite geral de duração para todo o processo Python.

### 7.3 subprocess

O recurso `subprocess.run()` executa o comando externo e aguarda sua conclusão.

No projeto:

- Os argumentos são enviados em uma lista.
- `capture_output=True` captura a saída do comando.
- `text=True` solicita que a saída seja tratada como texto.
- `returncode` informa o código de saída do processo.

A implementação atual interpreta `returncode == 0` como resultado positivo. Essa é a regra utilizada pelo código; sua confiabilidade em diferentes respostas de erro de rede deve ser verificada em testes específicos.

### 7.4 Thread

Uma thread permite executar a tarefa de ping separadamente do processamento principal da interface.

Isso evita que a janela precise esperar cada ping para responder às interações.

Atualmente, existe uma thread para a rodada, mas os roteadores são verificados sequencialmente dentro dela. Não existe um ping simultâneo para cada filial.

### 7.5 Controle de rodadas simultâneas

A variável `monitoramento_em_andamento` informa se já existe uma rodada ativa.

- Antes de iniciar a rodada, recebe `True`.
- Uma nova solicitação é ignorada enquanto ela permanece `True`.
- Ao finalizar a atualização, recebe `False`.

Falhas que interrompam a rodada antes dessa liberação precisam ser tratadas para evitar que o monitoramento fique bloqueado.

### 7.6 Atualização automática

O sistema tenta iniciar uma verificação a cada 10 segundos.

Se a rodada anterior ainda estiver em execução, a nova solicitação é ignorada. Portanto, 10 segundos é o intervalo de agendamento, não uma garantia de atualização de todos os resultados nesse prazo.

O horário exibido na janela registra a conclusão da rodada, não apenas seu início.

## 8. Armazenamento local em JSON

### 8.1 Formato dos dados

JSON é um formato de texto utilizado para representar dados estruturados. Não é um banco de dados nem um código Python executável.

O modelo atual contém uma lista de filiais:

```json
[
  {
    "nome": "Filial Exemplo",
    "ip": "192.0.2.10"
  }
]
```

Uma lista vazia é representada por `[]`.

### 8.2 Leitura e gravação

A função `json.load()` transforma o conteúdo de um arquivo JSON em estruturas do Python.

A função `json.dump()` grava estruturas do Python no formato JSON.

Na gravação do projeto:

- `ensure_ascii=False` permite manter caracteres como acentos no arquivo.
- `indent=4` organiza o JSON com recuo de quatro espaços.
- `encoding="utf-8"` define a codificação utilizada na leitura e na escrita.

Abrir um arquivo com o modo `"w"` substitui seu conteúdo anterior. Por isso, o programa carrega os cadastros, modifica a lista e depois salva o conjunto atualizado.

### 8.3 Localização do arquivo

```python
PASTA_PROJETO = Path(__file__).resolve().parent
ARQUIVO_FILIAIS = PASTA_PROJETO / "filiais.json"
```

Nesse trecho:

- `__file__` identifica o arquivo Python.
- `resolve()` obtém seu caminho absoluto.
- `parent` representa a pasta que contém o arquivo.
- O operador `/` combina a pasta com o nome de `filiais.json`.

Assim, o caminho não depende da pasta em que o terminal estava quando o programa foi iniciado.

### 8.4 Arquivo real e arquivo de exemplo

- `filiais.json` contém os cadastros locais utilizados pela aplicação.
- `filiais.exemplo.json` apresenta o formato esperado com dados fictícios.

O arquivo de exemplo é público e não é carregado automaticamente pelo programa.

## 9. Git, GitHub e arquivos ignorados

### 9.1 O que é o .gitignore?

O arquivo `.gitignore` define padrões de arquivos e pastas que o Git deve ignorar quando ainda não são rastreados.

Ele não exclui esses arquivos do computador e não funciona como uma proteção de acesso.

Adicionar um arquivo ao `.gitignore` não remove automaticamente esse arquivo caso ele já esteja sendo rastreado pelo Git.

### 9.2 Regras usadas neste projeto

```text
filiais.json
__pycache__/
.venv/
```

| Regra | Motivo |
|---|---|
| `filiais.json` | Evitar incluir os cadastros reais no repositório. |
| `__pycache__/` | Ignorar arquivos de cache gerados pelo Python. |
| `.venv/` | Ignorar a pasta de um ambiente virtual local, caso seja criado. |

Ter `.venv/` no `.gitignore` não significa que um ambiente virtual já tenha sido criado ou utilizado.

### 9.3 O que é __pycache__?

A pasta `__pycache__` guarda arquivos de bytecode que o Python pode gerar ao importar ou compilar módulos.

Um exemplo é `dados.cpython-313.pyc`:

- `dados` identifica o módulo.
- `cpython-313` identifica a implementação CPython e a versão 3.13.
- `.pyc` indica um arquivo de bytecode compilado.

Esses arquivos não são destinados à edição manual e podem ser recriados pelo Python.

### 9.4 Principais comandos utilizados

| Comando | Finalidade |
|---|---|
| `git status -sb` | Mostrar resumidamente a branch e o estado dos arquivos. |
| `git diff` | Mostrar alterações rastreadas que ainda não foram preparadas para commit. |
| `git diff --staged` | Mostrar as alterações preparadas para commit. |
| `git diff --check` | Identificar problemas de espaços nas diferenças verificadas. |
| `git add arquivo` | Preparar as alterações de um arquivo para commit. |
| `git commit -m "mensagem"` | Registrar as alterações preparadas no histórico local. |
| `git push` | Enviar os commits locais para o repositório remoto. |
| `git log --oneline` | Consultar o histórico resumido dos commits. |

O comando `git diff --check` sem opções adicionais não verifica o conteúdo de arquivos novos ainda não rastreados.

### 9.5 Significado de M e ??

Na saída de `git status --short` ou `git status -sb`:

- `M` indica modificação.
- `??` indica um arquivo ainda não rastreado.

A posição das marcações nas colunas do status informa se a alteração está preparada para commit ou apenas no diretório de trabalho.

### 9.6 Salvar não é fazer commit

Salvar com `Ctrl + S` grava a alteração no arquivo do computador.

O comando `git add` prepara essa versão para commit.

O comando `git commit` registra a versão no histórico local.

O comando `git push` envia os commits para o GitHub.

Alterações ainda não salvas no editor não são lidas por uma nova execução do programa nem incluídas pelo Git.

## 10. Documentação com Markdown

Markdown é um formato de texto utilizado para organizar documentos com títulos, listas, tabelas e blocos técnicos.

No projeto:

- `#` define o título principal.
- `##` define uma seção.
- `###` define uma subseção.
- Crases destacam arquivos, funções e comandos.
- Tabelas organizam informações comparáveis.
- Blocos técnicos precisam ter abertura e fechamento.

No VS Code, `Ctrl + Shift + V` abre a visualização do Markdown.

As linhas de uma tabela devem permanecer juntas. Inserir um parágrafo entre elas interrompe a tabela.

Os diagramas do projeto utilizam Mermaid dentro de blocos identificados como `mermaid`.

## 11. Verificações e testes

### 11.1 Verificação de sintaxe

```powershell
python -m py_compile dados.py monitoramento.py interface.py
```

Esse comando verifica se os arquivos podem ser compilados. Ele não executa os testes funcionais da aplicação.

Não detectar erro de sintaxe não significa que todas as regras ou situações de uso estejam corretas.

### 11.2 Verificação do JSON de exemplo

```powershell
python -m json.tool filiais.exemplo.json
```

O comando verifica a sintaxe do JSON e apresenta seu conteúdo formatado.

Ele não comprova que o documento possui os campos exigidos pelo programa. Um JSON com o modelo antigo pode ser válido, mas incompatível com a versão atual.

### 11.3 Testes funcionais

Testes funcionais verificam o comportamento observado do programa.

Exemplos praticados:

- Cadastrar uma filial e reabrir o programa.
- Editar um nome e verificar se a alteração permanece.
- Excluir um cadastro e confirmar que ele não reaparece.
- Comparar respostas positivas e negativas de ping.
- Observar o horário mudar em ciclos automáticos.

Os resultados e as pendências devem ser consultados em `testes.md`.

## 12. Lições práticas do projeto

- Conferir o conteúdo completo de um arquivo antes de orientar ou realizar alterações.
- Indicar claramente onde começa e termina cada bloco de código.
- Salvar o arquivo antes de executar os testes.
- Evitar constantes e funções duplicadas.
- Distinguir código sintaticamente válido de funcionalidade efetivamente testada.
- Utilizar evidências observáveis, como o horário da última atualização.
- Preservar testes históricos sem apresentá-los como validação de outro modelo.
- Manter documentação, código e exemplos de dados alinhados.
- Não incluir dados reais da rede no repositório.
- Revisar um conjunto coerente de alterações antes do commit.

## 13. Próximos estudos

- Revisar cada função do projeto e explicar seu fluxo com exemplos.
- Aprofundar listas, dicionários, `enumerate()`, `next()` e `any()`.
- Estudar escopo, funções internas e `nonlocal`.
- Entender melhor a comunicação entre threads e o ciclo de eventos do Tkinter.
- Estudar tratamento de exceções e recuperação de falhas.
- Estudar validação de endereços IP.
- Entender estratégias para evitar leitura e gravação simultâneas do JSON.
- Estudar testes automatizados com dados isolados.
- Avaliar o comportamento do monitoramento com muitas filiais.