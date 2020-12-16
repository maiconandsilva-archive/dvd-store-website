# :abcd: LGPD Compliant Website
[![](https://img.shields.io/badge/python-v3.8-blue)](#) [![](https://img.shields.io/badge/docker%20build-automated-066da5)]()


## 👁️‍🗨️ Visão geral<a name="visao-geral"></a>

Este projeto tem o intuito de demonstrar a aplicação de técnicas de pseudonimização para um sistema, ideal para uma empresa seguindo as regras da Lei Geral de Proteção de Dados, desta forma permitindo acessar e alterar dados estatísticos sem a necessidade de violar a privacidade dos clientes.


#### 📖 Para mais informações sobre este projeto acesse nossa [Wiki](https://github.com/maiconandsilva/LGPD-compliant-website/wiki).

#### 📶 [Acesse a demonstração online.](https://lgpd-compliant.herokuapp.com)

## :cd: Dependências

Esta versão requer o [Docker e Docker-Compose](https://docs.docker.com/get-docker/).
Se você está utilizando o Windows [clique aqui](https://docs.docker.com/docker-for-windows/install/).

``` bash
docker-compose version 1.27.4
Docker version 19.03.13
```

##  :rocket: Inicialização e execução

1. Clonar repositório
``` bash
git clone https://github.com/maiconandsilva/LGPD-compliant-website.git
```

2. Mudar diretório atual
```bash
cd LGPD-compliant-website
```

3. Copiar arquivos de configurações na pasta _conf_ para a raíz do projeto
```bash
cp conf/* .
```

4. Modificar portas, usuarios e senhas padrão no arquivos de configuração (não é necessário)
> -  .env
> - docker-compose.override.yml

5. Iniciar projeto
```bash
docker-compose up -d
```

6. Carregar dados de scripts sql
```bash
# PARA FUNCIONAR OS SCRIPTS DEVEM ESTAR NA RAÍZ DO PROJETO

# Copia scripts para os containeres
# Mudar argumentos de acordo com configurações
docker cp dump-store.sql lgpd-compliant-website_db_1:/tmp/dump-store.sql

# Trocar o nome do container pelo correspondente, se aplicar
docker cp dump-isolatedstore.sql lgpd-compliant-website_db_isolated_1:/tmp/dump-isolatedstore.sql

# Executa scripts de carregamento dentro dos containeres
docker-compose exec db psql -U postgres -d store -f /tmp/dump-store.sql
docker-compose exec db_isolated psql -U postgres -d isolatedstore -f /tmp/dump-isolatedstore.sql
```

7. Acessar URL http://127.0.0.1:5000 (mudar porta de acordo com configuração)

8. Inserir credenciais de usuário com dados

> **Usuário:** user7@mailinator.com
> **senha:**   password 
