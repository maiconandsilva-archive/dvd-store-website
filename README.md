# :abcd: Projeto Segurança da Informação 
[![](https://img.shields.io/badge/python-v3.8-blue)](https://github.com/DevExpress/testcafe) ![](https://img.shields.io/badge/docker%20build-automated-066da5)

> Estudo de caso sobre Anonimização de Dados sensíveis dos clientes da Dell Store usando [PostgreSQL](https://www.postgresql.org/) 

Esse projeto tem o intuito de demonstrar a aplicação de técnicas para um banco de dados anonimizado ideal para uma empresa, seguindo as regras da Lei Geral de Proteção de Dados, fazendo com seja possível a exclusão dos dados sensíveis dos clientes sem a necessidade da exclusão de dados importantes para a empresa, como informações de vendas. Por meio de uma API que simule tal funcionamento.  


## :cd: Dependências

Esta versão requer o Docker e Docker-Compose. Se você está utilizando o Windows [clique aqui](https://docs.docker.com/docker-for-windows/install/).

``` bash
docker-compose version 1.27.4
Docker version 19.03.13
```
#### Principais bibliotecas Python usadas

| Biblioteca | Versão                               |
|-------|--------------------------------------|
| cryptography | 3.2.1 |
| Flask     | 1.1.2                      |
| Flask-SQLAlchemy    | 2.4.4 |
| Flask-WTF | 0.14.3 |
| Jinja2    | 2.11.2             |
| psycopg2     | 2.8.6                  |
| SQLAlchemy    | 1.3.19        |
| SQLAlchemy-Utils | 0.36.8 |
| WTForms-Alchemy | 0.17.0 |

##  :rocket: Inicialização 

``` bash
# Executar aplicação pela primeira vez 
docker-compose up --build -d

# Executar
docker-compose up -d

# URL de acesso 
url: http://127.0.0.1/
```
## :gear: Processo de Desenvolvimento
Como framework de desenvolvimento dessa aplicação foi aplicada o Scrum - Metodologia Ágil de Desenvolvimento de softwares, e as entregas desse projeto foram
divididas em sprints, e para controle dessas, foram utilizados ferramentas como o Nosso [Board no Trello](https://trello.com/b/PyOFWkYC/si) e também nossa Planilha de [BurnDown](https://docs.google.com/spreadsheets/d/1tDluxMUywgS5cD-ZQRGEMXdzJRsSD_wp/edit#gid=699714556).


### Sprint 1
**Destinada à pesquisas e à configuração inicial do projeto.**

- [x] Inicialização do projeto.
- [x] Configuração do ambiente em Docker (serviços de banco de dados e aplicação Flask)

### Sprint 2
**Destinada à criação de rotas e telas principais.**

- [x] Exclusão de usuário com técnica de anonimização
- [x] Rota de listagem dos dados dos clientes pós anonimização.

### Sprint 3
**Destinada à criação de rotas e telas para registro e autenticação.**
g
- [x] Rota para criar conta, login e visualizar dados
- [x] Rota de requisição para deletar conta de usuário (para anonimizar e pseudonomizar)

### Sprint 4
**Destinada à Pseudonimizacao dos dados do usuário/cliente através de requisição e criação de máscaras após requisição para deletar conta (anonimização com fim analítico).**

- [x] Pseudonimização dos dados do usuário
- [x] Aplicar máscaras para os campos e-mail e telefone
- [x] Aplicar máscaras para visualização de dados pessoais na conta do usuario

### [Sprint 5](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/1)
_A partir da sprint 5 o gerenciamento das tarefas mudou para o [Kanban](https://github.com/maiconandsilva/LGPD-compliant-website/projects/1?fullscreen=true) e o [Milestones com Issues](https://github.com/maiconandsilva/LGPD-compliant-website/milestones) do Github._

**Destinada à [revisão da documentação](https://github.com/maiconandsilva/LGPD-compliant-website/issues/5) e à funcionalidade de [solicitação de relatório](https://github.com/maiconandsilva/LGPD-compliant-website/issues/3).**

- [Tarefas abertas](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/1)
- [Tarefas fechadas](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/1?closed=1)

### [Sprint 6](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/2)
**Destinada à correção de bugs, implementação final de telas e demonstração do projeto.**

- [Tarefas abertas](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/2)
- [Tarefas fechadas](https://github.com/maiconandsilva/LGPD-compliant-website/milestone/2?closed=1)

## :anchor: Fontes
- Exemplo da Empresa Dell Store de [Banco de dados ](https://linux.dell.com/dvdstore/) utilizado para anonimização.

## :lock: Licença

Consulte o arquivo [LICENSE](LICENSE) para obter os direitos e limitações da licença (FATEC).

