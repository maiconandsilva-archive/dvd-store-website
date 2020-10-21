# :abcd: Projeto Segurança da Informação 
[![Tested with TestCafe](https://img.shields.io/badge/python-v3.7-blue)](https://github.com/DevExpress/testcafe) ![Tested with TestCafe](https://img.shields.io/badge/docker%20build-automated-066da5)

> Estudo de caso sobre Anonimização de Dados sensíveis dos clientes da Dell Store usando [PostgreSQL](https://www.postgresql.org/) 

Esse projeto tem o intuito de demonstrar a aplicação de técnicas para um banco de dados anonimizado ideal para uma empresa, seguindo as regras da Lei Geral de Proteção de Dados, fazendo com seja possível a exclusão dos dados sensíveis dos clientes sem a necessidade da exclusão de dados importantes para a empresa, como informações de vendas. Por meio de uma API que simule tal funcionamento.  


## :cd: Dependências

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

Consulte o arquivo [LICENSE](LICENSE) para obter os direitos e limitações da licença (FATEC).


## :gear: Processo de Desenvolvimento
Como framework de desenvolvimento dessa aplicação foi aplicada o Scrum - Metodologia Ágil de Desenvolvimento de softwares, e as entregas desse projeto foram
divididas em sprints como a ferramenta auxilia.

### Sprint 1

- [x] Estudo sobre principais ferramentas SGDB para o projeto.
- [x] Estudo e testes sobre principais linguagens de manipulação de dados.
- [x] Preparação do Ambiente em Docker

### Sprint 2
- [x] Criação de Rotas iniciais para testes de manipulação de dados.
- [x] Exclusão de um usuário com técnica de anonimização 
- [x] Início da Anonimização de dados fictícios de cliente da Dell Store
- [x] Rota de listagem dos dados dos clientes pós anonimização.

### Sprint 3
- [ ] Máscara para dados como o telefone
- [ ] Criptografia da senha do usuário
- [ ] Rota de criar usuário
- [ ] Botão para ativar rota de anonimização
- [ ] BurnDown / Velocity Chart
### Sprint 4

- [ ] Validação dos campos do usuário
- [ ] Autenticação

### Sprint 5

- [ ] Telas de interação do usuário

## :anchor: Fontes
- Exemplo da Empresa Dell Store de [Banco de dados ](https://linux.dell.com/dvdstore/) utilizado para anonimização.

