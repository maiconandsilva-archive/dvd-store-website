Dell DVD Store CASE
===================

Projeto de Segurança da Informação



GOAL
----


Instalar
-------

createdb -E LATIN1 dellstore2
createlang plpgsql dellstore2
* Save all .csv files from the dell store distribution into the dellstore2 directory *
psql -f dellstore.sql dellstore2

Executar
-------

`docker-compose up -d`

### Rebuilding Images

`docker-compose up --build -d`

Fontes
--------
- [Database Source](https://linux.dell.com/dvdstore/)