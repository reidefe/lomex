# lomex
full-stack django app

# build app

## [Development Environment] Docker build and project startup
```
docker-compose up --build
```


### [Development Environment] Execute Django commands
```
docker-compose run web python 'django commands' for example:
docker-compose run web python manage.py migrate
docker-compose run web python manage.py load
docker-compose run web python manage.py makemigrations 
```

### sqlite data
```
Данные SQLite были загружены подклассом BaseCommand Django manage.py load, чтобы упростить загрузку данных в db. Файл находится в management / commands.
Postgres был выбран, потому что у него есть поле массива, а в SQLite его нет, поэтому я мог бы его использовать.
Кроме того, я не мог загрузить данные непосредственно в базу данных с помощью pandas dataframe.to_sql, потому что данные не коррелировали с указанными полями в требовании.
Мне также пришлось изменить данные, чтобы они соответствовали требуемой структуре в приложении. Я также задокументировал это с помощью swagger и redoc. Так что нет необходимости во внешнем интерфейсе. Хотя я сделал контейнер для интерфейса. linting и formatting проводились с использованием flake8 и black.
```
### Swagger and redoc endpoints
```
http://0.0.0.0:8000/doc/
http://0.0.0.0:8000/redoc/

```
