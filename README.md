# sip api
## Запуск проекта
```
Для запуска необходим Docker, Docker Compose, nginx
```
* Добавить в /etc/hosts  127.0.0.1 sip_api.localhost.com

* Добавить nginx.cfg в sites-enabled nginx
```sh
cd /etc/nginx/sites-enabled
sudo ln -s [путь_до_проекта]/sipapi/configurations/nginx.cfg sip_api.cfg
sudo nginx -t
sudo nginx -s reload
```
* Собрать images по схеме описанной в docker-compose.yml
```sh
make build
```
* Запустить проект
```sh
make start
```

* Проект будет доступен по адресу: *http://sip_api.localhost.com*

* Для получения api token непобходимо перейти по адресу *http://sip_api.localhost.com/users* и ввести логин и пароль

* Остановить все запущенные контейнеры
```sh
make stop
```
## Описание API
=============================================
* Получить список звонков по времение
```sh
Method: GET
http://sip_api.localhost/api/v1/calls?date_from=<timestamp>&date_till=<timestamp>
```
если параметры date_from и date_till не были переданы, то вернется список звонков за тукущий день

* Получить список операторв
```sh
Method: GET
http://sip_api.localhost/api/v1/operators
```

* Получить запись звонка
```sh
Method: GET
http://sip_api.localhost/api/v1/recording?call_id=<id звонка>
```

## Доступные команды из Makefile
* Собрать проект 
```sh
make build
```
* Запустить проект
```sh
make start
```
* Остановить все контейнеры
```sh
make stop
```
* Запуск тестов
```sh
make test
```
