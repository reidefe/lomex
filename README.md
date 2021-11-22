# lomex
full-stack django app

# build app

## [Development Environment] Docker build and project startup
```
docker-compose up --build
```


### [Development Environment] Execute Django commands
```
docker-compose  web python 'django commands' for example:
docker-compose  web python manage.py migrate
docker-compose  web python manage.py load
```

### sqlite data
```
Данные SQLite были загружены с помощью базовой команды Django, чтобы упростить загрузку данных в базу данных.
Postgres был выбран, потому что у него есть поле массива, а в SQLite его нет, поэтому я мог бы его использовать.
Кроме того, я не мог загрузить данные непосредственно в базу данных с помощью pandas dataframe.to_sql, потому что данные не коррелировали с указанными полями в требовании.
Мне также пришлось изменить данные, чтобы они соответствовали требуемой структуре в приложении. Я также задокументировал это с помощью чванства и повторных документов. 
Так что нет необходимости во внешнем интерфейсе. Хотя я сделал контейнер для интерфейса. Линтинг и формование проводились с использованием flake8 и black.
```
