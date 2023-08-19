# vultus-law-backend

### DOCKER COMMANDS

docker-compose run --rm app sh -c "django-admin startproject app ."    container içi komut çalıştırma

docker-compose run --rm app sh -c "django-admin startapp core"    container içi komut çalıştırma


### TEST
docker-compose run --rm app sh -c "python manage.py test"


docker-compose run --rm app sh -c "pip install django-graphiql"