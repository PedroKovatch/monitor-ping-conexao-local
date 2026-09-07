# Requisitos do Sistema

## 1. Identificação

- **Projeto:** Monitor de Conexão Local
- **Versão do documento:** 1.4
- **Data:** 07/09/2026
- **Responsável:** Pedro Kovatch
- **Status:** Em elaboração

## 2. Problema a ser resolvido

A equipe de TI precisa acompanhar a resposta de ping dos roteadores das filiais. Atualmente, essa verificação é realizada manualmente, dificultando uma visualização rápida e centralizada.

O Monitor de Conexão Local será uma aplicação desktop desenvolvida em Python. Ele permitirá cadastrar filiais com nome e endereço IP de um único roteador, armazenar esses dados localmente e verificar periodicamente a conectividade a partir do computador em que o programa estiver sendo executado.

## 3. Requisitos funcionais

| Código | Requisito |
|---|---|
| RF01 | O sistema deve permitir o cadastro manual de uma filial, informando seu nome. |
| RF02 | O sistema deve permitir informar um único endereço IP de roteador no cadastro de cada filial. |
| RF03 | O sistema deve armazenar os dados cadastrados localmente, mantendo-os disponíveis após reiniciar o programa. |
| RF04 | O sistema deve exibir uma lista vertical com status de conectividade, nome da filial e IP do roteador. |
| RF05 | O sistema deve iniciar automaticamente o monitoramento ao abrir o programa e realizar verificações periódicas enquanto estiver aberto. |
| RF06 | O sistema deve indicar a resposta positiva ao ping com indicador verde e texto Online. |
| RF07 | O sistema deve indicar a ausência de resposta ao ping com indicador vermelho e texto Indisponível. |
| RF08 | O sistema deve permitir solicitar uma atualização manual dos status. |
| RF09 | O sistema deve permitir editar o nome e o IP de uma filial cadastrada. |
| RF10 | O sistema deve permitir excluir uma filial selecionada, solicitando confirmação antes da exclusão. |
| RF11 | O sistema deve exibir o horário da última atualização concluída. |
| RF12 | O sistema deve exibir Aguardando quando não houver resultado de ping disponível para o registro apresentado. |

## 4. Requisitos não funcionais

| Código | Requisito |
|---|---|
| RNF01 | O sistema deve ser executado localmente em computadores com sistema operacional Windows. |
| RNF02 | O sistema deve ser desenvolvido utilizando a linguagem Python. |
| RNF03 | A interface deve ser simples, com tema escuro e foco na visualização rápida do status dos roteadores das filiais. |
| RNF04 | Os dados das filiais devem ser armazenados em arquivo local no formato JSON, sem utilização de banco de dados. |
| RNF05 | Os endereços IP reais das filiais não devem ser enviados ao repositório do GitHub. |
| RNF06 | A atualização automática não deve travar a interface durante as verificações de ping. |

## 5. Escopo da primeira versão

A primeira versão do Monitor de Conexão Local terá como foco o cadastro local de filiais e equipamentos, além do monitoramento visual automático da resposta de ping dos respectivos endereços IP.

### 5.1 Funcionalidades previstas

- Cadastro de filial com nome e IP do roteador.
- Edição e exclusão de cadastros.
- Armazenamento local dos dados em JSON.
- Listagem de status, filial e IP.
- Atualização manual e automática.
- Indicadores de aguardando, online e indisponível.
- Exibição do horário da última atualização concluída.

### 5.2 Funcionalidades fora do escopo

- Banco de dados.
- Sistema web.
- Login de usuários.
- Envio de e-mails, mensagens ou notificações externas.
- Relatórios avançados e gráficos.
- Integração com sistemas externos.
- Cadastro de múltiplos roteadores ou equipamentos por filial.
- Verificação do funcionamento da internet e de serviços além da resposta ao ping.

## 6. Regras de negócio

| Código | Regra |
|---|---|
| RB01 | Um roteador será considerado online quando seu endereço IP responder à solicitação de ping. |
| RB02 | Um roteador será considerado indisponível quando seu endereço IP não responder à solicitação de ping. |
| RB03 | O status online deve ser representado pela cor verde. |
| RB04 | O status indisponível deve ser representado pela cor vermelha. |
| RB05 | O monitoramento deve continuar enquanto o programa estiver aberto. |
| RB06 | Os dados cadastrados devem ser carregados automaticamente ao iniciar o programa. |
| RB07 | Cada filial deve possuir um único roteador cadastrado, identificado por um endereço IP. |
| RB08 | O sistema não deve permitir nomes de filiais duplicados, sem diferenciar letras maiúsculas e minúsculas, tanto no cadastro quanto na edição. |
| RB11 | O cadastro e a edição não devem aceitar nome ou IP vazios após remover espaços no início e no fim dos campos. |
| RB12 | O sistema deve tentar iniciar uma verificação automática a cada 10 segundos, sem iniciar outra enquanto a anterior estiver em andamento. |
| RB13 | A atualização manual deve respeitar a mesma proteção contra verificações simultâneas. |
| RB14 | A exclusão deve ocorrer somente após confirmação do usuário. |
| RB15 | O horário da última atualização deve ser alterado quando o ciclo de verificação for concluído. |

As regras RB09 e RB10 foram retiradas na versão 1.4 porque tratavam de múltiplos equipamentos dentro da mesma filial. Seus códigos não serão reutilizados.

O intervalo de 10 segundos corresponde ao agendamento das verificações, não à garantia de conclusão de todos os pings nesse prazo. Se uma rodada ainda estiver em andamento, a tentativa de iniciar outra será ignorada.

O status representa a resposta ao ping a partir do computador que executa o programa. A ausência de resposta não determina, isoladamente, a causa da indisponibilidade.

## 7. Critérios de aceitação

A primeira versão será considerada aceita quando:

- For possível cadastrar uma filial com nome e IP de um único roteador.
- Campos vazios e nomes duplicados forem recusados no cadastro e na edição.
- For possível editar nome e IP de uma filial.
- For possível cancelar uma exclusão sem remover o cadastro.
- Uma exclusão confirmada remover o cadastro.
- Cadastros, edições e exclusões permanecerem após reiniciar o programa.
- A lista apresentar status, nome da filial e IP do roteador.
- O monitoramento iniciar automaticamente e continuar enquanto o programa estiver aberto.
- O agendamento automático ocorrer a cada 10 segundos, sem sobrepor verificações.
- A atualização manual funcionar sem iniciar verificações simultâneas.
- A interface permanecer responsiva durante os pings.
- Uma resposta positiva ao ping produzir indicador verde e texto Online.
- A ausência de resposta produzir indicador vermelho e texto Indisponível.
- O horário da última atualização mudar após cada ciclo concluído.
- O arquivo com os IPs reais permanecer fora do repositório do GitHub.