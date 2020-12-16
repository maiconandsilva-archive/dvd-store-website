export COMPOSE_PROJECT_NAME=lgpd-compliant-website
export HEROKU_APP=lgpd-compliant

include .env

BACKEND_SERVICE=backend

DOCKER_COMPOSE=docker-compose
args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`


migrate:
	$(PYTHON_MIGRATION)

build:
	$(DOCKER_COMPOSE) build

start:
	$(DOCKER_COMPOSE) up -d

clean:
	$(DOCKER_COMPOSE) down -v

logs:
	$(DOCKER_COMPOSE) logs --tail 15 $(call args,"")

logs-f:
	$(DOCKER_COMPOSE) logs -f --tail 10 $(call args,"")

in:
	$(DOCKER_COMPOSE) exec $(call args,"") bash

do:
	$(DOCKER_COMPOSE) $(call args,"")

deploy:
	heroku container:push web
	heroku container:release web