


# :abcd: Projeto Seguranca da Informacao 
[![Tested with TestCafe](https://img.shields.io/badge/python-v3.7-blue)](https://github.com/DevExpress/testcafe) ![Tested with TestCafe](https://img.shields.io/badge/docker%20build-automated-066da5)

> Estudo de caso sobre Anonimização de Dados sensiveis dos clientes da Dell usando [PostgreSQL](https://www.postgresql.org/) 

Esse projeto tem o intuito de demonstrar a aplicação de tecnicas para um banco de dados anonimizado ideal para uma empresa, seguindo as regras da Lei Geral de Protecao, fazendo com seja possivel a exclusao dos dados sensiveis dos clientes sem a necessidade da exclusao de dados importantes para a empresa, como informacoes de vendas. Por meio de uma API que simule tal funcionamento.  


## :cd: Dependencias

Esta versão requer o Docker e Docker-Compose. Se você está utilizando o Windows [clique aqui](https://docs.docker.com/docker-for-windows/install/).

``` bash
docker-compose version 1.27.4
Docker version 19.03.13
```

| Ferramenta | Versão                               |
|-------|--------------------------------------|
| Flask     | 1.1.2                      |
| Flask-SQLAlchemy    | 2.4.4 |
| Jinja2    | 2.11.2             |
| psycopg2     | 2.8.6                  |
| SQLAlchemy    | 1.3.19        |

##  :rocket: Inicialização 

``` bash
# Executar aplicação pela primeira vez 
docker-compose up --build -d

# Executar
docker-compose up -d

# URL de acesso 
url: http://127.0.0.1:5000/tests
```

## :beers: Contribuições

Estamos muito felizes em ver contribuições em potencial, então não hesite. Se você tiver alguma sugestão, ideia ou problema, sinta-se à vontade para adicionar um novo [issue](https://github.com/WilliamBarretoH/DataBase-Anonymization/issues), mas primeiro verifique se a sua pergunta não repete as anteriores.


## :lock: Licença

Consulte o arquivo [LICENSE](LICENSE) para obter os direitos e limitações da licença (MIT).


## :gear: Processo de Desenvolvimento
Como framework de desenvolvimento dessa aplicação foi aplicada o Scrum - Metodologia Ágil de Desenvolvimento de softwares, e as entregas desse projeto foram
dividas em sprints como a ferramenta auxilia.

### Sprint 1

- [x] Estudo sobre principais ferramentas SGDB para o projeto.
- [x] Estudo e testes sobre principais liguagens de manipulação de dados.
- [x] Preparação do Ambiente em Docker

### Sprint 2
- [x] Criação de Rotas iniciais para testes de manipulação de dados.
- [x] Exclusao de um usuario com tecnica de anonimizacao 
- [x] Inicio da Anonimizacao de dados ficticios de cliente da Dell
- [ ] Rota de listagem dos dados dos clientes pós anonimização.

### Sprint 3
- [ ] Mascara para dados como o telefone
- [ ] Criptografia dos dados

## :anchor: Fontes
--------
- Exemplo da Empresa Dell de [Banco de dados ](https://linux.dell.com/dvdstore/) utilizado para anonimização.

